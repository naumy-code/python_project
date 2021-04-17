import time

def loop():
    is_ok = True
    for i in range(3):
        print("i", i)
        if is_ok:
            break
        else:
            continue


# python中函数作为参数传递  使用函数当做入参
def run(func):
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))
    func()
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))


def test():
    print("我只是个测试文件")


# 使用函数当做入参，函数本身包含参数
def run(func, a, b):
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))
    func(a, b)
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))


def plus(a, b):
    print(a + b)


# 使用函数当做入参，函数本身包含不确定个数的入参
def run(func, a, *args):
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))
    func(*args)
    print(time.strftime('%Y/%M/%D %H%M%S', time.localtime(time.time())))


def plus(*args):
    temp = 0
    for i in args:
        trmp =temp + i
    print(temp)


if __name__ == '__main__':
    loop()
    run(test)
    run(plus, 3, 5)
    run(plus, 5, 3, 5, 8)