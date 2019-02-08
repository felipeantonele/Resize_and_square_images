from PIL import Image
import csv
from io import BytesIO
import time
import requests
import urllib.request


def resize(link_image,link_save):
    # link_image = str('14405925_2.jpg')
    # link_save = str('teste.jpg')
    # image = Image.open(link_image)
    req = requests.get(link_image)
    image = Image.open(BytesIO(req.content))
    size_x = image.size[0]
    size_y = image.size[1]
    size_square = int(2000)
    if size_x <= size_square and size_y <= size_square:
        if size_x < size_y:
            size_square = size_y
        else:
            size_square = size_x
    if size_y / size_x >= 1:
        new_size_x = int((size_square * size_x) / size_y)
        new_size_y = int(size_square)
        x_0 = int((size_square - new_size_x) / 2)
        y_0 = int(0)
    else:
        new_size_x = int(size_square)
        new_size_y = int((size_square * size_y) / size_x)
        x_0 = int(0)
        y_0 = int((size_square - new_size_y) / 2)

    size = new_size_x, new_size_y
    image.thumbnail(size)
    background = Image.new('RGB', (size_square, size_square), (255, 255, 255))
    background.paste(image, (x_0, y_0))
    background.save(link_save)


link_csv = str(r'Lista_link.csv')
try:
    with open(link_csv, 'r', encoding='utf-8', errors='ignore') as lb:
        reader = csv.reader(lb)
        i = 0
        for r in reader:
            link_image = r[0]
            link_save = str('imagens') + '\\' + r[1]
            resize(link_image, link_save)
            i += 1
            print('Realizado: ' + str(i))
except:
    print('Fudeu')
