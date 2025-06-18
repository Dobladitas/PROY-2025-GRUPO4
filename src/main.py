#IMPORTANDO FUNCIONES
from utils.wifi.wifi_tools import scan_wifi, get_wifis
from machine import Pin, PWM
import ustruct
import time
import os

#NOMBRES DE ARCHIVOS DE AUDIO
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

#SALIDA AUDIO (AUDIFONOS)
audio = PWM(Pin(1))
audio.freq(8000)  #8kHz y PWM como GPIO 1
audio.duty_u16(0)


#CONFIGURACIONES ESPECIFICAS DE LOS PINES
boton = Pin(13, Pin.IN, Pin.PULL_DOWN)

#ULTRA-SONIDO
trigger_pin = Pin(0, Pin.OUT)
echo_pin = Pin(15, Pin.IN)
buzzer = PWM(Pin(16))

#VARIABLES ULTRA-SONIDO
final, inicio = 0,0
TIMEOUT_US = 30000  #30ms TIMEOUT PARA EL REGRESO DEL ECO

#CONFIGURANDO EL BUZZER
buzzer.freq(440)
buzzer.duty_u16(0)

#OTRAS VARIABLES    
detectando_sala = False
boton_presionado = 0


#FUNCION PARA AJUSTAR EL BEEP DEL BUZZER
def buzzer_beep(distance):
    buzzer.duty_u16(30000)
    time.sleep((distance/100)/4)
    buzzer.duty_u16(0)
    time.sleep((distance/100)/4)
    
def detectar_sala_cercana():
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
                toPrint.append(fileNames[2])
                
    else:
        toPrint.append(fileNames[2])
    
    return(toPrint)
        
import time
import ustruct
import os
from machine import Pin, PWM

# PWM en GPIO 1
audio = PWM(Pin(1))
audio.freq(8000)

def play_wav(filename):
    print('attempting to play: '+filename)
    if filename == 'audio/number_0.wav':
        filename = 'audio/0.wav'
    try:
        with open(filename, "rb") as f:
            header = f.read(44)  # Salta el encabezado WAV (asumido estándar)

            file_size = os.stat(filename)[6]
            data_size = file_size - 44
            duration_seconds = data_size / 8000  # si es 8 kHz

            while True:
                data = f.read(1024)
                if not data:
                    break

                for b in data:
                    # Esto asume audio 8-bit unsigned PCM
                    sample = ustruct.unpack("B", bytes([b]))[0]
                    duty = int(sample / 255 * 65535)
                    audio.duty_u16(int(duty/10))
                    time.sleep_us(40)

            audio.duty_u16(0)  # Apagar después de terminar
        time.sleep(duration_seconds - 40 * 1_000_000)

    except Exception as e:
        print("Error playing file:", e)

        
while True:
    
    #EL CODIGO QUE SE EJECUTA CUANDO ESTAMOS DETECTANDO UNA SALA
    if detectando_sala == True:    
        buzzer.duty_u16(0)
        trigger_pin.off()
        lista_salas = detectar_sala_cercana()
        
        print('Ahora mismo, estariamos buscando la sala mas cercana' )
        time.sleep(0.1)
        
        for i in range(len(lista_salas)):
            name = 'audio/'+str(lista_salas[i])+'.wav'
            play_wav(name)
            
        time.sleep(0.01)
        detectando_sala = False
        boton_presionado = 2
        time.sleep(0.01)
        
        
    
    trigger_pin.on()
    time.sleep_us(1)
    trigger_pin.off()
    start_time = time.ticks_us()

    #ESPERANDO A QUE EL ECHO_PIN AUMENTE
    while echo_pin.value() == 0:
        if time.ticks_diff(time.ticks_us(), start_time) > TIMEOUT_US:
            print("Timeout: El eco no regreso")
            distancia = None
            break
    else:
        inicio = time.ticks_us()
        
        #REVISANDO QUE LA SEÑAL NO SE HAYA "PERDIDO"
        while echo_pin.value() == 1:
            if time.ticks_diff(time.ticks_us(), inicio) > TIMEOUT_US:
                print("Timeout: No echo received (end)")
                distancia = None
                break
        else:
            final = time.ticks_us()
            distancia = (final - inicio) / 58  #CONVERSION A [cm]
    
    if distancia != None and distancia < 125: #SI TODO ESTO ES VERDADERO, HACEMOS SONAR EL BUZZER
        print("Distancia: " + str(int(distancia)) + " Cm")
        buzzer_beep(distancia)
        
    else:
        buzzer.duty_u16(0)  #Apagando el buzzer

    time.sleep_us(1)
    
    
    #AJUSTE PARA QUE NO SE GENEREN "BUGS" A LA HORA DE PRESIONAR EL BOTON
    if boton_presionado > 0:
        boton_presionado = boton_presionado - 0.1
    if boton_presionado < 0:
        boton_presionado = 0
        
        
    #CUANDO SE PRESIONA EL BOTON
    if boton.value() == False and boton_presionado <= 0:
        detectando_sala = True
        boton_presionado = 2
        print("Botón presionado")
    
    time.sleep_us(1)
