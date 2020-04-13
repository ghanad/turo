from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports

step = 100

im = Image.open("cisco3560x.png")
im_original = im.copy()

draw = ImageDraw.Draw(im)

x_start = im.size[1] * -1
x_end = 0

# make port
draw.polygon(ports.port_geo(1), fill=(255,255,0))


# make diagonal
renge_loop = round(im.size[0]/step)+im.size[1]

for i in range(renge_loop):
    point1 = ((x_start,im.size[1]),(x_end,0))
    draw.line(point1, fill=200, width=10)
    x_start += step
    x_end += step


im_a = Image.new("L", im.size, 0)
drawMask = ImageDraw.Draw(im_a)
drawMask.polygon(ports.port_geo(1), fill=255)

im2 = im.copy()
im2.putalpha(im_a)

# im2.show()

mask = Image.new("L", im.size, 128)

im3 = Image.composite(im_original, im2, mask)
im.show()

## https://note.nkmk.me/en/python-pillow-putalpha/