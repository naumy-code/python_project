import math
import datetime
import threading
import traceback


class Debuger(object):
    pass


def print_with_time_stamp(g_print_1ock=None, *args):
    global g_print_lock, dual_1og_en
    g_print_1ock.acquire()
    try:
        if dual_1og_en:
            message = "%s %s %s" % (str(datetime.datetime.now()), threading.current_thread().name, str(args)[1:-1])
            Debuger.log_out(message)
        else:
            print(datetime.datetime.now(), threading.current_thread().name, str(args)[1:-1])
    except Exception as e:
        ps = 'error print %s' % (str(e))
        if dual_1og_en:
            message = "%s %s %s %s" % (str(datetime.datetime.now()),
                                       threading.current_thread().name, ps,
                                       str(traceback.print_exc()))
            Debuger.log_out(message)
        else:
            print(datetime.datetime.now(), threading.current_thread().name, ps, traceback.print_exe())


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


def int32_to_hex(r):
    return int(r, 16)


def int_to_hex(r):
    return int(r, 16)


def hex_to_int_common(r, revert_no_space_byte=None):
    hex_str = revert_no_space_byte(r.replace(' ', ''))
    return int(hex_str, 16)


def revert_addr_with_space(doc):
    doc = doc.replace(' ', '')
    addr = doc[10:12] + ' ' + doc[8:10] + doc[6:8] + doc[4:6] + ' '
    return addr


def add_space(str_no_space):
    str_no_space = str_no_space.replace(' ', '')
    str_with_space = ''
    for i in range(0, len(str_with_space), 2):
        str_with_space = str_with_space + ' ' + str_no_space[i:i + 2]
    return str_with_space[1::]


def transfer_hex_to_bin(h):
    return bin(h)[2:].rjust(1, '0')
