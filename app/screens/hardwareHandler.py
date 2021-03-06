import time
import serial

a_exist = False

def connect_arduino():
    try:
        a = serial.Serial('/dev/ttyACM0', 9600)
        a_exist = True
        return a
    except:
        pass

def asend(a, c):
    if (a == None):
        return
    a.write(c)
    
def areset(a):
    asend(a, 'asdfgkl;\'x')

def red_thruster(a, on_off):
    if (on_off):
        asend(a, 'q')
    else:
        asend(a, 'a')

def blue_thruster(a, on_off):
    if (on_off):
        asend(a, 'w')
    else:
        asend(a, 's')

def yellow_dome(a, on_off):
    if (on_off):
        asend(a, 'e')
    else:
        asend(a, 'd')

def white_dome(a, on_off):
    if (on_off):
        asend(a, 'r')
    else:
        asend(a, 'f')

def glass(a, on_off):
    if (on_off):
        asend(a, 't')
    else:
        asend(a, 'g')
    
def control_led(a, led_num, on_off):
    if (led_num == 1):
        if (on_off):
            asend(a, 'q')
        else:
            asend(a, 'a')
    elif (led_num == 2):
        if (on_off):
            asend(a, 'w')
        else:
            asend(a, 's')
    elif (led_num == 3):
        if (on_off):
            asend(a, 'e')
        else:
            asend(a, 'd')
    elif (led_num == 4):
        if (on_off):
            asend(a, 'r')
        else:
            asend(a, 'f')
    elif (led_num == 5):
        if (on_off):
            asend(a, 't')
        else:
            asend(a, 'g')

def door_fr(a, open_close):
    if (open_close):
        asend(a, 'i')
    else:
        asend(a, 'k')
    time.sleep(1)

def door_fl(a, open_close):
    if (open_close):
        asend(a, 'o')
    else:
        asend(a, 'l')
    time.sleep(1)

def door_br(a, open_close):
    if (open_close):
        asend(a, 'p')
    else:
        asend(a, ';')
    time.sleep(1)

def door_bl(a, open_close):
    if (open_close):
        asend(a, '[')
    else:
        asend(a, '\'')
    time.sleep(1)
    
def cont(a, dir):
    if (dir == 0):
        asend(a, 'x')
    elif (dir == 1):
        asend(a, 'z')
    elif (dir == 2):
        asend(a, 'c')    

def servo_pos_test(a, ang):
    a.write(str(ang))
    time.sleep(2)
    
def demo(a):
    door_bl(a, 1)
    for i in range(80, 0, -10):
        blue_thruster(a, 1)
        time.sleep(0.1)
        blue_thruster(a, 0)
        time.sleep(float(i)/100)
    red_thruster(a, 1)
    time.sleep(1)
    door_fl(a, 1)
    for i in range(0, 5):
        yellow_dome(a, 1)
        time.sleep(0.5)
        glass(a, 1)
        time.sleep(0.5)
        white_dome(a, 1)
        cont(a, (i%2)+1)
        time.sleep(1)
    time.sleep(1)
    cont(a, 0)
    white_dome(a, 0)
    areset(a)
