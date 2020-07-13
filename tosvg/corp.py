from PIL import Image
from os import mkdir


img_name = input("Исходный файл: ")
print("-- Значения в px")
user_width = int(input("Ширина среза (x): "))
user_height = int(input("Высота среза (y): "))

save_folder = img_name.split(".", 1)[0]
mkdir(save_folder)

img = Image.open(img_name)
width, height = img.size

for y in range(height // user_height):
    for x in range(width // user_width):
        x1 = x * user_width
        y1 = y * user_height
        x2 = x1 + user_width
        y2 = y1 + user_height
        im_crop_outside = img.crop((x1, y1, x2, y2))
        im_crop_outside.save(f"./{save_folder}/outside_{x1}_{y1}.png")

print("Готово")