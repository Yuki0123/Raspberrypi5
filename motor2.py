import gpiod
import time
import RPi.GPIO as GPIO

EN_PIN = 22
A_PIN1 = 27
A_PIN2 = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_PIN, GPIO.OUT)
GPIO.setup(A_PIN1, GPIO.OUT)


try:
    GPIO.output(EN_PIN, GPIO.HIGH)


    while True:
        GPIO.output(A_PIN1, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(A_PIN1, GPIO.LOW)
        time.sleep(5)

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    GPIO.cleanup()
