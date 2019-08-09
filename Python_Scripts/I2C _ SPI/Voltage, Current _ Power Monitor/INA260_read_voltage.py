import smbus
from time import sleep

# Get I2C bus
bus = smbus.SMBus(1)

#Reset Device
data = [0xE1,0x27]
print('Data to be sent :',bin(data[0]),' ',bin(data[1]))
bus.write_i2c_block_data(0x40,0x00,data)
sleep(1)

#Read Configuration Register
data = bus.read_i2c_block_data(0x40,0x00,2)
print('Initial Data :',bin(data[0]),' ',bin(data[1]))

#Set Configuration Register
data = [0x6b,0x27]
print('Data to be sent :',bin(data[0]),' ',bin(data[1]))
bus.write_i2c_block_data(0x40,0x00,data)
sleep(1)

#Verify contents of Configuration Register
data = bus.read_i2c_block_data(0x40,0x00,2)
print('Data stored :',bin(data[0]),' ',bin(data[1]))

#Read Voltage
while True:
    data = bus.read_i2c_block_data(0x40,0x02,2)
    print('Data stored :',bin(data[0]),' ',bin(data[1]))
    if (data[0] & 0x80):
        print("Under Voltage")
    else :
        voltage = (((data[0]<<8) + data[1])*1.25)/1000
        print("Voltage :",voltage," V")
    sleep(1)



