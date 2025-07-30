#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2,INPUT_4,INPUT_3
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor,ColorSensor
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent
from time import sleep
import time
import math
from ev3dev2.button import Button
from ev3dev2.led import Leds


rast = UltrasonicSensor(INPUT_2)
chap = UltrasonicSensor(INPUT_3)

door=4*3

# تنظیم پورت Pixy
pixy = Sensor(INPUT_1)
pixy.mode = 'ALL'

sig = pixy.value(1) * 256 + pixy.value(0)

# تعریف سنسور اولتراسونیک روی پورت 1
color_sensor = ColorSensor(INPUT_4)
motor_a = MediumMotor(OUTPUT_B)
motor_b = MediumMotor(OUTPUT_D)
motor_a.reset() 
motor_b.reset()

btn = Button()
leds = Leds()
leds.set_color('LEFT', 'ORANGE')
leds.set_color('RIGHT', 'ORANGE')


############btn.wait_for_bump('enter')
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
    green = 230
    red = 20
    rang=5
    rangdovom=2
else:
    al=1
    green = 230
    red = 5
    rang=2
    rangdovom=5

print(al)

cr1=color_sensor.color

lastsig=0
a_timer=0
b_timer=0
lastpos=0
fasele=35
ghabeliat=False

motor_a.on_for_seconds((-40)*al, 0.5)
motor_b.on_for_rotations(80,1)
motor_a.stop(stop_action='coast')
#motor_a.on_for_degrees(40,-motor_a.position)
sleep(0.2)
sig = pixy.value(1) * 256 + pixy.value(0) 

y = pixy.value(3) 

if y<75:
    sig=0

if al > 0 :
    if sig==0:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100),-motor_a.position)
        motor_b.on_for_rotations(60,1.5)
        
        

    elif (sig == 2 ) and y > 100:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((40),-motor_a.position)

        

        
    elif (sig==1 ) and y > 100 :
        motor_b.on_for_degrees(30,550)
        motor_a.on_for_seconds((40)*al, 0.5)
        motor_b.on_for_rotations(60,1.5)
        motor_a.on_for_degrees((40),-motor_a.position)
        motor_a.stop(stop_action='coast')
        motor_b.stop(stop_action='coast')
    
else:
    if sig==0:
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100)*al,60)
        motor_b.on_for_rotations(60,1.5)
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((100),motor_a.position)



    elif (sig == 1 ) and y > 100 :
        motor_a.stop(stop_action='coast')
        motor_a.on_for_degrees((40),-motor_a.position)
        

        
    elif (sig==2 ) and y > 100 :
        motor_b.on_for_degrees(30,550)
        motor_a.on_for_seconds((40)*al, 0.5)
        motor_b.on_for_rotations(60,1.5)
        motor_a.on_for_degrees((40),-motor_a.position)
        motor_a.stop(stop_action='coast')
        motor_b.stop(stop_action='coast')

sleep(0.5)
a=0
speed =20
بستنی= 2
a_timer=0

