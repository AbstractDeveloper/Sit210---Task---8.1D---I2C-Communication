# Importing the libraries
import smbus
import time

# Device Address
Sensor = 0x23

Address = 0x23

# To initiate the smbus library bus is used as a variable
bus = smbus.SMBus(1)

# Used to have the readings of the sensor
def light():
    address = bus.read_i2c_block_data(Sensor, Address)
    value = Light_intensity(address)
    return value    # Returns the captured value

def Light_intensity(address):
    result = ((address[1] + (256 * address[0])) / 1.2)
    return int (result)   # Returns the calculated result

def output():
    while True:
        # To display the value
        intensity = light()

        if(intensity >= 400):
            print(str(light()) + " -> Too Bright")
        elif(intensity > 200 and intensity < 400):
            print(str(light()) + " -> Bright")
        elif(intensity > 50 and intensity < 200):
            print(str(light()) + " -> Medium")
        elif(intensity > 20 and intensity < 50):
            print(str(light()) + " -> Dark")
        elif(intensity < 20):
            print(str(light()) + " -> Too Dark")

        # Delay of 1 second
        time.sleep(1)
        
output()