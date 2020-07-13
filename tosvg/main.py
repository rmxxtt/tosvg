from PIL import Image
import sys


if len(sys.argv) == 2:
    img_name = sys.argv[1]
    svg_name = img_name.split(".", 1)[0]
elif len(sys.argv) == 3:
    img_name = sys.argv[1]
    svg_name = sys.argv[2].split(".", 1)[0]
else:
    sys.exit(1)


img = Image.open(img_name)
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

with open(f"{svg_name}.svg", "w") as file:
    file.write(svg)

print(f"Готово {svg_name}.svg")
