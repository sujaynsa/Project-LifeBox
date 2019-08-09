import smbus
from time import sleep

sel = 14

# Get I2C bus
bus = smbus.SMBus(1)

# DRV2605L address, 0x5a

#Reset the Device
#bus.write_byte_data(0x5a, 0X01, 0x80)
#sleep(1)
#Set Device in Auto calibration mode
#bus.write_byte_data(0x5a, 0X01, 0x07)
#Begin Auto calibration
#bus.write_byte_data(0x5a, 0x0C, 0x01)
#sleep(1)

#Set Device in Internal trigger mode
bus.write_byte_data(0x5a, 0X01, 0x00)
sleep(1)
#Set Waveform Sequencer
bus.write_byte_data(0x5a, 0X04, sel)
bus.write_byte_data(0x5a, 0X05, sel)
bus.write_byte_data(0x5a, 0X06, 0x00)
bus.write_byte_data(0x5a, 0X07, 0x00)
#Begin Waveform Sequence
bus.write_byte_data(0x5a, 0x0C, 0x01)
sleep(1)
data = bus.read_byte_data(0x5a, 0X01)
print(bin(data))
data = bus.read_byte_data(0x5a, 0X0C)
print(bin(data))



