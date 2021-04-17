import math


# 十六进制转换为32
def hex_to_int_8(hex):
    return int(hex, 16)


# 十六进制转换为16
def hex_to_int_16(r):
    return int(hex[2:] + hex[:2], 16)


# 十六进制转换为32
def hex_to_int_32(r):
    hex_str = r[6:8] + r[4:6] + r[2:4] + r[0:2]
    return int(hex_str, 16)


# 十六进制转换为int
def hex_to_int(r):
    hex_str = r[6:8] + r[4:6] + r[2:4] + r[0:2]
    return str(int(hex_str, 16))


def hex_to_int_common(r, revert_no_space_byte=None):
    hex_str = revert_no_space_byte(r.replace(' ', ''))
    return int(hex_str, 16)
