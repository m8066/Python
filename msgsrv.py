
import requests
import subprocess

url=''
local_filename = url.split('/')[-1]

r = requests.get(url)

#print r.content

#subprocess.Popen([r.content],shell=True)

with open(local_filename, "wb") as pdf_f:
   ''' for chunk in r.iter_content(1024): 
            if chunk: # filter out keep-alive new chunks'''
   pdf_f.write(r.content)


