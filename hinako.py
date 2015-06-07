#!/usr/bin/env python
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

        self.b_pin_id = b_pin_id
        self.w_pin_id = w_pin_id
        self.h_pin_id = h_pin_id

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

    def set_bust(self, val):
        pin = self.board.get_pin(self.b_pin_id)
        self._move_servo(pin, self.w, val)
        self.w = val
        
    def set_waist(self, val):
        pin = self.board.get_pin(self.w_pin_id)
        # dc motor

    def set_hip(self, val):
        pin = self.board.get_pin(self.h_pin_id)        
        self._move_servo(pin, self.h, val)
        self.h = val


def map_value(val, val_min, val_max, target_min, target_max):
    ratio = (val - val_min) / float(val_max - val_min)
    target = ratio * (target_max - target_min) - target_min
    return target


if __name__ == '__main__':

    port = '/dev/cu.usbmodemfa131'
    hinako = Hinako(port, 'd:3:s', 'd:4:s', 'd:5:s')

    hinako.set_bust(127)
    # hinako.set_waist(127)
    # hinako.set_hip(127)
