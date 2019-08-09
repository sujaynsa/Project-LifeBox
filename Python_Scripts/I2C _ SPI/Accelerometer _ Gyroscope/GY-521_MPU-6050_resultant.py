import smbus
from time import sleep, time
import math

start_time = time()

# Get I2C bus
bus = smbus.SMBus(bus = 1)

bus.write_byte_data(0x69, 0X6B, 128)
sleep(1)
bus.write_byte_data(0x69, 0X6B, 0)
sleep(1)
bus.write_byte_data(0x69, 0X1C, 8)
sleep(1)

while True:
    x_MSB = bus.read_byte_data(0x69, 0x3B)
    x_LSB = bus.read_byte_data(0x69, 0x3C)
    y_MSB = bus.read_byte_data(0x69, 0x3D)
    y_LSB = bus.read_byte_data(0x69, 0x3E)
    z_MSB = bus.read_byte_data(0x69, 0x3F)
    z_LSB = bus.read_byte_data(0x69, 0x40)
    x_sign = (x_MSB & 128)
    x_MSB = (x_MSB & 127) << 8
    x_data = x_MSB + x_LSB
    if x_sign == 128:
        x_data = x_data - 32768
        acc_x = x_data / 8192.0
    else :
        acc_x = x_data / 8192.0
    print("Acc_x :",acc_x)
    y_sign = (y_MSB & 128)
    y_MSB = (y_MSB & 127) << 8
    y_data = y_MSB + y_LSB
    if y_sign == 128:
        y_data = y_data - 32768
        acc_y = y_data / 8192.0
    else :
        acc_y = y_data / 8192.0
    print("Acc_y :",acc_y)
    z_sign = (z_MSB & 128)
    z_MSB = (z_MSB & 127) << 8
    z_data = z_MSB + z_LSB
    if z_sign == 128:
        z_data = z_data - 32768
        acc_z = z_data / 8192.0
    else :
        acc_z = z_data / 8192.0
    print("Acc_z :",acc_z)
    resultant_acc = math.sqrt(pow(acc_x,2)+pow(acc_y,2)+pow(acc_z,2))
    print('Resultant Acceleration reading:',resultant_acc,' in g')
    time_elapsed = time() - start_time
    print('Time elapsed:',round(time_elapsed,2),' in s')
    if resultant_acc == 0.0 :
        bus.write_byte_data(0x69, 0X6B, 128)
        sleep(1)
        bus.write_byte_data(0x69, 0X6B, 0)
        sleep(1)
        bus.write_byte_data(0x69, 0X1C, 8)
        sleep(1)
    sleep(1)
