#Create a simple GUI with multiple PushButtons in a window and implement password portection for one of the GUI buttons

from guizero import App, TextBox, PushButton, Text, Window, Picture
from time import strftime, time

def update_time():
    p_t_t.set(strftime("%H : %M : %S"))

#Password window:
#open_password_window
def o_pass_w():
    p_w.show()
#close_app
def close_app():
    password_input = i_tb.get()
    if password_input == '0000':
        app.destroy()
    else:
        e_w.show()
#PIN_input
def p1():
    i_tb.append('1')
def p2():
    i_tb.append('2')
def p3():
    i_tb.append('3')
def p4():
    i_tb.append('4')
def p5():
    i_tb.append('5')
def p6():
    i_tb.append('6')
def p7():
    i_tb.append('7')
def p8():
    i_tb.append('8')
def p9():
    i_tb.append('9')
def p0():
    i_tb.append('0')
def clear():
    i_tb.clear()

app = App(title = 'Display Console', layout= "grid")
app.tk.attributes("-fullscreen",True)

#Main_main_window:
#main_menu_button
m_m_b = PushButton(app, text="Main\nMenu", grid=[0,0], height= 5, width=10)
#clock_set_button
c_s_b = PushButton(app, text="Clock\nSet", grid=[0,1], height= 5, width=10)
#setup_button
s_b = PushButton(app, text="Setup", grid=[0,2], height= 5, width=10)
#blank_button_1
b_b_1 = PushButton(app, text="blank\nbutton", grid=[0,3], height= 5, width=10)
#present_date_text
p_d_t = Text(app, text=strftime("%d  /  %m  /  %Y"), grid=[1,0,3,1], height= "fill", width="fill")
#present_time_text
p_t_t = Text(app, text=strftime("%H : %M : %S"), grid=[1,1,3,1], height= "fill", width="fill")
p_t_t.repeat(1000,update_time)
#company_logo_picture
c_l_p = Picture(app, grid=[1,2,3,2], height=200, width=300)
#service_menu_button
s_m_b = PushButton(app, text="Service\nMenu", grid=[4,0], height= 5, width=10)
#prime_button
p_b = PushButton(app, text="Prime", grid=[4,1], height= 5, width=10)
#program_button
pro_b = PushButton(app, text="Program", grid=[4,2], height= 5, width=10)
#app_close_button
a_c_b = PushButton(app, text="Close", command= o_pass_w, grid=[4,3], height= 5, width=10)


#Password_window:
p_w = Window(app, title='Enter the password:', width=165, height= 220, layout= "grid", visible=False)
#input_TextBox
i_tb = TextBox(p_w, grid=[0,0,3,1])
#confirm_close_button
c_c_b = PushButton(p_w, text="Enter", command=close_app, grid=[3,0])
#Digit_0_to_9_button
b_1 = PushButton(p_w, text="1", command=p1, grid=[0,1])
b_2 = PushButton(p_w, text="2", command=p2, grid=[1,1])
b_3 = PushButton(p_w, text="3", command=p3, grid=[2,1])
b_4 = PushButton(p_w, text="4", command=p4, grid=[0,2])
b_5 = PushButton(p_w, text="5", command=p5, grid=[1,2])
b_6 = PushButton(p_w, text="6", command=p6, grid=[2,2])
b_7 = PushButton(p_w, text="7", command=p7, grid=[0,3])
b_8 = PushButton(p_w, text="8", command=p8, grid=[1,3])
b_9 = PushButton(p_w, text="9", command=p9, grid=[2,3])
blank_text1= Text(p_w, text='', grid=[0,4])                      
b_0 = PushButton(p_w, text="0", command=p0, grid=[1,4])
blank_text2= Text(p_w, text='', grid=[2,4])
#Clear_TextBox_button
c_tb_b = PushButton(p_w, text="Clear", command=clear, grid=[3,4])


#Error_window:
e_w = Window(app, title='Error', width=160, height= 90, visible=False)
#Error_text
e_t = Text(e_w, text= 'Incorrect Password')


app.display()
