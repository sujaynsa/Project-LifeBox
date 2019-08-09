import smbus
from time import sleep

# Get I2C bus
bus = smbus.SMBus(bus = 1)

# MCP9808 address, 0x18(96)
# Read data back from 0x05(05) register, 1 bytes
# Ambient Temperature
#data = bus.read_word_data(0x18, 0x05)

while True:
    data = bus.read_word_data(0x18, 0x05)
    MSB = (data & 15)
    data_MSB = MSB << 8
    LSB = (data & 65280)
    data_LSB = LSB >> 8
    temp_bin = data_MSB | data_LSB
    temp = temp_bin/16.0
    data_bin = bin(data)
    temp_binary = bin(temp_bin)
    print('Data received in binary:', data_bin)
    print('Converted Temperature in binary:',temp_binary)
    print('Converted Temperature reading:',temp)
    print('-'*50)
    sleep(1)
