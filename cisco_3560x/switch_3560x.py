from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports_3560x
from PIL import ImageFont
import vlan_colors
import port_string_png_maker


switch_image = Image.open("cisco3560x.png")

# read port list file
with open('sw1.csv', newline='') as ff:
    f1 = ff.readlines()
    switch_port_list = [x.rstrip() for x in f1]

# seprate access and trunk ports
trunk_port_list = [x for x in switch_port_list if x.split(',')[1].lower() == 'trunk' ]
access_port_list = [x for x in switch_port_list if x.split(',')[1].lower() != 'trunk' ]

for i in access_port_list:
    portNum = int(i.split(',')[0])
    color1 = str(i.split(',')[1].upper())
    spare_status = str(i.split(',')[2])
    if spare_status in ["spare", 1]:
        spare_result = True
    else:
        spare_result = False
    port1 = ports_3560x.Port(portNum, vlan_colors.vlanDict[color1] ,spare=spare_result)
    port_temp = port1.portShape()
    switch_image.paste(port_temp[0], port1.geo, port_temp[1])

for i in trunk_port_list:
    port1 = ports_3560x.Trunk(i.split(',')[0])
    port_temp = port1.portShape()
    switch_image.paste(port_temp[0], port1.geo, port_temp[1])

# port list text
w,h = switch_image.size
strpic = port_string_png_maker.stringpic(switch_port_list,(w,400),300)

bg = Image.new('RGB',(w,h+600),'white')
bg_draw = ImageDraw.Draw(bg)

bg.paste(switch_image,(0,0))
bg.paste(strpic,(0,h+300))
bg.show()
