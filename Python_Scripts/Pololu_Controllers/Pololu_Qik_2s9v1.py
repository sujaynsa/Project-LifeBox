import serial
from time import sleep,timez

init_cmd = [0xAA,0x09,0x04,0x01,0x00,0x55,0x2A]
motor_stop = [0x8c,0x00]
motor_cmd = [140,0]

port = serial.Serial("/dev/ttyS0", baudrate=38400, timeout=1)
port.write(bytearray(init_cmd))
sleep(1)

power = 100
speed_int = int(power*1.27)
motor_cmd[1] = speed_int
port.write(bytearray(motor_cmd))
sleep(10)
port.write(bytearray(motor_stop))

received_data = str(port.readline())
print('Received Data: ','\n',received_data)



    
