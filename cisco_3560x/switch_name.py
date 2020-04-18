from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
from PIL import ImageFont
import os

def absPath(fileName):
    dirName = os.path.dirname(os.path.abspath(__file__))
    tempName1 = fileName
    return os.path.join(dirName, tempName1)


def sNamePic(sName, picSize, fontSize):
    sNameP1 = sName.split('-')[0]
    sNameP2 = sName.split('-')[1]

    sNameT = '  {}\n{}'.format(sNameP1,sNameP2)
    _,h = picSize
    hP1 = round((h/2) - h*0.17)

    text_bg = Image.new('RGB',picSize,'white')
    text_mask = ImageDraw.Draw(text_bg)
    font = ImageFont.truetype(absPath('calibri.ttf'), fontSize)
    text_mask.text((10, hP1), sNameT, (0, 0, 0),font=font)
    return text_bg