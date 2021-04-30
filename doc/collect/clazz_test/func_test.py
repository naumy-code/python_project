def test_case_info():
    """
    测试函数的返回值的接收函数
    :return:
    """
    a = 1 + 2
    b = 1 + 3
    return a, b


if __name__ == '__main__':
    a = test_case_info()
    print("a", a)
