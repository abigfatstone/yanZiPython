# encoding:utf-8
import os
import base64
import requests
import cv2
import numpy as np
from os import listdir
from PIL import Image
import wand
# do not set True!
GO_BAIDU = True

IS_DEBUG = False

def get_token():
    client_key = 'ulGgLNEs8B5L4259UHRqglni'
    client_secret= '2SNhN7bbvHSusaHr3Va1bptwYxjlmivD'
    grant_type = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'
    curl_get_access = 'curl -i -k \'{}&client_id={}&client_secret={}\''.format(grant_type,client_key,client_secret)
    print(curl_get_access)
    tmpres = os.system(curl_get_access)
    print(tmpres)

def jpg_2_base64(filePath):
    with open(filePath,"rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read())#使用base64进行加密\
    return base64_data

def base64_2_jpg(filePath,base64_string):
    # with open("C:\\Users\\wonai\\Desktop\\1.txt","r") as f:
    #str = "iVBORw0KGgoAAAANSUhEUgAAANwAAAAoCAIAAAAaOwPZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQuSURBVHhe7ZptmoMgDIR7rh6o5+lpvEwP01XUGshAokgX+8z+7PKRTF6SoN7e/KMCnSlw68wemkMF3oSSEHSnAKHsLiQ0iFCSge4UIJTdhYQGEUoy0J0ChLK7kNAgQkkGulOAUHYXEhpEKMlAdwpcG8rhcRv/HkN3stIgW4F88DYoX89nObjmANuOc0eMXpHHcyX9+mowhgHKmdlChM0BZzvzet6DSSW7xjEWk8Hu+/O1x7zF1237/Uu4t/O46V6sZuARoZb9KqbO7On4rJlykqcYYnNAjSbx3Gmrj6WTzxirVlA+90F82G+nm4fX3zOxgqyKqRaUU7b8FpRDOeyjJa7k5oByT1yWse4mxfDC3NrrprnQtQeUMuUXoURmCGHdKfl/oTS8MElxu2mudO0BXUCZL8efVGU0EmsQjkGpM2H8y/CwGtW1C3el8ywxhHKWxgOlaPNj0VcRRW+OoiKvCXF0o6YeXWLQDaNQyMf1Clhsi22D9HUNXOBCVZamaBmiO5BxRdRQOt3M3oFUAD4/HDolSChx7AvXzRIJQtgsUfMu6HB+HglNLc5d5KiwpcAqTH7Idk/lvLD9Z0rUx4vYWL2UJ4WY6XbdL91ML57+EjsRNEMnw/LCrKklN9NNkbuLvKsdabjM/ZMByh+PDWuuw6kDEYXPzeSfzGARlNG1M1ENRCfGLlUuJ5MVTg+UyxGzC+1+KN/DkDyuTSVbqo7vNnagfKPTrH9b8pQtgQ/PRCifDTaUJaIWw8adUycklLrcppkyCZfkJ5cYlSZnQTkmsYf58OYAlMpg6JnlhYlC9uxhIdWvbr1NS8Ahc9pgQlkkai3fOorVUK4JGeYTJIgVTm+mnCqrmSfOgDJ0mOlOlhcmClk3M0KmPzeF0mnDGVB6LjqbmKB8p5GRQ34DStRCdpEpp5MRNWRNocwsjk9i7nyqugzPYTWUSZuqe0qVucAT5tgH9ITmxEdCdihjpcCVAgfI8uJ4pgx3K3UhgBeRQ9dtbJmjp1TnYmsKoSH1UGqKE23mxlrsri4yKsuAFnZ5BrAugypw0/IdSvHmxHJbEI6lREzj0asuOc7TR8BONdd9pNKCo4LRNY9CdgCEXjqObDhQvsFpy7z7DsqHP9khxp9DzNeKbSR+Iy3/n31tqVFYe17xFUZkTu507+4px4USFwBRm32lbzFyXphgRMtn3cwqqaef8a0UrMHlaJYM8RC1Iq2DeOXvKUdVjALmzromST8+4N+Egm9rrwzl/DpAVlddnE9su36Jyx6ECtkUxufaUMJOzfwQsxldUbnTLyO/ckCcNsS112yDmkkGF/4xKL8rHndrowChbKMrV61QgFBWiMepbRQglG105aoVChDKCvE4tY0ChLKNrly1QgFCWSEep7ZRgFC20ZWrVihAKCvE49Q2ChDKNrpy1QoF/gDXIhmWmc+CSAAAAABJRU5ErkJggg=="
    imgdata = base64.b64decode(base64_string)
    file = open(filePath,'wb')
    file.write(imgdata)
    file.close()

def get_filePath(filePath_path):
    return filePath_path.split('/')[-1].split('.')[0]

def get_folderPath_out(folderPath,api_name):
    return "{}/{}/{}".format(os.path.dirname(folderPath),api_name,folderPath.split('/')[-1])

def get_filePath_out(filePath,folderPath_home,folderPath_out_base,project_name,api_name):
    folderPath_out_home = "{}/{}/{}".format(folderPath_out_base,api_name,project_name)
    filePath_more = filePath[len(folderPath_home)+1:]
    filePath_out = "{}/{}".format(folderPath_out_home,filePath_more)
    fileName = filePath.split('/')[-1]
    folderPath_out = filePath_out[:len(filePath_out)-len(fileName)-1]
    if IS_DEBUG:
        print("filePath:\t{}\nfilePath_out:\t{}\nfolderPath_out:\t{}\nfileName:\t{}".format(filePath,filePath_out,folderPath_out,fileName))
    else:
        print(filePath_out)    
    os.system("mkdir -p \"{}\"".format(folderPath_out))
    return filePath_out,fileName,folderPath_out

def get_file_list(folderPath):
    file_list = []
    for root, dirs, files in os.walk(folderPath):
        for f in files:
            if f.split('.')[-1].lower() in ['png','jpeg','jpg']:
                filePath=filePath = "{}/{}".format(root, f)
                file_list.append(filePath)
    file_list.sort()     
    if IS_DEBUG:
        return [file_list[0]]
    else:       
        return file_list


def pdf_2_jpg(folderPath_home,folderPath_out_base,project_name):
    from wand.image import Image
    api_name = 'source'
    filePath = "{}.{}".format(folderPath_home,'pdf')
    # 将pdf文件转为jpg图片文件
    # ./PDF_filePath 为pdf文件路径和名称
    image_pdf = Image(filename=filePath,resolution=300)
    image_jpeg = image_pdf.convert('jpg')
    
    # wand已经将PDF中所有的独立页面都转成了独立的二进制图像对象。我们可以遍历这个大对象，并把它们加入到req_image序列中去。
    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))
    
    # 遍历req_image,保存为图片文件
    i = 0
    fileName = filePath.split('/')[-1]
    file_ext = fileName.split('.')[-1]

    fileName_clean = fileName[:len(fileName)-len(file_ext)-1]
    print(fileName,file_ext,fileName_clean)    
    os.system("mkdir -p \"{}/{}/{}\"".format(folderPath_out_base,api_name,fileName_clean))
    for img in req_image:
        fileName_out = "{}/{}/{}/{}_{:0>4d}.jpg".format(folderPath_out_base,api_name,fileName_clean,fileName_clean,i)
        print("fileName_out:\t".format(fileName_out))
        ff = open(fileName_out,'wb')
        ff.write(img)
        ff.close()
        i += 1

