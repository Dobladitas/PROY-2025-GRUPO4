#Este script debe apagar todos los componentes del proyecto.
from machine import Pin, PWM

#Configurando pines
trigger_pin = Pin(0, Pin.OUT)
echo_pin = Pin(15, Pin.IN)
buzzer = PWM(Pin(16))

buzzer.duty_u16(0)

print('Se ha apagado el sistema correctamente')



