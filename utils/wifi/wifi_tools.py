#importando librerias
import network
import time
import json


def get_real_name(mac):
    # Load the JSON file into a dictionary
    with open('utils/wifi/names.json', 'r') as file:
        name_lookup = json.load(file)
    real_name = name_lookup.get(mac)
    
    if real_name:
        return real_name
    else:
        return mac
    

def format_mac(mac_bytes): #convirtiendo el nombre de la mac
    return ':'.join(f'{b:02X}' for b in mac_bytes)

#declarando la funcion
def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    networks = wlan.scan()
    print("Escaneando redes Wi-Fi...")
    time.sleep(.5)

    
    try:
        networks = wlan.scan()
        networks = wlan.scan()
        networks = wlan.scan()
        if not networks:
            print("No se encontraron redes Wi-Fi.")
            return False

        # Ordenar por RSSI (intensidad de señal), de mas fuerte a mas debil. 
        networks.sort(key=lambda net: net[3]*99, reverse=True)

        result = []
        for i, net in enumerate(networks, start=1):
            ssid = net[0].decode('utf-8')
            rssi = net[3]
            mac = format_mac(net[1])
            
            if ssid == "eduroam" :
                if 'CIAC' in get_real_name(mac):                
                    print(f'Probablemente estes en el {get_real_name(mac)}')
                else:
                    print(f'Probablemente estes en la sala {get_real_name(mac)}')
                #print(mac)
                #print(f"{i}. SSID: {ssid} | Signal Strength: {rssi} dBm |", get_real_name(mac))
                #print(get_real_name(mac))
                result.append((ssid, rssi))
                return True
        
        return False
    
    except Exception as e:
        
        networks = wlan.scan()
        if not networks:
            print("No se encontraron redes Wi-Fi.")
            return True
        
        print(f"Ha ocurrido un error de tipo: {e}")
        return True
    
    
#debug
def get_wifis(only_eduroams):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Escaneando redes Wi-Fi...\n")
    time.sleep(.1)

    
    try:
        networks = wlan.scan()
        if not networks:
            print("No se encontraron redes Wi-Fi.")
            return

        # Ordenar por RSSI (intensidad de señal), de mas fuerte a mas debil. 
        networks.sort(key=lambda net: net[3], reverse=True)

        result = []
        for i, net in enumerate(networks, start=1):
            ssid = net[0].decode('utf-8')
            rssi = net[3]
            mac = format_mac(net[1])
            
            if (only_eduroams == True and ssid == 'eduroam') or only_eduroams ==False :
                print(f'Punto de acceso encontrado: {get_real_name(mac)}, con intensidad: {rssi}, de nombre {ssid}')
        
    
    except Exception as e:
        
        networks = wlan.scan()
        if not networks:
            print("No se encontraron redes Wi-Fi.")
            return True
        
        print(f"Ha ocurrido un error de tipo: {e}")
        return True
    
    
