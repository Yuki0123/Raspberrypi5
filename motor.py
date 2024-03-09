import gpiod
import time


EN_PIN = 22
A_PIN1 = 27
A_PIN2 = 17

chip = gpiod.Chip('gpiochip4', gpiod.Chip.OPEN_BY_NAME)
en_line = chip.get_line(EN_PIN)
a1_line= chip.get_line(A_PIN1)
a2_line = chip.get_line(A_PIN2)

en_line.request(consumer="EN", type=gpiod.LINE_REQ_DIR_OUT)
a1_line.request(consumer="A1", type=gpiod.LINE_REQ_DIR_OUT)
a2_line.request(consumer="A2", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        en_line.set_value(1)
        a1_line.set_value(1)
        a2_line.set_value(0)
        time.sleep(5)
        a1_line.set_value(0)
        a2_line.set_value(1)
        time.sleep(5)

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    en_line.release()
    a1_line.release()
    a2_line.release()
    chip.close()