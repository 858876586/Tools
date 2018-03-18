#coding=utf-8  
import requests  
url = "http://localhost"  
path = r'C:\Users\85887\Desktop\Project\Tools\HttpServer\test.txt'  

files = {'file': open(path, 'rb')}  
r = requests.post(url, files=files)  
print(r.url)  
print(r.text)  
