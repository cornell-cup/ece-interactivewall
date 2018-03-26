int top_scan_pin
int bottom_scan_pin

GPIO.setup(top_scan_pin, GPIO.INPUT)
GPIO.setup(bottom_scan_pin, GPIO.INPUT)

def stop():
    print('stopping the scanner when it reaches the top or bottom')
    GPIO.output(enablePin1, GPIO.HIGH) #disable driver

GPIO.add_event_detect(bottom_scan_pin, GPIO.RISING, callback=stop, bouncetime=2000)
GPIO.add_event_detect(top_scan_pin, GPIO.RISING, callback=stop, bouncetime=2000)
#add interrupt and handler for start and reset button

#the following method isn't needed once CS is integrated
def reset(): #motor 
    moveScannerUp(10000)
    moveScannerDown(200) #release from pressing the switch
    moveVerticalUp(10000)
    moveVerticalDown(200) #release from pressing the switch
    moveHorizontalLeft(10000)
    moveHorizontalRight(200) #release from pressing the switch
