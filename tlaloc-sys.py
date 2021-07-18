# Este es el codigo de Tlaloc-Sys
# Es para el manejos de leds en PC's
# Creador por el: Ing. Erick Paul García Ramírez
# México, Puebla. 18 de Julio de 2021
#
#

from machine import Pin
import time

l0  = Pin(25, Pin.OUT) #Led que se encuentra en la placa
l1  = Pin(0 , Pin.OUT)
l2  = Pin(1 , Pin.OUT)
l3  = Pin(2 , Pin.OUT)
l4  = Pin(3 , Pin.OUT)
l5  = Pin(4 , Pin.OUT)
l6  = Pin(5 , Pin.OUT)
l7  = Pin(6 , Pin.OUT)
l8  = Pin(7 , Pin.OUT)
l9  = Pin(8 , Pin.OUT)
l10 = Pin(9 , Pin.OUT)
l11 = Pin(10, Pin.OUT)
l12 = Pin(11, Pin.OUT)

#Inicia la secuencia de encendido de led's
l0.on()
l1.on()
l2.on()
l3.on()
l4.on()
l5.on()
l6.on()
l7.on()
l8.on()
l9.on()
l10.on()
l11.on()
l12.on()


