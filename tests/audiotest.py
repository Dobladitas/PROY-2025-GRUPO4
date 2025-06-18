from machine import Pin, PWM
import ustruct
import time
#unsigned 8 bit PCM

# Set up PWM on GPIO 1
audio = PWM(Pin(1))
audio.freq(8000)  # 8kHz to match the .wav sample rate
audio.duty_u16(0)  # Start with silence

def play_wav(filename):
    try:
        with open(filename, "rb") as f:
            f.read(44)  # Skip the WAV file header

            while True:
                data = f.read(1024)
                if not data:
                    break

                for b in data:
                    sample = ustruct.unpack("B", bytes([b]))[0]
                    duty = int(sample / 255 * 65535)
                    audio.duty_u16(duty)
                    time.sleep_us(125)  # 8000 Hz = 125 µs per sample

        audio.duty_u16(0)  # Turn off after playback
    except Exception as e:
        print("Error playing file:", e)

# Run it
play_wav("test.wav")
                 