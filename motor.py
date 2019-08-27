import RPi.GPIO as GPIO
import time

MOTOR_L1 = 11
MOTOR_L2 = 13
MOTOR_R1 = 16
MOTOR_R2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_L1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_L2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_R1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_R2, GPIO.OUT, initial=GPIO.LOW)

def forword():
    GPIO.output(MOTOR_L1, False)
    GPIO.output(MOTOR_L2, True)
    GPIO.output(MOTOR_R1, False)
    GPIO.output(MOTOR_R2, True)

def backword():
    GPIO.output(MOTOR_L1, True)
    GPIO.output(MOTOR_L2, False)
    GPIO.output(MOTOR_R1, True)
    GPIO.output(MOTOR_R2, False)

def stop():
    GPIO.output(MOTOR_L1, False)
    GPIO.output(MOTOR_L2, False)
    GPIO.output(MOTOR_R1, False)
    GPIO.output(MOTOR_R2, False)

def open():
    forword()
    time.sleep(2)
    stop()
    time.sleep(1.5)
    backword()
    time.sleep(2)

open()
GPIO.cleanup()
