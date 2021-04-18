"""
    反转字符串

"""
import re


class reverse:
    def strReverse(self, strDemo):
        strList = []
        for i in range(len(strDemo) - 1, -1, -1):
            strList.append(strDemo[i])
        return ''.join(strList)

    def test(self):
        string = 'DECGABCF'
        new_str = ''.join(re.findall(r'.{2}', string)[::-1])
        return new_str

    def split_str(self, string, length):
        """
        按照指定长度分割输入字符串，并以列表形式返回
        :param string: 待分割字符串
        :param length: 指定分割长度
        :return: 分割后的字符串列表
        """
        str_lst = re.findall(r'.{' + str(length) + '}', string)
        str_lst.append(string[(len(str_lst) * length):])
        return str_lst

    def reverse_lst(self, string_lst):
        """
        将列表中的字符串反转
        :param string_lst: 字符串列表
        :return: 反转后的字符串列表
        """
        reverse_str_lst = []
        for each in string_lst:
            reverse_str_lst.append(each[::-1])
            reverse_str_lst.append(each[::-2])
        return reverse_str_lst


if __name__ == '__main__':
    code = 'DFCEABCG'
    case = reverse()
    print(case.test())
