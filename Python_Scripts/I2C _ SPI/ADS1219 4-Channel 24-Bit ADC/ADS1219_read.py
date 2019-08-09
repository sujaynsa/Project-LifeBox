import smbus
from time import sleep

x = 1

# Get I2C bus
bus = smbus.SMBus(1)

# ADS1219 address, 0x40
#Reset the Device
bus.write_byte(0x40, 0X06)
#RREG
bus.write_byte_data(0x40, 0X41, 0x63)
sleep(1)
#Start Conversion
bus.write_byte(0x40, 0X08)
sleep(1)
while True:
    r_data = bus.read_i2c_block_data(0x40, 0X10, 3)
    #print(r_data)
    conv_data = (r_data[0] << 16) + (r_data[1] << 8) + r_data[2]
    if (r_data[0] & 0x80):
        count = (conv_data & 0x7fffff) - 8388608
    else :
        count = conv_data
    v = (count/8388608)*3.3
    #print(count)
    #print(v)
    if x == 1:
        print('Voltage at A0:',v)
        bus.write_byte_data(0x40, 0X41, 0x83)
    if x == 2:
        print('Voltage at A1:',v)
        bus.write_byte_data(0x40, 0X41, 0xA3)
    if x == 3:
        print('Voltage at A2:',v)
        bus.write_byte_data(0x40, 0X41, 0xC3)
    if x == 4:
        print('Voltage at A3:',v)
        bus.write_byte_data(0x40, 0X41, 0x63)
        x = 0
    x += 1
    sleep(1)
