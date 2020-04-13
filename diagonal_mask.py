from PIL import Image
import PIL.ImageDraw as ImageDraw

im = Image.open("cisco3560x.png")


im_a = Image.new("L", im.size, 0)
draw = ImageDraw.Draw(im_a)

x_start = im.size[1] * -1
x_end = 0


step = 100
renge_loop = round(im.size[0]/step)+im.size[1]


for i in range(renge_loop):
    point1 = ((x_start,0),(x_end,im.size[1]))
    draw.line(point1, fill=200, width=10)
    x_start += step
    x_end += step

im_a.show()

## https://note.nkmk.me/en/python-pillow-putalpha/