# Este es el codigo de Tlaloc-Sys
# Es para el manejos de leds en PC's
# Creador por el: Ing. Erick Paul García Ramírez
# México, Puebla. 18 de Julio de 2021
#
#

from machine import Pin, PWM
from time import sleep


#Declaración de variables 
l0  = Pin(25, Pin.OUT) #Led que se encuentra en la placa3
# l1  = Pin(0 , Pin.OUT)
# l2  = Pin(1 , Pin.OUT)
# l3  = Pin(2 , Pin.OUT)
# l4  = Pin(3 , Pin.OUT)
# l5  = Pin(4 , Pin.OUT)
# l6  = Pin(5 , Pin.OUT)
# l7  = Pin(6 , Pin.OUT)
# l8  = Pin(7 , Pin.OUT)
# l9  = Pin(8 , Pin.OUT)
# l10 = Pin(9 , Pin.OUT)
# l11 = Pin(10, Pin.OUT)
# l12 = Pin(11, Pin.OUT)

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
p1.freq( 800)
p3.freq( 800)
p2.freq( 800)
p4.freq( 800)
p5.freq( 800)
p6.freq( 800)
p7.freq( 800)
p8.freq( 800)
p9.freq( 800)
p10.freq(800)
p11.freq(800)
p12.freq(800)

while True:
    for duty in range(0, 65025, +15):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        p3.duty_u16(duty)
        p4.duty_u16(duty)
        p5.duty_u16(duty)
        p6.duty_u16(duty)
        p7.duty_u16(duty)
        p8.duty_u16(duty)
        p9.duty_u16(duty)
        p10.duty_u16(duty)
        p11.duty_u16(duty)
        p12.duty_u16(duty)
        sleep(0.0001)
        
    for duty in range(65025, 0, -15):
        p1.duty_u16(duty)
        p2.duty_u16(duty)
        p3.duty_u16(duty)
        p4.duty_u16(duty)
        p5.duty_u16(duty)
        p6.duty_u16(duty)
        p7.duty_u16(duty)
        p8.duty_u16(duty)
        p9.duty_u16(duty)
        p10.duty_u16(duty)
        p11.duty_u16(duty)
        p12.duty_u16(duty)
        sleep(0.0001)

l0.on()
# l1.on()
# l2.on()
# l3.on()
# l4.on()
# l5.on()
# l6.on()
# l7.on()
# l8.on()
# l9.on()
# l10.on()
# l11.on()
# l12.on()


