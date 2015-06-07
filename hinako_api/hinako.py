#!/usr/bin/env python
import math
import time
from pyfirmata import Arduino, util

class Hinako:

    def __init__(self, port, b_pin_id, w_pin_id, h_pin_id):
        self.board = Arduino(port)
        
        '''
        d: digital output
        n: number PWM pin
        s: servo control
        '''
        self.b_pin = self.board.get_pin(b_pin_id)
        self.w_pin = self.board.get_pin(w_pin_id)
        self.h_pin = self.board.get_pin(h_pin_id)

        self.b = 0
        self.w = 0
        self.h = 0

    def _move_servo(self, pin, begin_val, end_val, ds=0.1):
        step = 1 if begin_val < end_val else -1

        print '%d -> %d' % (begin_val, end_val)
        print step

        for i in range(begin_val, end_val, step):
            pin.write(i)
            time.sleep(ds)

    def set_bust(self, size_cm):
        print "bust: %d cm" % size_cm
        val = int(round(map_value(size_cm, 70, 90, 60, 20)))
        self._move_servo(self.b_pin, self.w, val)
        self.w = val
        
    def set_waist(self, val):
        '''
        dc motor
        self.w_pin
        '''

    def set_hip(self, val):
        self._move_servo(self.h_pin, self.h, val)
        self.h = val

def map_value(value, begin1, end1, begin2, end2):
    return begin2 + (end2 - begin2) * ((value - begin1) / float(end1 - begin1));


if __name__ == '__main__':
    print map_value(50, 0, 100, 0, 255)
    print map_value(50, 0, 100, 255, 0)


    port = '/dev/cu.usbmodemfd121'
    hinako = Hinako(port, 'd:3:s', 'd:4:s', 'd:5:s')

    # 70-80
    hinako.set_bust(90)
    # hinako.set_waist(127)
    # hinako.set_hip(127)
