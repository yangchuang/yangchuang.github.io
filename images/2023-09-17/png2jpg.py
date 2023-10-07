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
    folder_path = "/Users/yang/projects/FE/yangchuang.github.io/images/2023-09-17"
    convert_all_png_to_jpg(folder_path)