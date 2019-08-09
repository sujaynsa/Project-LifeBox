#Plot CPU temperature of Raspberry Pi in real time

from guizero import App, Picture
import matplotlib.pyplot as plt
from gpiozero import CPUTemperature
from time import time
import RPi.GPIO as io

cpu = CPUTemperature()
x=[]
y=[]
#io.setmode(io.BCM)
#io.setup(17, io.OUT)
#io.output(17, True)

start_time = time()

def graph():
    global start_time
    temp = cpu.temperature
    y.append(temp)
    x.append(time()-start_time)
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Temperature')
    plt.title('CPU Temperature')
    plt.grid(True)
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.savefig('/home/pi/Documents/2.png')
    plt.close('all')
    picture.set('/home/pi/Documents/2.png')


app = App()
picture = Picture(app,align="top",width = 500,height = 300)
picture.repeat(250,graph)


app.display()
