from machine import Pin, PWM
from time import sleep

p1  =  PWM(Pin(0))
p2  =  PWM(Pin(1))
p3  =  PWM(Pin(2))
p4  =  PWM(Pin(3))
p5  =  PWM(Pin(4))
p6  =  PWM(Pin(5))
p7  =  PWM(Pin(6))
p8  =  PWM(Pin(7))
p9  =  PWM(Pin(8))
p10 =  PWM(Pin(9))
p11 = PWM(Pin(10))
p12 = PWM(Pin(11))

#Inicia la secuencia de encendido de led's
p1.freq( 144)
p3.freq( 144)
p2.freq( 144)
p4.freq( 144)
p5.freq( 144)
p6.freq( 144)
p7.freq( 144)
p8.freq( 144)
p9.freq( 144)
p10.freq(144)
p11.freq(144)
p12.freq(144)

def parpadeoLento():
    while True:
        v1 = 65025
        band1 = 0
        for duty in range(0, 130050, +25):
            if duty <= 65025 and band1 == 0:
                p1.duty_u16( duty)
                p2.duty_u16( duty)
                p3.duty_u16( duty)
                p4.duty_u16( duty)
                p5.duty_u16( duty)
                p6.duty_u16( duty)
                p7.duty_u16( duty)
                p8.duty_u16( duty)
                p9.duty_u16( duty)
                p10.duty_u16(duty)
                p11.duty_u16(duty)
                p12.duty_u16(duty)
                sleep(0.001)
                # print(duty)
            else: 
                band1 = 1 
                v1 = v1 - 25 
                p1.duty_u16( v1)
                p2.duty_u16( v1)
                p3.duty_u16( v1)
                p4.duty_u16( v1)
                p5.duty_u16( v1)
                p6.duty_u16( v1)
                p7.duty_u16( v1)
                p8.duty_u16( v1)
                p9.duty_u16( v1)
                p10.duty_u16(v1)
                p11.duty_u16(v1)
                p12.duty_u16(v1)
                sleep(0.001)
                # print(v1)

def prueba():
    p1.duty_u16( 65025)
    p2.duty_u16( 65025)
    p3.duty_u16( 65025)
    p4.duty_u16( 65025)
    p5.duty_u16( 65025)
    p6.duty_u16( 65025)
    p7.duty_u16( 65025)
    p8.duty_u16( 65025)
    p9.duty_u16( 65025)
    p10.duty_u16(65025)
    p11.duty_u16(65025)
    p12.duty_u16(65025)