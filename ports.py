
def port_geo(port):
    LPO = 454
    port1 = ((6785,380),(6785,636),(7192,636),(7192,380),(7067,380),(7067,352),(7031,352),(7031,330),(6945,330),(6945,352),(6909,352),(6909,380))

    if port == 1: 
        return port1
    if port == 3 or port == 5 or port == 7 or port == 9 or port == 11:
        RPO = 0
    if port == 13 or port == 15 or port == 17 or port == 19 or port == 21 or port == 23:
        RPO = 157

    port_temp = list(port1)
    port_new_temp = list()
    for i in port_temp:
        a = list(i)
        a[0] = a[0]+ (LPO*(((port - 1))/2)) + RPO
        i = tuple(a)
        port_new_temp.append(i)
    return tuple(port_new_temp)




