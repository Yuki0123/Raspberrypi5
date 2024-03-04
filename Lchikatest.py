import gpiod
import time


PIN_NO = 17
chip = gpiod.Chip('gpiochip4', gpiod.Chip.OPEN_BY_NAME)
line = chip.get_line(PIN_NO)
line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

# GPIOライン25をHIGHに設定
line.set_value(1)

# 1秒待機
time.sleep(1)

# GPIOライン25をLOWに設定
line.set_value(0)