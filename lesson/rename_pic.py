import os
import subprocess,time
import pytz
import hashlib
import datetime

def os_cmd(cmd,is_debug=False):
    if is_debug:
        print(cmd)
    else:
        os.system(cmd)

def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return size
    except Exception as err:
        print(err)
        return 0

def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "{:.2f}Gb".format(G)
        else:
            return "{:.2f}Mb".format(M) 
    else:
        return "{:.2f}Kb".format(kb)

def get_md5_01(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
  return md5

def get_md5_02(file_path):
  f = open(file_path,'rb') 
  md5_obj = hashlib.md5()
  while True:
    d = f.read(8096)
    if not d:
      break
    md5_obj.update(d)
  hash_code = md5_obj.hexdigest()
  f.close()
  md5 = str(hash_code).lower()
  return md5
 
def get_from_pohto(file_path):
    import exifread 
    #加载 ExifRead 第三方库  https://pypi.org/project/ExifRead/
    #获取照片时间、经纬度信息
    #photo参数：照片文件路径
    
    # Open image file for reading (binary mode) 
    f = open(file_path, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    properties = {'callback':'success','file_path':file_path}
    try:
        #拍摄时间
        Lat = ""
        Lon = ""
        EXIF_Date=tags["EXIF DateTimeOriginal"].printable
        
        # #纬度
        # LatRef=tags["GPS GPSLatitudeRef"].printable
        # Lat=tags["GPS GPSLatitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        # Lat=float(Lat[0])+float(Lat[1])/60+float(Lat[2])/float(Lat[3])/3600
        # if LatRef != "N":
        #     Lat=Lat*(-1)
        # #经度
        # LonRef=tags["GPS GPSLongitudeRef"].printable
        # Lon=tags["GPS GPSLongitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        # Lon=float(Lon[0])+float(Lon[1])/60+float(Lon[2])/float(Lon[3])/3600
        # if LonRef!="E":
        #     Lon=Lon*(-1)
        properties['create_time'] = EXIF_Date
        f.close()
        return properties
    except:
        return {'callback':'failed','file_path':file_path}


def get_from_filename(file_path,time_format):
    properties = {'callback':'success','file_path':file_path}
    try:
        create_str = file_path.split('/')[-1].split('.')[0]
        create_time_cn=time.mktime(time.strptime(create_str,time_format))+int(0)*60*60
        create_str_cn = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(create_time_cn))
        properties['create_time']  = create_str_cn
        return properties
    except:
        return {'callback':'failed','file_path':file_path}

def get_from_media(file_path):

    try:
        result = subprocess.Popen(['hachoir-metadata', file_path, '--raw'],
            stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

        results = result.stdout.read().decode('utf-8').split('\n')
        properties = {'callback':'success','file_path':file_path}
        for item in results:
            if item.startswith('- creation_date: '):
                create_str =  item.lstrip('- creation_date: ')
                create_time_cn=time.mktime(time.strptime(create_str,'%Y-%m-%d %H:%M:%S'))+int(8)*60*60
                create_str_cn = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(create_time_cn))
                properties['create_time']  = create_str_cn
            if item.startswith('- duration: '):
                properties['duration']   = item.lstrip('- duration: ')

            if item.startswith('- width: '):
                properties['width'] = int(item.lstrip('- width: '))

            if item.startswith('- height: '):
                properties['height'] = int(item.lstrip('- height: '))
        return properties
    except:
        return {'callback':'failed','file_path':file_path}

def rename_pic(folder_name,folder_name_new):
    i = 0
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            i = i + 1
            file_name = "{}/{}".format(root, f)
            file_ext = f.split('.')[-1].lower()
            properties =  {'callback':'failed'} 
            if file_ext in[ 'mp4','mov']:
                properties = get_from_media(file_name)
            elif file_ext in['jpeg','jpg','png','heic']:
                properties = get_from_pohto(file_name)

            if properties['callback'] == 'failed':
                time_format = '%Y-%m-%d %H%M%S'
                properties = get_from_filename(file_name,time_format)

            if properties['callback'] == 'failed':
                time_format = '%Y-%m-%d %H-%M-%S'
                properties = get_from_filename(file_name,time_format)

            print(properties)
            if properties['callback'] == 'success':
                file_info = properties['create_time']
                new_folder_name = '{}/{}'.format(folder_name_new,file_info[0:7].replace(':','-'))
                new_file_name =  '{}-{}.{}'.format(file_info[0:10].replace(':','-'),file_info[11:19].replace(':',''),file_ext)
                new_file_path = '{}/{}'.format(new_folder_name,new_file_name)
                os_cmd("mkdir -p " +new_folder_name)                       # 创建路径 
                os_cmd("mv \"{}\" \"{}\"".format(file_name, new_file_path)) 
            # exit()

def move_file(folder_name,folder_name_new):
    i = 0
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            i = i + 1
            file_name=file_name = "{}/{}".format(root, f)
            file_name_new="{}/{}".format(folder_name_new,file_name[len(folder_name)+1:])
            folder_name_target = file_name_new.split(f)[0]
            os_cmd("mkdir -p \"{}\"".format(folder_name_target))
            os_cmd("mv \"{}\" \"{}\"".format(file_name, file_name_new)) 
            # print(file_name)
            if i % 100 == 0:
                print(i)
    print(i)                

def get_file_info(folder_name):
    # load data infile '/Users/fat/Desktop/Z__Cloud.csv' into table t_files;
    file = open('{}.csv'.format(folder_name.replace(':','_').replace('\\','_').replace("/",'_')), 'w',encoding='utf-8')
    dir_last = ""
    cnt_last = 0
    size_last = 0
    t0 = datetime.datetime.now()
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            file_name=file_name = "{}/{}".format(root, f)
            file_size = getDocSize(file_name)
            if file_size < 8*1024*1024:
                file_md5=get_md5_01(file_name)
            else:
                file_md5=get_md5_02(file_name)
            file_info_str="{}\t{}\t{}\t{}".format(root.replace('\\','/'), f,file_size,file_md5)     
            file.write(file_info_str+'\n')
            if dir_last != root:
                dur_last = (datetime.datetime.now() - t0).total_seconds()
                print("cnt:{:<7d}size:{:>12}\tDur:{:.2f}\t{}".format(cnt_last,formatSize(size_last),dur_last,dir_last,))   
                cnt_last = 0
                size_last = 0
                t0 = datetime.datetime.now()   
            size_last = size_last + file_size  
            cnt_last = cnt_last + 1
            dir_last = root   
    dur_last = (datetime.datetime.now() - t0).total_seconds()
    print("cnt:{:<7d}size:{:>12}\tDur:{:.2f}\t{}".format(cnt_last,formatSize(size_last),dur_last,dir_last,))     
    file.close()
if __name__ == '__main__':

    # test_file = '/doc/PIC_new/2018-07/2018-07-01 105150.mov'
    # time_format = '%Y-%m-%d %H%M%S'
    # print(get_from_filename(test_file,time_format))
    # folder_name = "/Volumes/disk_admin/Cloud/历史相册/未命名文件夹"
    # folder_name_new = "/Volumes/disk_admin/Cloud/历史相册"

    # rename_pic(folder_name,folder_name_new)
    # get_file_info("Z:/")
    move_file('/Volumes/TimeMachine2/Users/Moyuss/Backup_backup/历史相册/来自moyuPhone的相册','/Volumes/TimeMachine2/Users/Moyuss/Backup_backup/历史相册')
    
