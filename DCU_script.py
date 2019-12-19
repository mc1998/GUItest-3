import requests
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)


payload = { 'battery_switch': ' ', 'O2_switch': ' ', 'switch3': ' ', 'switch4': ' ', 'switch5': ' ', 'fan_switch': ' ' }

try:
    while True:
        if (GPIO.input(18) == True):
            payload['fan_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
            
        if (GPIO.input(17) == True):
            payload['O2_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
            
        if (GPIO.input(15) == True):
            payload['fan_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
            
        if (GPIO.input(27) == True):
            payload['fan_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
            
        if (GPIO.input(22) == True):
            payload['fan_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
            
        if (GPIO.input(3) == True):
            payload['fan_switch'] = 'false'
        else:
            payload['fan_switch'] = 'true'
    #  ip address has to be on same network/ IP address
    # both have to be connected through that router
    # url should have the address or
    #192.70.120.211
    # http://192.70.120.211:3000/api/simulation/dcucontrols
    # when hosting the simulation everything will have its own ip
    # .211 is the address (big white cube one netgear) 
    
        #url = 'http://169.254.86.147:3000/api/simulation/newuiacontrols'
        #url = 'http://169.254.86.147:3000'
        url = 'http://localhost:3000'
        r = requests.patch (url, params = payload)
        print (r.url)
  
except KeyboardInterrupt: print ("user interruption") #interruption using Keyboard "CTRL" + "C"
except : print ("other error")
