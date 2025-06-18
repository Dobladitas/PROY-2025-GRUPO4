#Script para probar la logica del proyecto final
#Script creado para propositos de prueba, mientras buscamos otro par de audifonos.

from machine import Pin
import time

# Configurar el botón en GP15, usando pull-down interno
boton = Pin(13, Pin.IN, Pin.PULL_DOWN)
detectandoSala = False
botonPresionado = 0


while True:
    
    if detectandoSala == True:
        print('Ahora mismo, estariamos buscando la sala mas cercana')
        time.sleep(1)
        print('Ahora, suena el audio basado en que sala del edificio P esta el usuario')
        time.sleep(0.5)
        detectandoSala = False
        time.sleep(1)
        
        
        
    print(f'El buzzer suena en base a la distancia del ultrasonido aqui')
    
    if botonPresionado > 0:
        botonPresionado = botonPresionado - 0.1
        
    if botonPresionado < 0:
        botonPresionado = 0
        
        
    if boton.value() == False and botonPresionado == 0:
        detectandoSala = True
        botonPresionado = 1.5
        print("Botón presionado")
    
    time.sleep(0.1)

