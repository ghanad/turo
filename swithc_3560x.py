from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports_3560x

switch_image = Image.open("cisco3560x.png")

#port 1
port1 = ports_3560x.Port(24,'red',True)
port_temp = port1.portShape()
switch_image.paste(port_temp[0], port1.geo, port_temp[1])

#port 13
port13 = ports_3560x.Port(13,'blue',True)
port_temp = port13.portShape()
switch_image.paste(port_temp[0], port13.geo, port_temp[1])

switch_image.show()
