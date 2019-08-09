import serial
from time import sleep,time

power = 60

def crc16(packet,key):
    packet_len = len(packet)
    crc = 0
    crc_ls = [0,0]
    for l1 in range(packet_len):
        crc = crc ^ (packet[l1] << 8)
        for l2 in range(8):
            if (crc & 0x8000):
                crc = (crc << 1) ^ key
            else :
                crc = crc << 1
    crc_ls[0] = crc >> 8
    crc_ls[1] = crc & (0xFF)
    return crc_ls

p_key = 0x11021

motor_full = [128,0,0]
speed_int = int(power*1.27)
motor_full[2] = speed_int
motor_full_crc = motor_full + crc16(motor_full,p_key)
print(motor_full_crc)
motor_stop = [128,0,0]
motor_stop_crc = motor_stop + crc16(motor_stop,p_key)
print(motor_stop_crc)

port = serial.Serial("/dev/ttyS0", baudrate=38400, timeout=1)
sleep(1)

port.write(bytearray(motor_full_crc))
received_data = port.read(1)
print('Received Data: ','\n',str(received_data))
sleep(10)
port.write(bytearray(motor_stop_crc))
received_data = port.read(1)
print('Received Data: ','\n',str(received_data))
