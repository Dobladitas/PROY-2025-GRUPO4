from machine import Pin
import time


boton = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    if boton.value() == False:
        print("Botón presionado")
    else:
        print("Esperando botón...")
    time.sleep(0.2)

