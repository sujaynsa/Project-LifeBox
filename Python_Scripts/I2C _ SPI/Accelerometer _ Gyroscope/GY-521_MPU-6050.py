import smbus
from time import sleep, time

# Get I2C bus
bus = smbus.SMBus(bus = 1)

bus.write_byte_data(0x68, 0X6B, 128)
sleep(1)
bus.write_byte_data(0x68, 0X6B, 0)
sleep(1)

# MCP9808 address, 0x68(96)
# Read data back from 0x05(05) register, 1 bytes
# Ambient Temperature
#data = bus.read_word_data(0x68, 0x05)

while True:
    start_time = time()
    data_MSB = bus.read_byte_data(0x68, 0x3B)
    data_LSB = bus.read_byte_data(0x68, 0x3C)
    sign = (data_MSB & 128)
    data_MSB = (data_MSB & 127) << 8
    data = data_MSB + data_LSB
    if sign == 128:
        data = data - 32768
        acc = data / 16384.0
    else :
        acc = data / 16384.0
    acc_f = - acc
    #data_bin = bin(data)
    #temp_bin = bin(temp_bits)
    #print('Data received in binary:', data_bin)
    #print('Converted Temperature in binary:',temp_bin)
    print('Converted Acceleration reading:',acc_f,' in g')
    stop_time = time()
    time_elapsed = stop_time - start_time
    print('Time elapsed:',time_elapsed,' in s')
    sleep(1)
