import pigpio
import time

MOTOR_L1 = 11
MOTOR_L2 = 13
MOTOR_R1 = 16
MOTOR_R2 = 18

pi = pigpio.pi()

def forword():
    pi.write(MOTOR_L1, 1)
    pi.write(MOTOR_L2, 0)
    pi.write(MOTOR_R1, 1)
    pi.write(MOTOR_R2, 0)

def backword():
    pi.write(MOTOR_L1, 0)
    pi.write(MOTOR_L2, 1)
    pi.write(MOTOR_R1, 0)
    pi.write(MOTOR_R2, 1)

def stop():
    pi.write(MOTOR_L1, 0)
    pi.write(MOTOR_L2, 0)
    pi.write(MOTOR_R1, 0)
    pi.write(MOTOR_R2, 0)

def open():
    forword()
    time.sleep(2)
    stop()
    time.sleep(1.5)
    backword()
    time.sleep(2)

if '__main__' == __name__:
    open()

