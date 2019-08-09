import serial
from time import sleep,time

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

def bytes_4(data_conv):
    data = [0,0,0,0]
    data[0] = (data_conv >> 24) & (255)
    data[1] = (data_conv >> 16) & (255)
    data[2] = (data_conv >> 8) & (255)
    data[3] = (data_conv) & (255)
    return data

p_key = 0x11021
rev = 60
power = 60
qpps = 7700

power_conv = int((power/100)*qpps)
print(power_conv)
power_data = bytes_4(power_conv)
print(power_data)

rev_conv = 256 + ((rev-1)*1024) - round((power - 20)*(38.395) + 0.8)
print(rev_conv)
rev_data = bytes_4(rev_conv)
print(rev_data)

p_1 = [128,20]
p_1_crc = p_1 + crc16(p_1,p_key)
print('packet :',p_1_crc)
p_2 = [128,16]
p_3 = [128,41]+power_data+rev_data+[1]
p_3_crc = p_3 + crc16(p_3,p_key)
print('packet :',p_3_crc)

port = serial.Serial("/dev/ttyS0", baudrate=38400, timeout=1)
sleep(1)

port.write(bytearray(p_1_crc))
received_data = port.read(1)
print('Received Data: ','\n',str(received_data))
port.write(bytearray(p_2))
received_data = port.readline()
print('Received Data: ','\n',str(received_data))
port.write(bytearray(p_3_crc))
received_data = port.read(1)
print('Received Data: ','\n',str(received_data))
sleep(20)
port.write(bytearray(p_2))
received_data = port.readline()
ls = list(received_data)
print('Received Data: ','\n',ls)
count = (ls[0]<<32)+(ls[1]<<16)+(ls[2]<<8)+ls[3]
print('Count :',count)
volume = round(count/328.169)
print('Volume (in ml):',volume)
