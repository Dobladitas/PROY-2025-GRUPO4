# PROY-2025-GRUPO4

Repositorio del **grupo 4** para el proyecto del ramo *Proyecto Inicial* – 2025.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol          |
| ----------------- | -------------- | ------------------------ | ------------ |
| Martín Pérez      | @dobladitas    | mperez@usm.cl            | 202530003-6 |
| Santiago Múnera   | @santiagomuneraa| smunera@usm.cl           | 202530024-9  |
| Lukas Grendi | @greenkass      | llealg@usm.cl | 202530035-4 |
| Nicolás Silva | @nicojjl      | nsilvad@usm.cl | 202530026-5 |

---

## 📝 Descripción breve del proyecto

> *Cansi tiene como objetivo mejorar la calidad de vida de personas no videntes mediante un dispositivo portátil que detecta obstáculos a través de un sensor de ultrasonido y alerta al usuario mediante vibraciones. Además, el dispositivo reconoce puntos de acceso distribuidos en salas universitarias mediante conexión Wi-Fi, permitiendo estimar la sala donde el usuario se encuentra. Todo el procesamiento se realiza mediante una Raspberry Pi Pico W, que coordina las señales del sensor, el motor de vibración y un laser ultrasonido.*

---

## 🎯 Objetivos

- Objetivo general:
  - El objetivo principal de nuestro proyecto es mejorar la calidad de vida de las personas no videntes de la universidad.
- Objetivos específicos:
  - *Listar objetivos concretos que permitirán alcanzar el objetivo general.*

---

## 🧩 Alcance del proyecto

> *El dispositivo posee dos funciones de las cuales podríamos considerar una universal y otra localizada. El proyecto, al tener la capacidad de detectar cuerpos solidos, se puede usar en cualquier lugar que se requiera. Por otro lado, su segunda funcionalidad está restringida a el lugar en donde se registraron previamente los puntos de acceso para identificar la posición estimada, en el caso de nuestro proyecto, de la universidad. Debido a esto no en todas partes se puede sar nuestro proyecto al 100%, pero sigue siendo posible usar al menos una función del dispositivo en cualquier sitio.*

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Python
- Microcontroladores
  - Raspberry Pi Pico W 2
- Sensores
  - HC-SR04
  - Botón
-Otros
  - Buzzer
  - Cable jack 3.5 (cable aux)
  - resistencia
  - Impresión 3D

---

## 🗂️ Estructura del repositorio

```
/PROY-2025-GRUPOX
│
├── docs/               # Documentos referentes (Carta gant, presentaciones hechas, etc...)
├── src/                # Código fuente del proyecto (Incluye archivos de audio en su respectiva carpeta dentro)
├── tests/              # Casos de prueba
└── README.md           # Este archivo
```

---

## 🧪 Metodología

> Comenzamos trabajando en la funcionalidad de detectar los puntos de acceso en la universidad, posteriormente programamos la estimacion de cual podria estar mas cerca.
> Una vez terminado esta parte del codigo, implementamos el sensor de ultra sonido (HC-SR04) para obtener las distancias de los objetos proximos, para despues combinarlo con un buzzer y hacer que suene en funcion de la distancia.
> Finalmente implementamos un boton para poder combinar todas las partes del codigo, primero programamos la logica de como todo debia funcionar, y despues escribimos el codigo final.

---

## 📅 Cronograma de trabajo


[Carta Gantt](https://docs.google.com/spreadsheets/d/1x-6Dj9K8uXK9_bMlVK5CzVprAU7yVYf6KnQrmKBqG6A/edit?usp=sharing)

---

## 📚 Bibliografía

 [MicroPython Documentation](https://docs.micropython.org/en/latest/)
 [Programming the Raspberry Pi Pico with MicroPython](https://www.raspberrypi.com/news/new-book-programming-the-raspberry-pi-pico-with-micropython/)
 [Ultrasonic Sensor HC-SR04 Tutorial](https://lastminuteengineers.com/hc-sr04-ultrasonic-sensor-arduino-tutorial/)
 [Using PWM to Output Audio](https://learn.adafruit.com/playing-wav-files-with-pwm)
 [WAV File Format Specification](https://learn.microsoft.com/en-us/windows/win32/api/mmreg/ns-mmreg-waveformat)
 [WAV Audio on Arduino](https://hackaday.io/project/6936-wav-audio-on-arduino)
 [ESP32 WiFi API Reference](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)

---

## 📌 Como usar

> Ejecutar el archivo main.py dentro de la carpeta src. El proyecto no requiere librerias adicionales. El usuario puede alejar o acercar el sensor a las superficies proximas para que el buzzer suene mas rapido o lento. Si se apreta el boton, se creara una estimacion de en que sala del piso 0 del edificio P de la universidad puedes estar, y se reproducira un audio.
