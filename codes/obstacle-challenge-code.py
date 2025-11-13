#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2,INPUT_4,INPUT_3
from ev3dev2.sensor import Sensor, INPUT_1
from smbus import SMBus
from ev3dev2.sensor.lego import UltrasonicSensor,ColorSensor
from ev3dev2.port import LegoPort
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent

from time import sleep
import time
import math
from ev3dev2.button import Button
from ev3dev2.led import Leds


rast = UltrasonicSensor(INPUT_2)
chap = UltrasonicSensor(INPUT_3)


door=12

# تنظیم پورت Pixy
pixy = LegoPort(INPUT_1)
pixy.mode = 'other-i2c'
address = 0x54  
bus = SMBus(3)     # برای in1

global block
global a
a = 0




color_sensor = ColorSensor(INPUT_4)
motor_a = MediumMotor(OUTPUT_B)
motor_b = MediumMotor(OUTPUT_D)
motor_a.reset() 
motor_b.reset()

btn = Button()
leds = Leds()
leds.set_color('LEFT', 'ORANGE')
leds.set_color('RIGHT', 'ORANGE')


#btn.wait_for_bump('enter')
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'GREEN')





def clamp(value, minimum, maximum):
    if value > maximum : value=maximum
    if value < minimum : value=minimum
    return value

def amotor(degrese,cl=50):
        diff =degrese

        diff=(diff-motor_a.position)*0.7

        motor_a.on(clamp(diff,-cl,cl))
        motor_a
def get_block(type):

    if type == "sig":
        export = block[7] << 8 | block[6]
    elif type == "x":
        export = block[9] << 8 | block[8]
    elif type == "y":
        export = block[11] << 8 | block[10]
    # اگه همه صفر باشن یعنی چیزی پیدا نشده
    if  block[7] << 8 | block[6]> 7 or block[9] << 8 | block[8]>3000 or block[11] << 8 | block[10] >3000 :
        return 0
    return (export)

def lineChek():
    global a

    cr1=color_sensor.color

    if (motor_b.position>1400  and  (cr1 == 1 or cr1 ==5 or cr1==2 )) or (a==0 and(cr1 == 1 or cr1 ==5 or cr1==2 )):
        
        a=a+1
        motor_b.reset()


p=0
jahat=0
sleep(0.2)
while p!= 100:
    r=rast.distance_centimeters
    c=chap.distance_centimeters
    if r>c : jahat=1+jahat
    else:jahat=jahat-1
    print(jahat)
    p=p+1

al=0
if jahat>0 :
    al=-1
    green = 245
    red = 75
    rang=[5,5]
    rangdovom=[2,1]
else:
    al=1
    green = 245
    red = 65
    rang=[1,2]
    rangdovom=[5,5]

print(al)

cr1=color_sensor.color

lastsig=0
a_timer=0
b_timer=0
lastpos=0
fasele=40
ghabeliat=False
Yignor=50

motor_a.on_for_seconds((-40)*al, 0.5)
motor_b.on_for_rotations(80,1)
motor_a.stop(stop_action='coast')


data = [174, 193, 32, 2, 3, 5]
bus.write_i2c_block_data(address, 0, data)
sleep(0.5)

block = bus.read_i2c_block_data(address, 0, 20)


sleep(0.5)

sig = get_block("sig")

y = get_block("y")
print("siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiig")
print(sig)
if y<Yignor:
    sig=0

if al > 0 :
    if sig==0:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100)*al,60)
        motor_b.on_for_rotations(60,1.5)
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100),-motor_a.position)
        
    
    elif (sig == 2 ) and y > Yignor:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((40),-motor_a.position)

        

        
    elif (sig==1 ) and y > Yignor :
        motor_b.on_for_degrees(30,430)
        motor_a.on_for_seconds((40), 0.5)
        motor_b.on_for_rotations(60,1.8)
        motor_a.on_for_degrees((40),-motor_a.position)
        motor_a.stop(stop_action='coast')
        motor_b.stop(stop_action='coast')
    
else:
    if sig==0:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100)*al,60)
        motor_b.on_for_rotations(60,1.5)
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100),-motor_a.position)



    elif (sig == 1 ) and y > Yignor :
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((40),-motor_a.position)
        

        
    elif (sig==2 ) and y > Yignor :
        motor_b.on_for_degrees(30,550)
        motor_a.on_for_seconds((40)*al, 0.5)
        motor_b.on_for_rotations(60,1.5)
        motor_a.on_for_degrees((40),-motor_a.position)
        motor_a.stop(stop_action='coast')
        motor_b.stop(stop_action='coast')

sleep(0.5)
speed =45
a_timer=0
motor_b.reset()

