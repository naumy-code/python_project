def str_test(str_param):
    """
    将大写字符串全部变为小写的字符串
    str.lower()函数  函数str_test()
    :param str_param:
    :return:
    """
    str_param = str_param.lower()
    return str_param


def add_space(str_no_space):
    """
    对字符串进行添加空格处理， 两个字符为以空格
    例如：a dddddcfefaa  dda    wda 转换为 ad dd dd cf ef aa dd aw da
    :param str_no_space:
    :return:
    """
    str_no_space = str_no_space.replace(' ', '')
    str_with_space = ''
    for i in range(0, len(str_no_space), 2):
        str_with_space = str_with_space + ' ' + str_no_space[i:i + 2]
    return str_with_space[1::]


def revert_addr_with_space(doc):
    """
    :param doc:
    :return:
    """
    doc = doc.replace(' ', '')
    addr = doc[10:12] + ' ' + doc[8:10] + doc[6:8] + doc[4:6] + ' '
    return addr


if __name__ == '__main__':
    print(add_space("a dddddcfefaa  dda    wda"))
