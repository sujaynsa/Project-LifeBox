#PID controller for temperature control of Raspberry Pi CPU temperature
#Hardware Used: 3.3V 15mA DC Blower used to a GPIO PIN of Raspberry Pi
#Note: The same PID controller can be used with different setup. The only components
#of script that needs to be changed are : 1. Input to temperature variable in line 133,
#2. Integrate the script to control the new blower and attach the control variable to variable "power_output".

from gpiozero import CPUTemperature
from time import sleep, time,strftime
import RPi.GPIO as io
import math
import matplotlib.pyplot as plt

output_pin = 17
pwm_freq = 5

io.setmode(io.BCM)
io.setup(output_pin,io.OUT)
pwm = io.PWM(output_pin, pwm_freq)
pwm.start(0)

cpu = CPUTemperature()
x=[]
y=[]
target_temp_graph = []

target = 45

error_log = [0,0,0,0,0,0,0]
diff_log = [0,0]

p_result = 0
i_result = 0
d_result = 0

def P_in_PID(current_temp):
    p_result = (100*(current_temp-45))/3
    if p_result > 100:
        p_result = 100
        print("p_result(Sat+ve):",p_result)
        return p_result
    elif p_result < -100:
        p_result = -100
        print("p_result(Sat -ve):",p_result)
        return i_result 
    else :
        print("p_result :",p_result)
        return p_result

def I_in_PID(current_temp):
    if ((diff_log[0] > target) and (target > diff_log[1])) or ((diff_log[1] > target) and (target > diff_log[0])) or (diff_log[1] == target) :
       error_log[0] = 0
       error_log[1] = 0
       error_log[2] = 0
       error_log[3] = 0
       error_log[4] = 0
       error_log[5] = 0
       error_log[6] = 0
    i_result = (error_log[0]+error_log[1]+error_log[2]+error_log[3]+error_log[4]+error_log[5])*(100/6)
    if i_result > 100:
        i_result = 100
        print("i_result(Sat +ve):",i_result)
        return i_result
    elif i_result < -100:
        i_result = -100
        print("i_result(Sat -ve):",i_result)
        return i_result        
    else :
        print("i_result :",i_result)
        return i_result

def D_in_PID(current_temp):
    if ((diff_log[0] > target) and (target > diff_log[1])) or ((diff_log[1] > target) and (target > diff_log[0])) or (diff_log[1] == target) :
        d_result = 0
        print("d_result :",d_result)
        return d_result 
    elif (diff_log[0] > target) and (diff_log[1] > target) :
        if diff_log[1] < diff_log[0]:
            inst_slope = diff_log[1] - diff_log[0]
            expt_slope=((diff_log[1] - target)/math.exp(1/3)) + target - diff_log[1]
            if inst_slope < expt_slope:
                d_result = 100*(inst_slope - expt_slope)
                if d_result < -100:
                    d_result = -100
                    print("d_result :",d_result)
                    return d_result
                else :
                    print("d_result :",d_result)
                    return d_result
            else :
                d_result = 0
                print("d_result :",d_result)
                return d_result
        else :
            d_result = (diff_log[1]-diff_log[0])*100
            if d_result > 100:
                d_result = 100
                print("d_result :",d_result)
                return d_result
            else :
                print("d_result :",d_result)
                return d_result
    else :
        if diff_log[1] > diff_log[0]:
            inst_slope = diff_log[1] - diff_log[0]
            expt_slope=((diff_log[1] - target)/math.exp(1/3)) + target - diff_log[1]
            if inst_slope > expt_slope:
                d_result = 100*(inst_slope - expt_slope)
                if d_result > 100:
                    d_result = 100
                    print("d_result :",d_result)
                    return d_result
                else :
                    print("d_result :",d_result)
                    return d_result
            else :
                d_result = 0
                print("d_result :",d_result)
                return d_result
        else :
            d_result = (diff_log[1] - diff_log[0])*100
            if d_result < -100:
                d_result = -100
                print("d_result :",d_result)
                return d_result
            else :
                print("d_result :",d_result)
                return d_result        

diff_log[0] = cpu.temperature
diff_log[1] = diff_log[0]

for t in range(60):
    temperature = cpu.temperature
    error = current_temp - target
    error_log.append(error)
    del error_log[0]
    diff_log.append(temperature)
    del diff_log[0]
    output_to_PWM = P_in_PID(temperature) + I_in_PID(temperature) + D_in_PID(temperature)
    if output_to_PWM > 100 :
        power_output = 100
    elif output_to_PWM < 0 :
        power_output = 0
        #power_output = -100
    else :
        power_output = output_to_PWM
    pwm.ChangeDutyCycle(int(power_output))
    print("Current Temp:", temperature)
    print("Temperature Changed from ",diff_log[0]," to ",diff_log[1])
    print("Power to motor:",power_output)
    print()
    y.append(temperature)
    x.append(t)
    target_temp_graph.append(target)
    sleep(1)

pwm.stop()

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('CPU Temperature')
plt.grid(True)
plt.scatter(x,y)
plt.plot(x,y)
plt.plot(x,target_temp_graph)
plt.savefig("/home/pi/Documents/Graph/{0}.png".format(strftime("%Y_%m_%d_%H_%M_%S")))
    
    