def pic_cut(filePath,filePath_out,p_cut):
    box_bottom = p_cut[0][1]
    box_top = p_cut[1][1]
    box_left = p_cut[0][0]
    box_right = p_cut[1][0]
    img = cv2.imread(filePath).astype(np.float32)
    img = img[box_bottom:box_top, box_left:box_right] 
    cv2.imwrite(filePath_out, img)

def pic_cut_folder(folderPath_home,folderPath_out_base,project_name,cut_list):
    api_name = 'cutfile'  
    file_list = get_file_list(folderPath_home)
    print("folderPath_home:{}".format(folderPath_home))
    for filePath in file_list:
        i = 0
        filePath_out,fileName,folderPath_out = get_filePath_out(filePath,folderPath_home,folderPath_out_base,project_name,api_name)
        file_ext = fileName.split('.')[-1]
        fileName_clean = fileName[:len(fileName)-len(file_ext)-1]
        for p_cut in cut_list:
            i = i + 1
            filePath_out_i = "{}/{}_{}.{}".format(folderPath_out,fileName_clean,i,file_ext)
            if IS_DEBUG:
                print("filePath_out_i:\t{}".format(filePath_out_i))
            pic_cut(filePath,filePath_out_i,p_cut)

def resize_pic(folderPath_home,folderPath_out_base,project_name,max_size = 1280):
    api_name = 'resize'    
    file_list = get_file_list(folderPath_home)

    for filePath in file_list:
        im_resize = Image.open(filePath)
        filePath_out,fileName,folderPath_out = get_filePath_out(filePath,folderPath_home,folderPath_out_base,project_name,api_name)
        width, height = im_resize.size
        if width >=height:
            ratio = max_size / width
        else:
            ratio = max_size / height
        new_img = im_resize.resize((int(width*ratio), int(height*ratio)), Image.BILINEAR)
        new_img.save(filePath_out)

# def load_pic(source_fname):
#     img = cv2.imread(source_fname).astype(np.float32)
#     x = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     x = np.array(x, dtype=np.uint8)
#     return x

