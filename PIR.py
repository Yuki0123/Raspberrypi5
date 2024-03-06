import gpiod
import time
from gpiozero import PWMOutputDevice

# GPIOピンの定義
LED_PIN_RED = 22
LED_PIN_GREEN = 18
LED_PIN_BLUE = 27

# GPIOチップの初期化
chip = gpiod.Chip('gpiochip4')  # 使用するgpiochipが異なる場合は変更

# 赤色LED用PWMデバイスの生成
led_red_pwm = PWMOutputDevice(chip=chip, line=LED_PIN_RED, frequency=2000)

# GPIOラインのリクエスト (出力モードで)
#led_line_red = chip.get_line(LED_PIN_RED)
led_line_green = chip.get_line(LED_PIN_GREEN)
led_line_blue = chip.get_line(LED_PIN_BLUE)

#led_line_red.request(consumer="LED_RED", type=gpiod.LINE_REQ_DIR_OUT)
led_line_green.request(consumer="LED_GREEN", type=gpiod.LINE_REQ_DIR_OUT)
led_line_blue.request(consumer="LED_BLUE", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        led_red_pwm.value = 0.5  # 赤LEDを点灯
        led_line_green.set_value(1)  # 緑LEDを消灯
        led_line_blue.set_value(1)  # 青LEDを点灯

        time.sleep(1)  # 遅延を入れてボタン状態の変化に適応

finally:
    # GPIOラインの解放
    led_line_red.release()
    led_line_green.release()
    led_line_blue.release()
 