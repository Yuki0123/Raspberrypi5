import gpiod
import time
from gpiozero import PWMOutputDevice
import random

# GPIOピンの定義
LED_PIN_RED = 22
LED_PIN_GREEN = 18
LED_PIN_BLUE = 27
pirPin=17

# GPIOチップの初期化
chip = gpiod.Chip('gpiochip4')  # 使用するgpiochipが異なる場合は変更

# GPIOラインのリクエスト (出力モードで)
pir_line=chip.get_line(pirPin)

pir_line.request(consumer="PIR", type=gpiod.LINE_REQ_DIR_IN)

def setup():
    global led_red_pwm,led_green_pwm,led_blue_pwm

    # 赤色LED用PWMデバイスの生成
    led_red_pwm = PWMOutputDevice(LED_PIN_RED, frequency=2000)
    led_green_pwm = PWMOutputDevice(LED_PIN_GREEN, frequency=2000)
    led_blue_pwm = PWMOutputDevice(LED_PIN_BLUE, frequency=2000)


def setcolor(color):
        #print(color)
        led_red_pwm.value = color[0]  # 赤LEDを点灯
        led_green_pwm.value=color[1]  # 緑LEDを消灯
        led_blue_pwm.value=color[2]   # 青LEDを点灯
        print(color[2])

def loop():
    while True:
       pir_state = pir_line.get_value()
       if pir_state == 1:
           setcolor([0,1,0])
       else:
           setcolor([1,0,0])
           

def destroy():
    led_red_pwm.close()
    led_green_pwm.close()
    led_blue_pwm.close()
    pir_line.release()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()