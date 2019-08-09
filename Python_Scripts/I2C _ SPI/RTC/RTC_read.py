import smbus
from time import sleep

seconds = 0
minutes = 50
hours = 12
date = 16
month = 4
year = 19

# Get I2C bus
bus = smbus.SMBus(1)

# DS3231 address, 0x68
bus.write_byte_data(0x68, 0X0E, 0x1C)
bus.write_byte_data(0x68, 0X0F, 0x00)
sleep(1)
r_data = bus.read_byte_data(0x68, 0X0E)
print(bin(r_data))
r_data = bus.read_byte_data(0x68, 0X0F)
print(bin(r_data))

seconds_2 = seconds % 10
seconds_1 = int((seconds - seconds_2)/10) << 4
seconds_data = (seconds_1 & 0xF0) | (seconds_2 & 0x0F)
print(bin(seconds_data))

minutes_2 = minutes % 10
minutes_1 = int((minutes - minutes_2)/10) << 4
minutes_data = (minutes_1 & 0xF0) | (minutes_2 & 0x0F)
print(bin(minutes_data))

hours_2 = hours % 10
hours_1 = int((hours - hours_2)/10) << 4
hours_data = (hours_1 & 0xF0) | (hours_2 & 0x0F)
print(bin(hours_data))

date_2 = date % 10
date_1 = int((date - date_2)/10) << 4
date_data = (date_1 & 0xF0) | (date_2 & 0x0F)
print(bin(date_data))

month_2 = month % 10
month_1 = int((month - month_2)/10) << 4
month_data = (month_1 & 0xF0) | (month_2 & 0x0F)
print(bin(month_data))

year_2 = year % 10
year_1 = int((year - year_2)/10) << 4
year_data = (year_1 & 0xF0) | (year_2 & 0x0F)
print(bin(year_data))

#bus.write_byte_data(0x68, 0X00, seconds_data)
#bus.write_byte_data(0x68, 0X01, minutes_data)
#bus.write_byte_data(0x68, 0X02, hours_data)
#bus.write_byte_data(0x68, 0X04, date_data)
#bus.write_byte_data(0x68, 0X05, month_data)
#bus.write_byte_data(0x68, 0X06, year_data)

while True:
    sec_data = bus.read_byte_data(0x68, 0X00)
    min_data = bus.read_byte_data(0x68, 0X01)
    hr_data = bus.read_byte_data(0x68, 0X02)
    r_date_data = bus.read_byte_data(0x68, 0X04)
    mon_data = bus.read_byte_data(0x68, 0X05)
    yr_data = bus.read_byte_data(0x68, 0X06)
    sec_2 = sec_data & 0x0F
    sec_1 = (sec_data >> 4) & 0x0F
    sec = (sec_1 * 10) + sec_2
    min_2 = min_data & 0x0F
    min_1 = (min_data >> 4) & 0x0F
    r_min = (min_1 * 10) + min_2
    hr_2 = hr_data & 0x0F
    hr_1 = (hr_data >> 4) & 0x0F
    hr = (hr_1 * 10) + hr_2
    r_date_2 = r_date_data & 0x0F
    r_date_1 = (r_date_data >> 4) & 0x0F
    r_date = (r_date_1 * 10) + r_date_2
    mon_2 = mon_data & 0x0F
    mon_1 = (mon_data >> 4) & 0x0F
    mon = (mon_1 * 10) + mon_2
    yr_2 = yr_data & 0x0F
    yr_1 = (yr_data >> 4) & 0x0F
    yr = 2000 + (yr_1 * 10) + yr_2
    print('-'*10)
    print('Seconds :',sec)
    print('Minutes :',r_min)
    print('Hours :',hr)
    print('Date :',r_date)
    print('Month :',mon)
    print('Year :',yr)
    sleep(1)
