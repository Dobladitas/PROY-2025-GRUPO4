from utils.wifi.wifi_tools import scan_wifi, get_wifis
fileNames = [
    'key_c',
    'key_p',
    'none',
    'number_0',#3
    'number_1',#4
    'number_2',#5
    'number_3',#6
    'number_4',#7
    'number_5',#8
    'number_6',#9
    'number_7',#10
    'number_8',#11
    'number_9',#12
    'root',#13
    'lab',#14
    'pasillo',#15
    'pasillo_ascensor'#16
]

roomName = scan_wifi()
chars = list()
toPrint = list()


if roomName != None:
    chars = list(roomName)
    toPrint.append(fileNames[13])
    for char in chars:
        
        if char.lower() == "c":
            toPrint.append(fileNames[0])
        elif char.lower() == "p":
            toPrint.append(fileNames[1])
        elif char.isdigit():
            toPrint.append(fileNames[int(char)+3])
        else:
            toPrint.append(roomName)
            
            
        #print(char)
else:
    toPrint.append(fileNames[2])
    
    
print(toPrint)
