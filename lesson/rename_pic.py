import os
import subprocess,time
import pytz

def os_cmd(cmd,is_debug=False):
    if is_debug:
        print(cmd)
    else:
        os.system(cmd)

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
        print(create_str)
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

test_file = '/doc/PIC_new/2018-07/2018-07-01 105150.mov'
time_format = '%Y-%m-%d %H%M%S'
print(get_from_filename(test_file,time_format))

folder_name = "/doc/PIC"
folder_name_new = "/doc/PIC"
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

        print(f,properties)
        if properties['callback'] == 'success':
            file_info = properties['create_time']
            new_folder_name = '{}/{}'.format(folder_name_new,file_info[0:7].replace(':','-'))
            new_file_name =  '{}-{}.{}'.format(file_info[0:10].replace(':','-'),file_info[11:19].replace(':',''),file_ext)
            new_file_path = '{}/{}'.format(new_folder_name,new_file_name)
            os_cmd("mkdir -p " +new_folder_name)                       # 创建路径 
            os_cmd("mv \"{}\" \"{}\"".format(file_name, new_file_path)) 
        # exit()

