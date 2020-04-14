from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports


switch_image = Image.open("cisco3560x.png")


port_image = Image.new('RGB',switch_image.size,(255,255,0))
port_mask = ImageDraw.Draw(port_image)


# make diagonal
step = 100
x_start = port_image.size[1] * -1
x_end = 0
renge_loop = round(port_image.size[0]/step)+port_image.size[1]

for i in range(renge_loop):
    point1 = ((x_start,port_image.size[1]),(x_end,0))
    port_mask.line(point1, fill=200, width=10)
    x_start += step
    x_end += step

port_mask_spare = Image.new("L", port_image.size, 0)
port_mask_temp = ImageDraw.Draw(port_mask_spare)
port_mask_temp.polygon(ports.port_geo(1), fill=255)

# im.show()
switch_image.paste(port_image,(0,0),port_mask_spare)

switch_image.show()
