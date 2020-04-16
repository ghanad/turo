from PIL import Image, ImageOps
import PIL.ImageDraw as ImageDraw

class Port:
    def __init__(self, number, color, spare):
        self.number = number
        self.color = color
        self.spare = spare
        self.geo = tuple()

    def portShape(self):
        self.port_geo()
        port_image = Image.new('RGB',(500,400),self.color)
        port_mask = ImageDraw.Draw(port_image)

        # make diagonal
        step = 100
        x_start = port_image.size[1] * -1
        x_end = 0
        renge_loop = round(port_image.size[0]/step)+port_image.size[1]

        if self.spare == True:
            for _ in range(renge_loop):
                point1 = ((x_start,port_image.size[1]),(x_end,0))
                port_mask.line(point1, fill='white', width=10)
                x_start += step
                x_end += step

        port_mask_spare = Image.new("L", port_image.size, 0)
        port_mask_temp = ImageDraw.Draw(port_mask_spare)
        if self.number in range(1,25,2):
            port1 = ((0, 50), (0, 306), (407, 306), (407, 50), (282, 50), (282, 22), (246, 22), (246, 0), (160, 0), (160, 22), (124, 22), (124, 50))
        if self.number in range(2,26,2):
            port1 = ((0, 14), (407, 14), (407, 268), (282, 268), (282, 295), (244, 295), (244, 318), (160, 318), (160, 295), (126, 295), (126, 268), (0, 268))
        port_mask_temp.polygon(port1, fill=255)
        return port_image,port_mask_spare

    def port_geo(self):
        offset = 0
        LPO = 454
        RPO = 0
        if self.number in [1,3,5,7,9,11]:
            RPO = 0
            offset =int(LPO*((self.number - 1)/2) + RPO)
            self.geo = (6785 + offset,330)
        if self.number in [13,15,17,19,21,23]:
            RPO = 157
            offset =int(LPO*((self.number - 1)/2) + RPO)
            self.geo = (6785 + offset,330)

        if self.number in [2,4,6,8,10,12]:
            RPO = 0
            offset =int(LPO*((self.number - 2)/2) + RPO)
            self.geo = (6785 + offset,794-14)
        
        if self.number in [14,16,18,20,22,24]:
            RPO = 157
            offset =int(LPO*((self.number - 2)/2) + RPO)
            self.geo = (6785 + offset,794-14)

class Trunk(Port):
    def __init__(self,number):
        self.number = number
        self.color = "blue"
        self.geo = tuple()

    def portShape(self):
        self.port_geo()
        port_image = Image.new('RGB',(500,400),self.color)
        port_mask = ImageDraw.Draw(port_image)

        # make diagonal
        step = 60
        step_temp = 50
        renge_loop = round(port_image.size[0]/step)+port_image.size[1]

        for _ in range(renge_loop):
            point1 = ((0,step_temp),(port_image.size[0],step_temp))
            port_mask.line(point1, fill='black', width=10)
            step_temp += step

        port_mask_spare = Image.new("L", port_image.size, 0)
        port_mask_temp = ImageDraw.Draw(port_mask_spare)
        
            
        if int(self.number) in range(1,25,2):
            port1 = ((0, 50), (0, 306), (407, 306), (407, 50), (282, 50), (282, 22), (246, 22), (246, 0), (160, 0), (160, 22), (124, 22), (124, 50))
        if int(self.number) in range(2,26,2):
            port1 = ((0, 14), (407, 14), (407, 268), (282, 268), (282, 295), (244, 295), (244, 318), (160, 318), (160, 295), (126, 295), (126, 268), (0, 268))
        if int(self.number) in [25,26,27,28]:
            port1 = ((0,0),(0,300),(450,300),(450,0))

        port_mask_temp.polygon(port1, fill=255)
        return port_image,port_mask_spare

    def port_geo(self):
        if self.number.isnumeric():
            offset = 0
            LPO = 454
            RPO = 0
            temp_number = int(self.number)
            if temp_number in [1,3,5,7,9,11]:
                RPO = 0
                offset =int(LPO*((temp_number - 1)/2) + RPO)
                self.geo = (6785 + offset,330)
            if temp_number in [13,15,17,19,21,23]:
                RPO = 157
                offset =int(LPO*((temp_number - 1)/2) + RPO)
                self.geo = (6785 + offset,330)

            if temp_number in [2,4,6,8,10,12]:
                RPO = 0
                offset =int(LPO*((temp_number - 2)/2) + RPO)
                self.geo = (6785 + offset,794-14)
            
            if temp_number in [14,16,18,20,22,24]:
                RPO = 157
                offset =int(LPO*((temp_number - 2)/2) + RPO)
                self.geo = (6785 + offset,794-14)
            if temp_number == 25:
                self.geo = (12820,863)
            if temp_number == 26:
                self.geo = (12820+465,863)
            if temp_number == 27:
                self.geo = (12820+930,863)
            if temp_number == 28:
                self.geo = (12820+1395,863)
        else:
            if self.number.lower() in ["gi0/1", "gi1/0/1"]:
                self.geo = (12820,863)
            if self.number.lower() in ["gi0/2", "gi1/0/2"]:
                self.geo = (12820+465,863)
            if self.number.lower() in ["gi0/3", "gi1/0/3"]:
                self.geo = (12820+930,863)
            if self.number.lower() in ["gi0/4", "gi1/0/4"]:
                self.geo = (12820+1395,863)