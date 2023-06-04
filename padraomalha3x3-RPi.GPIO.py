# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

def padrao1():
  LED_PIN = 1,2,3,4,5,6,7,8,9
  GPIO.setup(LED_PIN, GPIO.OUT)
    
  print("LED ON")
  GPIO.output(LED_PIN,GPIO.HIGH)
          
  time.sleep(4)
def padrao2():
  LED_PIN = 5
  GPIO.setup(LED_PIN, GPIO.OUT)

          
  print("LED OFF")
  GPIO.output(LED_PIN, GPIO.LOW)
          
  time.sleep(4)  
  
def padrao3():
  LED_PIN = 1, 3, 5, 7, 9
  GPIO.setup(LED_PIN, GPIO.OUT)
  
  print("LED OFF")
  GPIO.output(LED_PIN, GPIO.LOW)
  
  time.sleep(4)

def padrao4():
  LED_PIN_ON = 1,3,7,9
  LED_PIN_OFF = 2, 4 ,5 ,6,8
  GPIO.setup(LED_PIN_ON, GPIO.OUT)
  GPIO.setup(LED_PIN_OFF, GPIO.OUT)
  print("LED ON")
  GPIO.output(LED_PIN_ON, GPIO.HIGH)
  time.sleep(2)
  
  print("LED OFF")
  GPIO.output(LED_PIN_OFF, GPIO.LOW)
  time.sleep(2)
  
def padrao5():
  LED_PIN_ON = 2, 4, 6, 8
  LED_PIN_OFF = 1,3,5,7,9
  GPIO.setup(LED_PIN_ON, GPIO.OUT)
  GPIO.setup(LED_PIN_OFF, GPIO.OUT)
  print("LED ON")
  GPIO.output(LED_PIN_ON, GPIO.HIGH)
  time.sleep(2)
  print("LED OFF")
  GPIO.output(LED_PIN_OFF, GPIO.LOW)
  time.sleep(2)
  
def padrao6():
  LED_PIN_ON = 1, 3, 7, 9
  print("LED ON")
  GPIO.output(LED_PIN_ON, GPIO.HIGH)
  time.sleep(2)
        
while True:
    padrao1()
    padrao2()
    padrao3()
    padrao4()
    padrao5()
    padrao6()