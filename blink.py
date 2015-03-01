import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


def Blink(numTimes, speed):
    speed = float(speed)
    for i in range(0, numTimes):
        print "Iteration " + str(i+1)
        GPIO.output(7, True)
        time.sleep(speed)
        GPIO.output(7, False)
        time.sleep(speed)
    print "Done"
    GPIO.cleanup()


Blink(5, 1)
