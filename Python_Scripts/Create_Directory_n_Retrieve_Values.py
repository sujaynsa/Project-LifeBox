#To retreive data stored in .txt files(named in the format YYYYMMDD.txt) and store it in a list

import os

start_date = 30
start_mon = 12
start_year = 2019

stop_date = 2
stop_mon = 1
stop_year = 2020
val_date = (stop_year*10000)+(stop_mon*100)+stop_date

r_data = []

current_date = start_date
current_mon = start_mon
current_year = start_year
while True:
    try:
        file = open("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0:02d}_{1:02d}_{2}/read_file.txt".format(current_date,current_mon,current_year),"r")
        data_str = file.readline()
        data_ls = data_str.split(",")
        for x in range(len(data_ls)):
            r_data.append(data_ls[x])
        file.close()
    except:
        file_exist = False
        print("error")
    current_date += 1
    if (current_date > 31):
        current_date = 1
        current_mon += 1
        if current_mon > 12:
            current_mon = 1
            current_year += 1
    val_current = (current_year*10000)+(current_mon*100)+current_date
    if val_current > val_date:
        break

print(r_data)

"""
os.mkdir("/home/pi/Documents/Python_Programs/Test/{0:02d}_{1:02d}_{2}".format(date,month,year))

for x in range(1,32,1):
    date = x
    os.mkdir("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0}{1:02d}{2:02d}".format(year,month,date))

ls = os.listdir("/home/pi/Documents/Python_Programs/Test/Text_Folder")
print(ls)

for x in range(1,32,1):
    file = open("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0}{1:02d}{2:02d}/{0}{1:02d}{2:02d}.txt".format(2019,5,x),"w")
    file.write("{0}{1:02d}{2:02d}".format(2019,5,x))
    file.close()

for y in range(11,13,1):
    month = y
    for x in range(1,32,1):
        date = x
        #os.mkdir("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0:02d}_{1:02d}_{2}".format(x,y,2020))
        file = open("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0:02d}_{1:02d}_{2}/read_file.txt".format(x,y,2019),"w")
        file.write("{0:02d}_{1:02d}_{2}".format(x,y,2019))
        file.close()

for x in range(len(ls)):
    data =  int(ls[x])
    if (data >= start_date):
        file = open("/home/pi/Documents/Python_Programs/Test/Text_Folder/{0}/read_file.txt".format(ls[x]),"r")
        r_data.append(file.readline())
        file.close()
"""