while True:

    cr1=color_sensor.color


    print(a)
    
    sig = pixy.value(1) * 256 + pixy.value(0) 
    x = pixy.value(2)
    y = pixy.value(3) 
    size = pixy.value(4)
    motor_b.on(speed)

    
    if sig!=0:
        
        lastsig=sig
        if y<75:
            sig=0
        







    if  cr1 == rang:
            fasele=25

            cr1=color_sensor.color
            sig = pixy.value(1) * 256 + pixy.value(0)
            if y<75:
                sig=0
            if a ==door-1: 
                break 
            if sig == 0:
               # motor_b.off()
               # motor_a.on_for_degrees((100)*al, -80)
               # motor_b.on_for_degrees((50),150)

               # motor_b.off()
               # motor_a.on_for_degrees((100)*al, 160)
               # motor_b.on_for_degrees((-50),190)

                #motor_a.stop(stop_action='coast')
                #motor_b.stop(stop_action='coast')
                #motor_a.on_for_degrees((90),-motor_a.position)
                #motor_b.on_for_rotations(100,1)
                #motor_b.off()
                #motor_a.off()

               # sleep(0.4)
                timeRang=time.time()
                navakht=-40
                while cr1!=rangdovom and sig==0 and time.time()-timeRang <4:
                    amotor(navakht*al)
                    if navakht<=0:
                        navakht=navakht+1

                    cr1=color_sensor.color
                    sig = pixy.value(1) * 256 + pixy.value(0)
                    if y<75:
                        sig=0
                    #print(time.time()-timeRang )
                    motor_b.on(20)
                    cr1=color_sensor.color
                    
                timeRang=time.time()
                while time.time()-timeRang <0.7 and sig ==0:
                    amotor(-20*al)
                    sig = pixy.value(1) * 256 + pixy.value(0)
                    if y<75:
                        sig=0
                    motor_b.on((70))

            if a_timer==0 or time.time()-a_timer>4:
                a_timer=time.time()
                a=a+1
            cr1=color_sensor.color
            fasele = 35
            





    
   


    
    if y<110 and (sig==1):
        cr1=color_sensor.color
        leds.set_color('LEFT', 'GREEN')
        leds.set_color('RIGHT', 'GREEN')
        target=(x-120)*0.7
        target=clamp(target,-20,20)
        amotor(target,35)
        speed = 40




    elif y<110 and (sig==2):
        cr1=color_sensor.color
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')
        target=(x-100)*0.7
        target=clamp(target,-20,20)
        amotor(target,35)
        speed = 40


    elif sig == 1 :
         ghabeliat=True
         
         target=(x-green)*0.5
         leds.set_color('LEFT', 'GREEN')
         leds.set_color('RIGHT', 'GREEN')
         amotor(target,50)
         speed=22

    elif sig ==2:
         ghabeliat=True
         
         
         target=(x-red)*0.5
         leds.set_color('LEFT', 'RED')
         leds.set_color('RIGHT', 'RED')
         amotor(target,50)
         speed =22
        
    elif sig==0 and ghabeliat and False:
        if al < 0 and lastsig==1:
                motor_b.on_for_rotations(60,0.9)

                motor_b.off()
                motor_a.on_for_degrees((40),-motor_a.position)
                motor_a.on_for_degrees((40),30*al)
                motor_b.on_for_rotations(60,0.6)


        elif al >0 and lastsig==2:

                motor_b.on_for_rotations(60,0.9)

                motor_b.off()
                motor_a.on_for_degrees((40),-motor_a.position)
                motor_a.on_for_degrees((40),-30*al)   
                motor_b.on_for_rotations(60,0.6)

        else :
            pass


        ghabeliat=False
        




    
    elif sig == 0 and cr1==6:
        leds.all_off()
        speed = 33
        r=rast.distance_centimeters
        c=chap.distance_centimeters
        if al==1:
            oltra=c
        else:
            oltra=r  
        out= (fasele-oltra) *al
        out=clamp(out,-45,45)
        amotor(out)

    if lastsig ==2 and al>0 and sig ==0 :
        fasele =50


    if lastsig == 1 and al<0 and sig ==0 :
        fasele =50
        


    if fasele>33:
        
        fasele=fasele-0.09
    else: 
        fasele=33
   # print(fasele)
################################################


    
    if lastpos==motor_b.position:
        if b_timer==0:
            b_timer=time.time()
        #print(time.time()-b_timer)
        if time.time()-b_timer>0.3:
            print("khokafez")
            b_timer=0
            motor_a.on_for_degrees((40),-motor_a.position)
            motor_b.on_for_rotations(-100,1)

            motor_a.on_for_degrees((40),45*al)
            motor_b.on_for_rotations(100,0.8)



    lastpos=motor_b.position    
######################################
    if a==door:
        break
motor_a.off()
motor_b.off()
cr1=color_sensor.color



if al<0:
    navakht=90
    while cr1!=rangdovom :
        motor_b.on(30)
        amotor(0)
        if navakht<=0:
            navakht=navakht+1

        cr1=color_sensor.color
    motor_b.off()
    motor_a.on_for_degrees((100), -120)
    motor_b.on_for_degrees((-30),300)

    motor_b.off()
    #motor_a.on_for_degrees((100)*al, 190)
    #motor_b.on_for_degrees((-30),220)


    motor_a.on_for_degrees((90),-motor_a.position)
    #motor_b.on_for_rotations(30,0.2)
    motor_b.off()
    motor_a.off()

    speed=8

    while True:
        leds.all_off()
        motor_b.on(speed)
        cr1=color_sensor.color

        r=rast.distance_centimeters
        if r<60 or cr1==rangdovom:
            break
    fasele=15
    speed=20
    timerse=time.time()
    motor_b.off()

    motor_b.reset()
 
    while motor_b.position<1500:
        leds.all_off()
        motor_b.on(speed)
        r=rast.distance_centimeters
        out= (fasele-r)*1.5 *al
        out=clamp(out,-23,23)
        amotor(out)




    motor_b.off()

    motor_a.on_for_degrees((90),-motor_a.position)

    motor_b.on_for_rotations(-20,0.6)
   
    motor_b.off()
    cr1=color_sensor.color
    motor_a.on_for_degrees((90),-90)

    
    motor_b.on_for_rotations(-20,1.72)
    motor_a.on_for_degrees((90),-motor_a.position)
    motor_a.off()
    i=0
    while i<=50:
        amotor(0)
        i=i+1
    motor_a.off()

    motor_b.on_for_rotations(-20,3.5)

    motor_b.off()

    motor_a.on_for_degrees((90),90)
    motor_b.on_for_rotations(20,0.7)
    motor_b.off()

    motor_a.on_for_degrees((90),-190)
    motor_b.on_for_rotations(-20,0.6)
    motor_b.off()
    motor_a.on_for_degrees((90),190)

    motor_b.on_for_rotations(20,0.4)

while True:
    amotor(0)
    motor_b.off()

    



    





    
motor_b.off()
motor_a.off()





        
        