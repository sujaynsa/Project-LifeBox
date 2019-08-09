import smbus
from time import sleep

# Get I2C bus
bus = smbus.SMBus(1)

# GY-906 address, 0x5a

while True:
    # Read data back from 0x06(06) register
    # Ambient Temperature
    data_ambient = bus.read_word_data(0x5b, 0x06)
    temp_ambient = (data_ambient * 0.02) - 273.0
    print("Converted Temperature Ambient reading: {:06.2f}".format(temp_ambient))
    # Read data back from 0x07(07) register
    # Object Temperature
    data_object_1 = bus.read_word_data(0x5b, 0x07)
    temp_object_1 = (data_object_1 * 0.02) - 273.0
    #print('Converted Temperature Object_1 reading:',temp_object_1,' C')
    print("Converted Temperature Object-1 reading: {:06.2f}".format(temp_object_1))
    print('-'*65)
    sleep(1)
#    data = bus.read_word_data(0x5a, 0x05)
#    data_bin = bin(data)
#    print('Data received in binary:', data_bin)
#    print('Converted Temperature in binary:',temp_bin)
#    print('Converted Temperature reading:',temp)
#    sleep(5)
