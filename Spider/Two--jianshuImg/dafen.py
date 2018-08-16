from aip import AipFace
import base64
import os
import time

APP_ID = '11660967'
API_KEY = '8PFSscW1pXWOX3q8b38ps5hN'
SECRET_KEY = 'pnfzRclmzmTqbxOW7KjL6hMFwNfXoTk3'

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
 with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
 return content.decode('utf-8')

imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,beauty"

file_path = 'Photo'
file_lists = os.listdir(file_path)
for file_list in file_lists:
    result = aipFace.detect(get_file_content(os.path.join(file_path,file_list)),imageType,options)
    error_code = result['error_code']
    if error_code == 222202:
        continue

    try:
        sex_type = result['result']['face_list'][-1]['gender']['type']
        if sex_type == 'male':
            continue
     #     print(result)
        beauty = result['result']['face_list'][-1]['beauty']
        new_beauty = round(beauty/10,1)
        print(file_list,new_beauty)
        if new_beauty >= 8:
            os.rename(os.path.join(file_path,file_list),os.path.join('8分',str(new_beauty) + '+' + file_list))
        elif new_beauty >= 7:
            os.rename(os.path.join(file_path,file_list),os.path.join('7分',str(new_beauty) + '+' + file_list))
        elif new_beauty >= 6:
            os.rename(os.path.join(file_path,file_list),os.path.join('6分',str(new_beauty) + '+' + file_list))
        elif new_beauty >= 5:
            os.rename(os.path.join(file_path,file_list),os.path.join('5分',str(new_beauty) + '+' + file_list))
        else:
            os.rename(os.path.join(file_path,file_list),os.path.join('其他分',str(new_beauty) + '+' + file_list))
            time.sleep(1)
    except KeyError:
        pass
    except TypeError:
        pass