data = [174, 193, 32, 2, 3, 5]
while True:             



    bus.write_i2c_block_data(address, 0, data)


    block = bus.read_i2c_block_data(address, 0, 20)



    print(a)
    
    sig = get_block("sig") 
    y = get_block("y")
    if y<Yignor:
        sig=0
    x = get_block("x")
    motor_b.on(speed)

    
    if sig!=0:
        
        lastsig=sig



    cr1=color_sensor.color
        
    if  (cr1 == rang[0] or cr1== rang[1] )and a !=door :

            cr1=color_sensor.color
            sig = get_block("sig")
            y = get_block("y")

            if y<Yignor:
                sig=0
 
            if sig == 0  :
                
                timeRang=time.time()
                navakht=-45
                while cr1!=rangdovom[0]and cr1!=rangdovom[1]  and sig==0 and time.time()-timeRang <4 and a<door-1 :  
                    
                    lineChek()

                    bus.write_i2c_block_data(address, 0, data)
                    block = bus.read_i2c_block_data(address, 0, 20)


                    


                    motor_a.stop(stop_action='coast')
                    amotor(navakht*al)
                    if navakht<=15:
                        navakht=navakht+3.9
                    print(navakht)    

                    cr1=color_sensor.color
                    sig = get_block("sig")
                    y = get_block("y")
                    if y<Yignor:
                        sig=0
                    if sig != 0 :
                        break

                    motor_b.on(20)
                    cr1=color_sensor.color
                    
                timeRang=time.time()
                while time.time()-timeRang <0.5 and sig ==0:


                    lineChek()
                    
                    bus.write_i2c_block_data(address, 0, data)
                    block = bus.read_i2c_block_data(address, 0, 20)



                    amotor(0)
                    sig = get_block("sig")
                    y = get_block("y")

                    if y<Yignor:
                        sig=0
                    if sig != 0 :
                        print("khar22")
                        break

                    motor_b.on((70))


            cr1=color_sensor.color
            fasele = 45

    lineChek()
            
    
    if y<70 and (sig!=0):
        leds.set_color('LEFT', 'ORANGE')
        leds.set_color('RIGHT', 'ORANGE')
        target=(x-165)*0.7
        target=clamp(target,-20,20)
        amotor(target,35)
        speed = 40






    elif sig == 1 :
         
         target=(x-green)*0.5
         leds.set_color('LEFT', 'GREEN')
         leds.set_color('RIGHT', 'GREEN')
         amotor(target,45)
         speed=40

    elif sig ==2:
         
         
         target=(x-red)*0.5
         leds.set_color('LEFT', 'RED')
         leds.set_color('RIGHT', 'RED')
         amotor(target,45)
         speed =40
        
   
        
    elif sig == 0 and cr1==6:
        leds.all_off()
        speed = 40
        r=rast.distance_centimeters
        c=chap.distance_centimeters
        if al==1:
            oltra=c
        else:
            oltra=r  
        out= (fasele-oltra) *al
        out=clamp(out,-45,45)
        amotor(out)

    lineChek()



    if lastsig ==2 and al>0 and sig ==0 :
        fasele =55


    if lastsig == 1 and al<0 and sig ==0 :
        fasele =55
        


    if fasele>40:
        
        fasele=fasele-0.09
    else: 
        fasele=40


    
    if lastpos==motor_b.position:
        if b_timer==0:
            b_timer=time.time()
        if time.time()-b_timer>0.3:
            print("khokafez")
            b_timer=0
            motor_a.on_for_degrees((40),-motor_a.position)
            motor_b.on_for_rotations(-100,1)

            motor_a.on_for_degrees((40),45*al)
            motor_b.on_for_rotations(100,0.8)



    lastpos=motor_b.position    

    if a==door:
        break
motor_a.off()
motor_b.off()
cr1=color_sensor.color



