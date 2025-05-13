from utils.wifi.wifi_tools import scan_wifi, get_wifis
import time

#get_wifis(False) #debug :3

timeschecked = 0
for number in range(10):
    
    timeschecked = 0
    while scan_wifi() == False:
        if timeschecked >= 5:
            print('No se lograron detectar puntos de acceso cercanos')
            break
        
        time.sleep(.5)
        timeschecked+1


