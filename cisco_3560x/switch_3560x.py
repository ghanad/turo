from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports_3560x
from PIL import ImageFont
import vlan_colors
import port_string_png_maker
import switch_name
import os


def absPath(fileName):
    dirName = os.path.dirname(os.path.abspath(__file__))
    tempName1 = fileName
    return os.path.join(dirName, tempName1)

switch_image = Image.open(absPath('cisco3560x.png'))

# read port list file
with open(absPath('sw1.csv'), newline='') as ff:
    f1 = ff.readlines()
    switch_port_list = [x.rstrip() for x in f1[1:]]

switchName = f1[0].rstrip()

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
sImageW,sImageH = switch_image.size
sPortH = 600
strpic = port_string_png_maker.stringpic(switch_port_list,(sImageW,sPortH),300)

# swithc Name 
sNameW = 1400
sNameFontSize = 430
switchName = switch_name.sNamePic(switchName,(sNameW,sImageH),sNameFontSize)

# create background 
bg = Image.new('RGB',(sImageW+sNameW,sImageH+sPortH),'white')
bg_draw = ImageDraw.Draw(bg)


bg.paste(switch_image,(sNameW,0))
bg.paste(strpic,(sNameW,sImageH+300))
bg.paste(switchName,(0,0))
bg.show()
