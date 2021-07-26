# Este es el codigo de Tlaloc-Sys
# Es para el manejos de leds en PC's
# Creador por el: Ing. Erick Paul García Ramírez
# México, Puebla. 18 de Julio de 2021
#
#

from rutinasLed import parpadeoLento, prueba
from machine import Pin, PWM
from time import sleep

#Declaración de variables 
l0  = Pin(25, Pin.OUT) #Led que se encuentra en la placa3
l0.on()

# while True:
#     for duty in range(0, 65025, +25):
#         p1.duty_u16(duty)
#         p2.duty_u16(duty)
#         p3.duty_u16(duty)
#         p4.duty_u16(duty)
#         p5.duty_u16(duty)
#         p6.duty_u16(duty)
#         p7.duty_u16(duty)
#         p8.duty_u16(duty)
#         p9.duty_u16(duty)
#         p10.duty_u16(duty)
#         p11.duty_u16(duty)
#         p12.duty_u16(duty)
#         sleep(0.001)
        
#     for duty in range(65025, 0, -25):
#         p1.duty_u16(duty)
#         p2.duty_u16(duty)
#         p3.duty_u16(duty)
#         p4.duty_u16(duty)
#         p5.duty_u16(duty)
#         p6.duty_u16(duty)
#         p7.duty_u16(duty)
#         p8.duty_u16(duty)
#         p9.duty_u16(duty)
#         p10.duty_u16(duty)
#         p11.duty_u16(duty)
#         p12.duty_u16(duty)
#         sleep(0.001)

parpadeoLento()
