import requests # request img from web
import shutil # save img locally
import os

def save_image(url, path):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        #f_ext = os.path.splitext(url)[-1]
        f_name = str(url.split('/')[-1])
        with open(os.path.join(path, f_name), 'wb') as f:
            f.write(res.content)
        print('Image sucessfully Downloaded: ', path)
    else:
        print('Image Couldn\'t be retrieved')
