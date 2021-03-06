import requests
import os
import sys
import zipfile

def download_file(url):
    file_name = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        return file_name

    return False

def unzip(file_name):
    with zipfile.ZipFile( file_name ,'r') as f:
        f.extractall("./plugins/")

#example_url
url = 'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'
filename = download_file(url)
unzip(filename)
os.remove("./" + filename)