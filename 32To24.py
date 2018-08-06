import os
from PIL import Image


imageList = os.listdir('./')

for n in imageList:
    p = os.path.splitext(n)
    if p[1] == '.bmp':
        print(n)
        img = Image.open(n)
        imgrgb = img.convert('RGB')
        imgrgb.save(n)
print('保存完毕')
os.system("pause")
