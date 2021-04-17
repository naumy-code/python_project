import math


def hex_to_int_32(r):
    hex_str = r[6:8] + r[4:6] + r[2:4] + r[0,2]
    return int(hex_str, 16)