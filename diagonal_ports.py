from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports

step = 100

def diagonal(ports , photo_size):
    im = Image.new("L", photo_size, 0)
    draw = ImageDraw.Draw(im)

    x_start = photo_size[1] * -1
    x_end = 0

    # make port
    for portNum,color in ports:
        print(portNum)
        draw.polygon(ports.port_geo(portNum), fill=color)

    # make diagonal lines
    renge_loop = round(im.size[0]/step)+im.size[1]

    for _ in range(renge_loop):
        point1 = ((x_start,im.size[1]),(x_end,0))
        draw.line(point1, fill=200, width=10)
        x_start += step
        x_end += step

    # mask
    im_a = Image.new("L", im.size, 0)
    drawMask = ImageDraw.Draw(im_a)
    drawMask.polygon(ports.port_geo(1), fill=255)

    im.putalpha(im_a)

    return im


port1 = ((1,(255,255,0)),(2,(255,100,0)))

a = diagonal(port1,(1500,1500))
a.show()