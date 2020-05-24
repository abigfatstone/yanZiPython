import base64
import os

def get_base_home():
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    BASE_HOME = "/".join(FILE_PATH.split('/')[:-3])
    return BASE_HOME

def get_resouece_home():
    BASE_HOME =get_base_home()
    RESOURCE_DIR = os.path.join(BASE_HOME, 'resource')
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    return RESOURCE_DIR

def get_output_home():
    BASE_HOME =get_base_home()
    OUTPUT_DIR = os.path.join(BASE_HOME, 'output')
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    return OUTPUT_DIR

def get_checkbox_html(inputLine,inputType):
    lineHtml = ''
    for line in inputLine[0]:
       lineHtml = lineHtml + '<p>' + line + '</p>'
    for line in inputLine[1]:
       lineHtml = lineHtml + "<p><input type='" + inputType+ "' name='option' value='"+ line[1] +"'/>"+ line[0] + "</p>"
    lineHtml = lineHtml + "<p align='right'><a href='javascript:void(0)' class='button button-glow button-rounded button-raised button-primary' id='sendOption'> 提交</a></p>"
    return lineHtml

def get_table_html(inputLine,inputType):
    lineHtml = '<table>'
    for line in inputLine:
        fieldHtml =''
        for line_field in line:
            if not isinstance(line_field, str) :
                fieldHtml = fieldHtml + '<td width = \''+line_field[1] +'%\'> '+ line_field[0] + '</td>'
            else:
                fieldHtml = fieldHtml + '<td>' + line_field + '</td>'
        lineHtml = lineHtml + '<tr>' + fieldHtml + '</tr>'
    lineHtml = lineHtml + '</table> '
    return lineHtml

def format_html(input_list,client_type):
    if client_type == 'django':
        nLine = 0
        return_str = ''
        for line_char in input_list:
            if line_char == '\n':
                nLine += 1
                if nLine == 1:
                    return_str += '<p>'
                else:
                    return_str += '</p><p>'
            elif line_char == ' ':
                return_str += '&nbsp;'
            else:
                return_str += line_char
        return_str += '</p>'
    else:
        return_str = '<p>'
        for line_char in input_list:
            if line_char == '\n':
                return_str += '</p><p>'
            elif line_char == ' ':
                return_str += '&nbsp;'
            else:
                return_str += line_char
        return_str += '</p>'
    return return_str

def format_file(file_name,client_type):
    if client_type == 'django':
        file_url = 'http://yanzi.cloudoc.cn:8000/static/'
        return_str = "<a href=\"" + file_url + file_name + "\">点击查看文件</a>"
        answer_type = 'text'
    else:
        with open(file_name, 'rb') as f:
            encode_img = base64.b64encode(f.read())
            file_ext = file_name.split('/')[-1]
            return_str = 'data:image/{};base64,{}'.format(
                file_ext[1:], encode_img.decode())
            f.close()

        answer_type = 'image'
    return return_str,answer_type

def save_file(input_message):
    resouece_home = get_resouece_home()
    imgdata = base64.b64decode(input_message.split(';base64,')[1])
    file_type= input_message.split(';base64,')[0].split(":")[-1]
    if file_type == 'text/plain':
        file_ext = '.txt'
    else:
        file_ext = '.png'
    file_name = '1' + file_ext
    file_path = os.path.join(resouece_home, file_name)
    print(file_path)

    file = open(file_path, 'wb')
    file.write(imgdata)
    file.close()