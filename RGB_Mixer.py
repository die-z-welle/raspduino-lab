#!/usr/bin/env python
# RGB LED dimmer test
# Russell Barnes - 04 Sept 2013 (Updated 19th November for issue 134 of Linux User magazine).

#  Copyright 2013 Imagine Publishing Ltd.

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


from nanpy import Arduino
from time import sleep

# set LED pin numbers - these go to the Digital pins of your Arduino
redPin = 3
greenPin = 6
bluePin = 9

# set pot pin numbers - these go to the (A)nalog pins of your Arduino
pot_r_Pin = 0
pot_g_Pin = 3
pot_b_Pin = 5

#set three coloured pins as outputs
for pins in (redPin, greenPin, bluePin):
        Arduino.pinMode(pins, Arduino.OUTPUT)

# set pot pins as inputs
for pins in (pot_r_Pin, pot_g_Pin, pot_b_Pin):
        Arduino.pinMode(pins, Arduino.INPUT)

# prints values to the terminal when True
debug = False

def get_pots():
        """
        Grab a reading from each of the pot pins and 
        send it to a tuple to be read by the colour mixer
        """
        r = Arduino.analogRead(pot_r_Pin) / 4
        Arduino.delay(1)
        g = Arduino.analogRead(pot_g_Pin) / 4
        Arduino.delay(1)
        b = Arduino.analogRead(pot_b_Pin) / 4
        Arduino.delay(1)
        return r, g, b

def colour_mixing():
        """
        Call get_pots() and set 
        the colour pins accordingly
        """
        r, g, b = get_pots()
        Arduino.analogWrite(redPin, r)
        Arduino.analogWrite(greenPin, g)
        Arduino.analogWrite(bluePin, b)
        Arduino.delay(1)

def close_pins():
        """
        Close pins to quit cleanly (doesn't work with a 'for
        loop' despite the pins happily initialising that way!)
        """
        Arduino.digitalWrite(redPin,Arduino.LOW)
        Arduino.digitalWrite(greenPin,Arduino.LOW)
        Arduino.digitalWrite(bluePin,Arduino.LOW)

def main():
        """
        Mix the colours using three pots. 
        Ctrl+C cleans up the pins on exit.
        """
        try:
                print "Adjust the pots to change the colours"
                while True:
                        colour_mixing()
                        sleep(0.2)
                        if debug:
                                print "Red: {:d} | Green: {:d} | Blue: {:d}".format(r, g, b)
        except KeyboardInterrupt:
                close_pins()
                print "\nPins closed"

if __name__ == '__main__':        
        main()