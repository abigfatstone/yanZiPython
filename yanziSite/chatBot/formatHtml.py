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

def format_html(input_list):
    nLine = 0
    return_str = ''
    line_list = input_list.split(':')
    if line_list[0] == '文件地址':
        file_name = line_list[1].split('/')[-1]
        file_url = 'http://yanzi.cloudoc.cn:8000/static/'
        return_str = "<a href=\"" + file_url + file_name + "\">点击查看文件</a>"
    else:
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
    return return_str