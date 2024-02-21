# remove the current file
import os
import shutil
if os.path.exists(".\ISCXURL2016.zip"):
    os.remove(".\ISCXURL2016.zip")
if os.path.exists(".\ISCXURL2016"):
    shutil.rmtree(".\ISCXURL2016")
#  download a file from the web using requests
import requests
url = 'http://205.174.165.80/CICDataset/ISCX-URL-2016/Dataset/ISCXURL2016.zip'
r = requests.get( url , allow_redirects=True ) 
open('ISCXURL2016.zip','wb').write(r.content)
from zipfile import ZipFile
with ZipFile('ISCXURL2016.zip', 'r') as zipObj:
    # Extract all the contents of zip file in different directory
    zipObj.extractall('ISCXURL2016')
    # print('File is unzipped in dataset folder')