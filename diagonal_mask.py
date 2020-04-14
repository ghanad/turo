from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw
import ports


switch_image = Image.open("cisco3560x.png")


def spare_port(color):
    port_image = Image.new('RGB',(500,400),color)
    port_mask = ImageDraw.Draw(port_image)

    # make diagonal
    step = 100
    x_start = port_image.size[1] * -1
    x_end = 0
    renge_loop = round(port_image.size[0]/step)+port_image.size[1]

    for _ in range(renge_loop):
        point1 = ((x_start,port_image.size[1]),(x_end,0))
        port_mask.line(point1, fill='white', width=10)
        x_start += step
        x_end += step

    port_mask_spare = Image.new("L", port_image.size, 0)
    port_mask_temp = ImageDraw.Draw(port_mask_spare)
    port1 = ((0, 50), (0, 306), (407, 306), (407, 50), (282, 50), (282, 22), (246, 22), (246, 0), (160, 0), (160, 22), (124, 22), (124, 50))
    port_mask_temp.polygon(port1, fill=255)
    return port_image,port_mask_spare


switch_image.paste(spare_port(color='red')[0],(6785,330),spare_port(color='red')[1])

switch_image.show()
