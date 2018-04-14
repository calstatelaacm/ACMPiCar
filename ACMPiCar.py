import RPi.GPIO as gpio
import time
import sys
from evdev import InputDevice, categorize, ecodes

# read the input from the bluetooth device
# the device may change, however
# To see what devices are registered on your device, use
# ls /dev/input/
gamepad=InputDevice('/dev/input/event0')

print(gamepad)


# Choose the GPIO pins for your left and right side motors
r = [2, 3]
l = [17, 27]

# Initialize the pins
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup (r[0], gpio.OUT)
    gpio.setup (r[1], gpio.OUT)
    gpio.setup (l[0], gpio.OUT)
    gpio.setup (l[1], gpio.OUT)
    
def move_forward():
    init()
    print("ONWARDS")
    gpio.output(r[0], False)
    gpio.output(r[1], True)
    gpio.output(l[0], False)
    gpio.output(l[1], True)
    time.sleep(1)
    gpio.cleanup()

def move_back():
    init()
    print("Backwards")
    gpio.output(r[0], True)
    gpio.output(r[1], False)
    gpio.output(l[0], True)
    gpio.output(l[1], False)
    time.sleep(1)
    gpio.cleanup()

# To turn left, rotate the left wheels backwards and the right wheels forwards
def turn_left():
    init()
    print("LEFT")
    gpio.output(r[0], True)
    gpio.output(r[1], False)
    gpio.output(l[0], False)
    gpio.output(l[1], True)
    time.sleep(1)
    gpio.cleanup()
    
# To turn right, do the opposite
def turn_right():
    init()
    print("RIGHT")
    gpio.output(r[0], False)
    gpio.output(r[1], True)
    gpio.output(l[0], True)
    gpio.output(l[1], False) 
    time.sleep(1)
    gpio.cleanup()
    

def stop():
    init()
    gpio.output(r[0], False)
    gpio.output(r[1], False)
    gpio.output(l[0], False)
    gpio.output(l[1], False)
    gpio.cleanup()


# Check every event that is read through the bluetooth controller
for event in gamepad.read_loop():
    # If the event has an event key
    if event.type== ecodes.EV_KEY:
        if event.value==1:
        # Check if it matches the pre-determined buttons
        # and perform some function
            if event.code==115:
                print("UP")
                move_back()
            elif event.code== 114:
                print("LEFT")
                turn_left()
            elif event.code== 158:
                print("RIGHT")
                turn_right()
            elif event.code== 28:
                print("DOWN")
                move_forward()
            elif event.code== 272:
                sys.exit()    
    # To find which event codes correspond to you controller,
    # simply use:
    #
    #    for event in gamepad.read_loop():
    #        print(event)
    #
    # And use the process of elimination
    

#move_back()
#move_forward()
#turn_left()
#turn_right()
#time.sleep(3)
#stop()
    

    
    
