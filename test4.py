from PIL import Image
import PIL.ImageDraw as ImageDraw

offset1 = 60
offset2 = offset1 * 2
offset3 = offset1 * 3
offset4 = offset1 * 4
offset5 = offset1 * 5
offset6 = offset1 * 6

im = Image.open("cisco3560x.png")
pixels = im.load()

port1 = ((6785,380),(6785,636),(7192,636),(7192,380),(7067,380),(7067,352),(7031,352),(7031,330),(6945,330),(6945,352),(6909,352),(6909,380))

draw = ImageDraw.Draw(im)
nodes1 = ((port1[2][0]-offset1,port1[2][1]-2),(port1[2][0],port1[2][1]-offset1))
nodes2 = ((port1[2][0]-offset2,port1[2][1]-2),(port1[2][0],port1[2][1]-offset2))
nodes3 = ((port1[2][0]-offset3,port1[2][1]-2),(port1[2][0],port1[2][1]-offset3))
nodes4 = ((port1[2][0]-offset4,port1[2][1]-2),(port1[2][0],port1[2][1]-offset4))
nodes5 = ((port1[2][0]-offset5,port1[2][1]-2),(port1[2][0]-40,port1[0][1]))
nodes6 = ((port1[2][0]-offset6,port1[2][1]-2),(port1[2][0]-100,port1[0][1]))
nodes7 = ((port1[1][0],port1[1][1]-13),(port1[5][0],port1[5][1]+2))
nodes8 = ((port1[1][0],port1[1][1]-73),(port1[7][0],port1[7][1]+2))
nodes9 = ((port1[1][0],port1[1][1]-133),(port1[9][0],port1[9][1]+2))
nodes10 = ((port1[1][0],port1[1][1]-193),(port1[11][0]-50,port1[11][1]+2))
# draw.polygon((port_geo(23)), fill=200)

draw.line(nodes1, fill=200, width=10)
draw.line(nodes2, fill=200, width=10)
draw.line(nodes3, fill=200, width=10)
draw.line(nodes4, fill=200, width=10)
draw.line(nodes5, fill=200, width=10)
draw.line(nodes6, fill=200, width=10)
draw.line(nodes7, fill=200, width=10)
draw.line(nodes8, fill=200, width=10)
draw.line(nodes9, fill=200, width=10)
draw.line(nodes10, fill=200, width=10)
# paintPort(port=port24)


im.show("cisco3560x1.png")
# im.save("cisco3560x1.png")