if al<0:
    navakht=40
    while cr1!=rangdovom[0] and cr1!=rangdovom[1]:
        motor_b.on(12)
        amotor(0)
        if navakht>=-20:
            navakht=navakht-1

        cr1=color_sensor.color

    motor_b.stop()
    sleep(0.1)

    motor_a.on_for_degrees((90),90)


    motor_b.on_for_degrees((30),-350)




    cr1=color_sensor.color
    sleep(0.1)


  

    motor_a.stop()
    motor_b.stop()
    out=0
    
    while cr1!=rangdovom[0] and cr1!=rangdovom[1]:
        motor_b.on(16)
        amotor(0)
        cr1=color_sensor.color


    motor_a.on_for_degrees((90),-motor_a.position)



    r=rast.distance_centimeters

    timeRang=time.time()
    speed=10
    out=0
    while r>5 and time.time() - timeRang < 8:
        print(r)
        r=rast.distance_centimeters

        cr1=color_sensor.color
        if cr1==6:
            out=-60              ##################### line follwo
        else:
            out=20
        amotor(out)
        motor_b.on(speed)
    print(r)
    motor_b.stop()
    motor_b.stop(stop_action='coast')

    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60),-motor_a.position)
    motor_a.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((-60), 150)
    motor_a.stop()

    motor_b.on_for_degrees((-30), 1100)
    motor_a.on_for_degrees((60), 150)
    motor_b.on_for_degrees((-20), 260)

    motor_b.stop()
    sleep(0.1)
    motor_a.stop(stop_action='coast')

    motor_a.on_for_degrees((30), -motor_a.position)


    motor_a.stop()


    motor_b.on_for_degrees((30), 700)


    fasele = 30
    c=chap.distance_centimeters
    motor_b.reset()
    speed = 15
    sig = 3
    timersig=0
    khorog=True
    sleep(0.03)
    while khorog :
        motor_b.on(speed)
        data = [174, 193, 32, 2, 4, 5]
        sleep(0.02)
        bus.write_i2c_block_data(address, 0, data)
        block = bus.read_i2c_block_data(address, 0, 20)
        sig = get_block("sig")
        c=chap.distance_centimeters 
        print(time.time()-timersig)
        if c <= fasele - 1:
            out = 27
        elif c >= fasele + 1:
            out = -27          ############### waaaaallll
        else:
            out = 0
        amotor(out)

        motor_b.on(speed)

        if sig!=3 and timersig==0:
            timersig=time.time()
        elif sig ==3:
            timersig=0


        if time.time()-timersig > 0.3 and timersig!=0 :
            print("print")
            khorog=False   

    motor_b.reset()
    motor_a.on_for_degrees((90), -motor_a.position)

    while motor_b.position < 195:
        motor_b.on(10)
        c=chap.distance_centimeters 
        print(sig)
        if c <= fasele - 1:
            out = 20
        elif c >= fasele + 1:
            out = -20              ############### waaaaallll
        else:
            out = 0
        amotor(out)
        motor_b.on(speed)

    motor_b.stop()
    motor_a.stop()
    motor_a.stop(stop_action='coast')




    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), -150)
    motor_a.stop()

    motor_b.on_for_degrees((-20), 500)
    motor_b.stop()
    motor_a.stop(stop_action='coast')

    motor_a.on_for_degrees((60), -motor_a.position)
    motor_a.stop()


    motor_b.reset()
    mp=0
    while mp > -530:
        motor_b.on(-15)
        mp = motor_b.position
        amotor((mp * -0.37))
        print(mp)
    print("dar ovordam")
    motor_b.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), -motor_a.position)
    motor_a.stop()
    sleep(1)



    

elif al > 0:
    navakht=40
    while cr1!=rangdovom[0] and cr1!=rangdovom[1]:
        motor_b.on(12)
        amotor(0)
        if navakht>=-20:
            navakht=navakht-1

        cr1=color_sensor.color

    motor_b.stop()
    sleep(0.1)

    motor_a.on_for_degrees((-90),90)


    motor_b.on_for_degrees((30),-290)




    cr1=color_sensor.color
    sleep(0.1)


  

    motor_a.stop()
    motor_b.stop()
    out=0
    
    while cr1!=rangdovom[0] and cr1!=rangdovom[1]:
        motor_b.on(16)
        amotor(0)
        cr1=color_sensor.color


    motor_a.on_for_degrees((90),-motor_a.position)



    c=chap.distance_centimeters

    timeRang=time.time()
    speed=10
    out=0
    while c>5 and time.time() - timeRang < 8:
        print(r)
        c=chap.distance_centimeters

        cr1=color_sensor.color
        if cr1==6:
            out=60           ##################### line follwo
        else:
            out=-20
        amotor(out)
        motor_b.on(speed)
    print(r)
    motor_b.stop()
    motor_b.stop(stop_action='coast')

    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60),-motor_a.position)
    motor_a.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), 150)
    motor_a.stop()

    motor_b.on_for_degrees((-50), 500)
    motor_b.stop()
    sleep(0.1)
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), -300)
    motor_a.stop()

    motor_b.on_for_degrees((50), 500)
    motor_b.stop()

    fasele = 34
    r=rast.distance_centimeters
    motor_b.reset()
    speed = 15

    while motor_b.position < 1500:
        r=rast.distance_centimeters 
        print(r)
        if r <= fasele - 1:
            out = -35
        elif r >= fasele + 1:
            out = 35              ############### waaaaallll
        else:
            out = 0
        amotor(out)
        motor_b.on(speed)

    print(r)
    motor_a.stop()
    motor_b.stop()
    sleep(1)
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), -300)
    motor_a.stop()

    motor_b.on_for_degrees((25), 550)
    motor_b.stop()
    sleep(0.2)
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), 80)
    motor_a.stop()
    sleep(0.2)

    motor_b.on_for_degrees((-15), 450)
    motor_b.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), 150)
    motor_a.stop()

    motor_b.on_for_degrees((-15), 670)
    motor_b.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60), -300)
    motor_a.stop()

    motor_b.on_for_degrees((15), 121)
    motor_b.stop()
    motor_a.stop(stop_action='coast')
    motor_a.on_for_degrees((60),-motor_a.position)


motor_b.off()
motor_a.off()