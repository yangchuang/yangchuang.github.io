---
layout: post
title: Python工具脚本
date: 2023-10-07 20:24:00
feature: https://static.ericsky.com/images/2023-09-17/IMG_8425.jpg
summary: 好记性不如烂笔头，将平时用到的一些python工具脚本存档
categories: Python
---

**1. [<u>PNG格式图片转成JPEG格式</u>](#jump_1)**  

**2. [<u>批量改文件名</u>](#jump_2)**  

<a id="jump_1"></a>
### 1. PNG格式图片转成JPEG格式
```
# png3jpg.py

import os
from PIL import Image

def png_to_jpg(png_path, jpg_path):
    img = Image.open(png_path)
    rgb_img = img.convert('RGB')
    rgb_img.save(jpg_path)

def convert_all_png_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            png_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename[:-4] + '.jpg')
            png_to_jpg(png_path, jpg_path)

if __name__ == '__main__':
    # 指定文件夹路径
    folder_path = "/path/to/your/directory"
    convert_all_png_to_jpg(folder_path)
```

若遇到`ModuleNotFoundError: No module named 'PIL'`  报错，可以卸载pillow后重新安装
```
pip uninstall pillow
python3 -m pip install pillow
```

<a id="jump_2"></a>
### 2. 批量改文件名
```
#将某文件夹下的文件名中的空格替换成下划线_
import os

def replace_spaces_with_underscore(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # 获取文件的绝对路径
            file_path = os.path.join(root, file_name)
            # 替换文件名中的空格为下划线
            new_file_name = file_name.replace(" ", "_")
            new_file_path = os.path.join(root, new_file_name)
            # 修改文件名
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    # 指定文件夹路径
    folder_path = "/path/to/your/directory"
    replace_spaces_with_underscore(folder_path)
```