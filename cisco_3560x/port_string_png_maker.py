from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# create dictionary and seprate ports base vlan 
def dictMaker(list1):
    trunk_dict = dict()
    for i in list1:
        portNumber = i.split(',')[0]
        vlanName = i.split(',')[1].upper()
        if vlanName not in trunk_dict.keys():
            trunk_dict[vlanName] = [int(portNumber)]
        else:
            trunk_dict[vlanName].append(int(portNumber))
    return trunk_dict

def stringMaker(dict1):
    final_string = ''
    for x,y in dict1.items():
        res_string = listAbr(y)
        res_count = len(y)
        res = '{}:[{}][{}]       '.format(x.upper(),res_count, res_string)
        final_string = final_string + res
        return final_string

def listAbr(list1,st1=''):
    for i in range(len(list1)):
        start = list1[0]
        try:
            end = list1[i+1]
        except:
            if list1[i] - list1[i-1] != 1:
                result = '{},{}'.format(st1, list1[i])
            else:
                result = '{},{}-{}'.format(st1,start, list1[i])
            return result.lstrip(',')
        
        if  list1[i+1] - list1[i] == 1:
            end = list1[i+1]
            string1 = '{},{}-{}'.format(st1,start, end)
        elif list1[i+1] - list1[i] != 1 and list1[i] - list1[i-1] != 1:
            string1 = '{},{}'.format(st1,list1[i])
            break
        else:
            break
    return listAbr(list1[list1.index(list1[i+1]):],string1)

def stringpic(list2, picsize, fontSize):
    # seprate access and trunk ports
    trunk_port_list = [x for x in list2 if x.split(',')[1].lower() == 'trunk' ]
    access_port_list = [x for x in list2 if x.split(',')[1].lower() != 'trunk' and x.split(',')[1] != '' ]
    # print(dictMaker(access_port_list))
    fstring = stringMaker(dictMaker(access_port_list)) + stringMaker(dictMaker(trunk_port_list)) 
    
    # print(dictMaker(access_port_list))
    text_bg = Image.new('RGB',picsize,'white')
    text_mask = ImageDraw.Draw(text_bg)
    font = ImageFont.truetype('calibri.ttf', fontSize)
    text_mask.text((800, 0), fstring, (0, 0, 0),font=font)
    return text_bg