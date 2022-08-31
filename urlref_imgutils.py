from typing import final
import requests # request img from web
import shutil # save img locally
import os

def save_image(url, path):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        #f_ext = os.path.splitext(url)[-1]
        f_name = str(url.split('/')[-1])
        final_path = os.path.join(path, f_name)
        with open(final_path, 'wb') as f:
            f.write(res.content)
        print('Image sucessfully downloaded: ', path)
        return True, final_path
    else:
        print('Image couldn\'t be retrieved')
        return False