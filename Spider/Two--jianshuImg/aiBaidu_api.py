from aip import AipFace
import base64

APP_ID = '11660967'
API_KEY = '8PFSscW1pXWOX3q8b38ps5hN'
SECRET_KEY = 'pnfzRclmzmTqbxOW7KjL6hMFwNfXoTk3 '

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath = r'8.jpg'
def get_file_content(filePath):
 with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
 return content.decode('utf-8')

imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,beauty"

result = aipFace.detect(get_file_content(filePath),imageType,options)
# print(result['result']['face_list'][0]['age'])
print(result['result']['face_list'][0]['beauty'])
print(result)