# def concate_pic(left_pic,right_pic,convert_fname):
#     x_left = load_pic(left_pic)
#     print(x_left.shape)
#     x_right = load_pic(right_pic)
#     print(x_right.shape)
#     x = np.concatenate((x_left,x_right),axis=-1)  
#     img = cv2.cvtColor(x.astype(np.float32), cv2.COLOR_RGB2BGR)
#     cv2.imwrite(convert_fname, img)

def call_baidu_api(request_url,access_token,filePath,filePath_out):
    # 二进制方式打开图片文件
    f = open(filePath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        baidu_response = response.json()
        if 'image' in baidu_response:
            image_base64 = response.json()['image']
            base64_2_jpg(filePath_out,image_base64)
        else:
            print(baidu_response)

def baiduai_pic_dir(folderPath_home,folderPath_out_base,project_name,request_url,access_token):
    api_name = request_url.split('/')[-1]
    print("folderPath_home:\t".format(folderPath_home))
    file_list = get_file_list(folderPath_home)
    for filePath in file_list:
        im_resize = Image.open(filePath)
        filePath_out,fileName,folderPath_out = get_filePath_out(filePath,folderPath_home,folderPath_out_base,project_name,api_name)
        if GO_BAIDU:
            call_baidu_api(request_url,access_token,filePath,filePath_out)
        else:
            os.system("cp \"{}\" \"{}\"".format(filePath,filePath_out))

def concate_pic(filePath_out,im_list,step=2,concate_type='width'):
    # 获取第一张图片尺寸
    width, height = im_list[0].size
    # 图片转化为相同的尺寸
    ims = []
    for im_resize in im_list:
        new_img = im_resize.resize((width, height), Image.BILINEAR)
        ims.append(new_img)

    if concate_type == 'width':
        # 创建空白长图
        result = Image.new(ims[0].mode, (width * step, height))
        # 拼接图片
        for i, im in enumerate(ims):
            result.paste(im, box=(i * width,0))
    else:
        # 创建空白长图
        result = Image.new(ims[0].mode, (width, height * step))
        # 拼接图片
        for i, im in enumerate(ims):
            result.paste(im, box=(0, i * height))            
    # 保存图片
    result.save(filePath_out)

def concate_pic_dir(folderPath_home,folderPath_out_base,project_name,step=2,concate_type='width'):
    api_name = 'concate'
    # 获取当前文件夹中所有JPG图像
    file_list = get_file_list(folderPath_home)
    i = 0
    im_list= []
    for filePath in file_list:
        filePath_out,fileName,folderPath_out = get_filePath_out(filePath,folderPath_home,folderPath_out_base,project_name,api_name)
        i= i + 1
        im_list.append(Image.open(filePath))
        if i % step == 0:
            concate_pic(filePath_out,im_list,step,concate_type)
            im_list= [] #重置List
    if len(im_list)>0:
        concate_pic(filePath_out,im_list,step,concate_type)

if __name__ == '__main__':
    access_token = '24.a69a3c1d5770c166b131f84f6f039003.2592000.1619423916.282335-23878835'

    folderPath_out_base = '/Users/fat/Desktop'
    folderPath_home = "/Users/fat/Desktop/cutfile/牛津树 400+"
    project_name = folderPath_home.split('/')[-1]

    # pdf to jpg，folderPath_home including pdf filename，remove the file_ext ".pdf"
    # folderPath_home = "/Volumes/TimeMachine1/Users/public/Child/闪卡/幼儿英语单词配图闪卡-高清打印版"
    # project_name = folderPath_home.split('/')[-1]
    # pdf_2_jpg(folderPath_home,folderPath_out_base,project_name) 

    # 剪切图片
    # cut_list = [[[6,6],[1258,1800]],[[6+1300,6],[1258+1300,1800]]]
    # cut_list = [[[6,6],[1258,1800]]]
    # folderPath_home = "{}/{}/{}".format(folderPath_out_base,'resize',project_name)
    # pic_cut_folder(folderPath_home,folderPath_out_base,project_name,cut_list)
    
    # resize pic to MaxSize 1280 for baidu API
    # folderPath_home = "{}/{}/{}".format(folderPath_out_base,'source',project_name)
    # resize_pic(folderPath_home,folderPath_out_base,project_name) 

    # 色彩增强
    # request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/color_enhance"
    
    # 清晰度增强
    # folderPath_home = "{}/{}/{}".format(folderPath_out_base,'cutfile',project_name)
    # request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
    # baiduai_pic_dir(folderPath_home,folderPath_out_base,project_name,request_url,access_token)
    
    # 无损放大
    folderPath_home = "{}/{}/{}".format(folderPath_out_base,'cutfile',project_name)
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_quality_enhance"
    baiduai_pic_dir(folderPath_home,folderPath_out_base,project_name,request_url,access_token)

    # 拼接图片
    # folderPath_home = "{}/{}/{}".format(folderPath_out_base,'resize',project_name)
    # concate_pic_dir(folderPath_home,folderPath_out_base,project_name,2,'height')