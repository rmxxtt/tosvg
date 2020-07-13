from PIL import Image
import os
import re
from datetime import datetime


print("-- Все файлы типа png будут конвертированы в svg")
imgs_folder = input("Путь до папки: ").rstrip("\\/")
print("-- Необязательный параметр, название папки для файлов svg")
print("-- По дефолту название папки текущее время. Можно использовать путь")
save_folder = input("Название папки: ").strip(" ")
if not save_folder:
    save_folder = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

try:
    os.makedirs(save_folder)
except FileExistsError:
    pass

files = os.listdir(imgs_folder)
imgs = [x for x in files if re.match(".*.png", x)]


for img_name in imgs:
    img = Image.open(f"{imgs_folder}/{img_name}")
    width, height = img.size
    img_data = list(img.getdata())
    img_data = list(zip(*[iter(img_data)] * width))

    svg_path = '<path fill="{color}" d="{d}"/>'
    pixels = []

    for y in range(height):
        for x in range(width):
            d = f"M{x} {y}h1v1H{x}z"
            color = "#{:02x}{:02x}{:02x}{:02x}".format(*img_data[y][x])
            rect = svg_path.format(color=color, d=d)
            pixels.append(rect)

    svg_size = f'viewBox="0 0 {width} {height}" widht="{width}" height="{height}"'
    svg_style = 'style="shape-rendering:optimizeSpeed"'
    svg_xmlns = 'xmlns="http://www.w3.org/2000/svg"'
    svg_pahts = "".join(str(x) for x in pixels)

    svg = f'<svg {svg_xmlns} {svg_size} {svg_style}>{svg_pahts}</svg>'

    with open(f'{save_folder}/{img_name.split(".", 1)[0]}.svg', "w") as file:
        file.write(svg)

print(f"Готово")
