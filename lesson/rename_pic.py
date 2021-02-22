import os
import shutil
def exifread_infos(photo):
    import exifread 
    #加载 ExifRead 第三方库  https://pypi.org/project/ExifRead/
    #获取照片时间、经纬度信息
    #photo参数：照片文件路径
    
    # Open image file for reading (binary mode) 
    f = open(photo, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    if len(photo.split(' ')) == 2:
        file_name = photo.split('/')[-1]
        print(file_name)
        return file_name.replace("-",':'),'',''
    else:    
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
            f.close()
        except :
            return "ERROR"
        else:
            return EXIF_Date,Lat,Lon

# test_file = '/Volumes/disk_Moyuss/Backup/照片/moyu的iPhone/2013-12-11 205523.jpg'
# exifread_infos(test_file)

folder_name = "/Volumes/disk_Moyuss/Backup/照片/moyu的iPhone"
folder_name_new = "/Volumes/disk_Moyuss/Backup/照片_new"
i = 0
for root, dirs, files in os.walk(folder_name):

    for f in files:
        i = i + 1
        file_name = "{}/{}".format(root, f)
        file_info = exifread_infos(file_name)
        if file_info != 'ERROR':
            file_ext = f.split('.')[-1]
            new_folder_name = '{}/{}-{}'.format(folder_name_new,file_info[0].split(":")[0] ,file_info[0].split(":")[1])

            new_file_name = '{}-{}-{}-{}.{}'.format(file_info[0].split(":")[0] ,file_info[0].split(":")[1],file_info[0].split(":")[2].split(" ")[0],i,file_ext)

            os.system("mkdir -p " +new_folder_name)                       # 创建路径 
            shutil.move(file_name, "{}/{}".format(new_folder_name,new_file_name)) 



    # # 遍历所有的文件夹
    # for d in dirs:
    #     print(os.path.join(root, d))
