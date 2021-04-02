import os
import base64

def jpg_2_base64(file_name):
    with open(file_name,"rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read())#使用base64进行加密\
    return base64_data

def base64_2_jpg(file_name,base64_string):
    # with open("C:\\Users\\wonai\\Desktop\\1.txt","r") as f:
    #str = "iVBORw0KGgoAAAANSUhEUgAAANwAAAAoCAIAAAAaOwPZAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQuSURBVHhe7ZptmoMgDIR7rh6o5+lpvEwP01XUGshAokgX+8z+7PKRTF6SoN7e/KMCnSlw68wemkMF3oSSEHSnAKHsLiQ0iFCSge4UIJTdhYQGEUoy0J0ChLK7kNAgQkkGulOAUHYXEhpEKMlAdwpcG8rhcRv/HkN3stIgW4F88DYoX89nObjmANuOc0eMXpHHcyX9+mowhgHKmdlChM0BZzvzet6DSSW7xjEWk8Hu+/O1x7zF1237/Uu4t/O46V6sZuARoZb9KqbO7On4rJlykqcYYnNAjSbx3Gmrj6WTzxirVlA+90F82G+nm4fX3zOxgqyKqRaUU7b8FpRDOeyjJa7k5oByT1yWse4mxfDC3NrrprnQtQeUMuUXoURmCGHdKfl/oTS8MElxu2mudO0BXUCZL8efVGU0EmsQjkGpM2H8y/CwGtW1C3el8ywxhHKWxgOlaPNj0VcRRW+OoiKvCXF0o6YeXWLQDaNQyMf1Clhsi22D9HUNXOBCVZamaBmiO5BxRdRQOt3M3oFUAD4/HDolSChx7AvXzRIJQtgsUfMu6HB+HglNLc5d5KiwpcAqTH7Idk/lvLD9Z0rUx4vYWL2UJ4WY6XbdL91ML57+EjsRNEMnw/LCrKklN9NNkbuLvKsdabjM/ZMByh+PDWuuw6kDEYXPzeSfzGARlNG1M1ENRCfGLlUuJ5MVTg+UyxGzC+1+KN/DkDyuTSVbqo7vNnagfKPTrH9b8pQtgQ/PRCifDTaUJaIWw8adUycklLrcppkyCZfkJ5cYlSZnQTkmsYf58OYAlMpg6JnlhYlC9uxhIdWvbr1NS8Ahc9pgQlkkai3fOorVUK4JGeYTJIgVTm+mnCqrmSfOgDJ0mOlOlhcmClk3M0KmPzeF0mnDGVB6LjqbmKB8p5GRQ34DStRCdpEpp5MRNWRNocwsjk9i7nyqugzPYTWUSZuqe0qVucAT5tgH9ITmxEdCdihjpcCVAgfI8uJ4pgx3K3UhgBeRQ9dtbJmjp1TnYmsKoSH1UGqKE23mxlrsri4yKsuAFnZ5BrAugypw0/IdSvHmxHJbEI6lREzj0asuOc7TR8BONdd9pNKCo4LRNY9CdgCEXjqObDhQvsFpy7z7DsqHP9khxp9DzNeKbSR+Iy3/n31tqVFYe17xFUZkTu507+4px4USFwBRm32lbzFyXphgRMtn3cwqqaef8a0UrMHlaJYM8RC1Iq2DeOXvKUdVjALmzromST8+4N+Egm9rrwzl/DpAVlddnE9su36Jyx6ECtkUxufaUMJOzfwQsxldUbnTLyO/ckCcNsS112yDmkkGF/4xKL8rHndrowChbKMrV61QgFBWiMepbRQglG105aoVChDKCvE4tY0ChLKNrly1QgFCWSEep7ZRgFC20ZWrVihAKCvE49Q2ChDKNrpy1QoF/gDXIhmWmc+CSAAAAABJRU5ErkJggg=="
    imgdata = base64.b64decode(base64_string)
    file = open(file_name,'wb')
    file.write(imgdata)
    file.close()

def get_token():
    client_key = 'ulGgLNEs8B5L4259UHRqglni'
    client_secret= '2SNhN7bbvHSusaHr3Va1bptwYxjlmivD'
    grant_type = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'
    curl_get_access = 'curl -i -k \'{}&client_id={}&client_secret={}\''.format(grant_type,client_key,client_secret)
    print(curl_get_access)
    tmpres = os.system(curl_get_access)
    return tmpres
 


def enhance_pic(base64_string):

    url_string = 'https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance?'
    access_token= '24.a69a3c1d5770c166b131f84f6f039003.2592000.1619423916.282335-23878835'
    head_string = 'Content-Type:application/x-www-form-urlencoded'
    curl_get_access = 'curl -i -k \'{}&access_token={}\' --data \'image={}\' -H \'{}\''.format(url_string,access_token,base64_string,head_string)
    # print(curl_get_access)
    # tmpres = os.system(curl_get_access)
    file = open('/Users/fat/Desktop/test.sh','w')
    file.write(curl_get_access)
    file.close()
    return tmpres

base64_string = jpg_2_base64("/Users/fat/Desktop/IMG_8122.jpeg")
# base64_string = 'debug'
base64_newpic = enhance_pic(base64_string)
# print('\n',base64_newpic)
# base64_2_jpg("/Users/fat/Desktop/IMG_8129_NEW.JPEG",base64_string)
