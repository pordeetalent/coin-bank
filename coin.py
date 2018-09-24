#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from time import sleep
import os
import paho.mqtt.publish as publish

baht1_pin = 6
baht2_pin = 13
baht5_pin = 19
baht10_pin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(baht1_pin, GPIO.IN)
GPIO.setup(baht2_pin, GPIO.IN)
GPIO.setup(baht5_pin, GPIO.IN)
GPIO.setup(baht10_pin, GPIO.IN)

baht1_v = 0
baht2_v = 0
baht5_v = 0
baht10_v = 0
bahtall_v = 0
bahtall_pst = 0




def baht1_func():
    global baht1_v
    global bahtall_v
    baht1_v = baht1_v + 1
    bahtall_v = bahtall_v + 1
    publish.single("baht/1", baht1_v, hostname="localhost")

    return baht1_v
    return bahtall_v
    
def baht2_func():
    global baht2_v
    global bahtall_v
    baht2_v = baht2_v + 1
    bahtall_v = bahtall_v + 2
    publish.single("baht/2", baht2_v, hostname="localhost")

    return baht2_v
    return bahtall_v

def baht5_func():
    global baht5_v
    global bahtall_v
    baht5_v = baht5_v + 1
    bahtall_v = bahtall_v + 5
    publish.single("baht/5", baht5_v, hostname="localhost")
    
    return baht5_v
    return bahtall_v

def baht10_func():
    global baht10_v
    global bahtall_v
    baht10_v = baht10_v + 1
    bahtall_v = bahtall_v + 10
    publish.single("baht/10", baht10_v, hostname="localhost")
    
    return baht10_v
    return bahtall_v
    



def print_func():
    global baht1_v
    global baht2_v
    global baht5_v
    global baht10_v
    global bahtall_v
    publish.single("baht/all", bahtall_v, hostname="localhost")
    print("[[[PorPeang's coin Bank.]]]")
    print("1 baht = " +str(baht1_v))
    print("2 baht = " +str(baht2_v))
    print("5 baht = " +str(baht5_v))
    print("10 baht = " +str(baht10_v))
    print("Total = " +str(bahtall_v))
    lcdprint = "lcdi2c -b 1 -i -x 0 -y 1 -a 3f \"PorPeang's Bank.Total=\" " + str(bahtall_v)
    os.system(lcdprint)
    sleep(0.5)


while True:
    if GPIO.input(baht1_pin):
        baht1_func()
        print_func()
    elif GPIO.input(baht2_pin):
        baht2_func()
        print_func()
    elif GPIO.input(baht5_pin):
        baht5_func()
        print_func()
    elif GPIO.input(baht10_pin):
        baht10_func()
        print_func()
    else:
        pass
    

    


