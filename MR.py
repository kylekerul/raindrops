import time
from time import sleep 
import os
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

Motor1 = 23    # Input Pin pin7_IC
Motor2 = 24    # Input Pin pin2_IC
Motor3 = 25    # Enable Pin pin1_IC

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
pwm=GPIO.PWM(25,100) 
GPIO.setup(12, GPIO.IN)

while(1):
 x=1
 while(x==1):   
  if (GPIO.input(12) == True):
   print "Fine Weather!"
   pwm.start(70)
   GPIO.output(Motor1,GPIO.LOW)
   GPIO.output(Motor2,GPIO.HIGH)
   GPIO.output(Motor3,GPIO.HIGH)
   sleep(2)
   GPIO.output(Motor2,GPIO.LOW) 
   sleep(2) 
   x=x+1
    

  z=2 
  y=1 
 while(z!=1):
  while(y==1):
   GPIO.output(Motor1,GPIO.LOW)
   if (GPIO.input(12) == False):
    print "RAINING!"
    pwm.start(70)
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor2,GPIO.LOW)
    GPIO.output(Motor3,GPIO.HIGH)
    sleep(2)
    GPIO.output(Motor1,GPIO.LOW) 
    sleep(2)
    y=y+1
   if (GPIO.input(12) == True):	 
    z=1
    
    	
	
	
  


