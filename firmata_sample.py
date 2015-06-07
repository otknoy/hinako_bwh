#!/usr/bin/env python
import time
import math
from pyfirmata import Arduino, util

def map_value(val, val_min, val_max, target_min, target_max):
    ratio = (val - val_min) / float(val_max - val_min)
    target = ratio * (target_max - target_min) - target_min
    return target


def move_servo(pin, begin_val, end_val, ds=0.1):
    step = 1 if begin_val < end_val else -1

    # print '%d -> %d' % (begin_val, end_val)
    # print step

    for i in range(begin_val, end_val, step):
        pin.write(i)
        time.sleep(ds)


if __name__ == '__main__':
    port = '/dev/cu.usbmodemfa131'

    board = Arduino(port)

    '''
    d: digital output
    2: number PWM pin
    s: servo control
    '''
    servo = board.get_pin('d:3:s')

    move_servo(servo, 0, 127, ds=0.1)
    move_servo(servo, 127, 255, ds=0.01)
    move_servo(servo, 255, 0, ds=0.01)
