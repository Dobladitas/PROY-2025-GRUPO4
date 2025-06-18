from utils.wifi.wifi_tools import scan_wifi, get_wifis 
from machine import Pin, PWM
import time


#Importando pines
trigger_pin = Pin(0, Pin.OUT)
echo_pin = Pin(15, Pin.IN)
buzzer = PWM(Pin(16))

#declarando variables
final, inicio = 0,0
TIMEOUT_US = 30000  # 30ms timeout para el regreso del eco

#configurando el buzzer
buzzer.freq(440)
buzzer.duty_u16(0)

#funcion para ajustar el beep del buzzer
def buzzer_beep(distance):
    #buzzer.freq(440 + int(magic_number) * 300) #scrapped
    
    #tanto el tono como el volumen aumenta a medida que la distancia disminuye
    buzzer.duty_u16(30000)
    time.sleep((distance/100)/2)
    buzzer.duty_u16(0)
    time.sleep((distance/100)/2)

#bucle principal
while True:
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()
    start_time = time.ticks_us()

    #Esperando a que el echo_pin aumente
    while echo_pin.value() == 0:
        if time.ticks_diff(time.ticks_us(), start_time) > TIMEOUT_US:
            print("Timeout: No echo received (start)")
            distancia = None
            break
    else:
        inicio = time.ticks_us()
        
        #Revisando que la señal no se haya perdido
        while echo_pin.value() == 1:
            if time.ticks_diff(time.ticks_us(), inicio) > TIMEOUT_US:
                print("Timeout: No echo received (end)")
                distancia = None
                break
        else:
            final = time.ticks_us()
            distancia = (final - inicio) / 58  #Conversion a [cm]
    
    if distancia is not None and distancia < 125: #si esta condicion es verdadera hacemos sonar el buzzer
        print("Distancia: " + str(int(distancia)) + " Cm")
        buzzer_beep(distancia)
        
    else:
        buzzer.duty_u16(0)  #Apagando el buzzer

    time.sleep_ms(1)
    
    
buzzer.duty_u16(0)


