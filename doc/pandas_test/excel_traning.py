import pandas as pd


class pandas_test:
    """
        进行pandas的部分测试:

    """

    def __init__(self):
        self.enum_qmd_map = {}

    def test(self):
        """
            进行项目的测试，首先遍历Excel表的每一个sheet，然后进行k，v的输出
        :return:
        """
        # 相对路径
        qmd_test_file = '../../spec/pandas_test.xlsx'
        # 获取qmd_enum的值
        enum_qmd_list = pd.read_excel(qmd_test_file, sheet_name=None).keys()
        for enum_name in enum_qmd_list:
            self.enum_qmd_map[enum_name] = {}
            k_col = '姓名'
            v_col = '年龄'
            df = pd.read_excel(qmd_test_file, sheet_name=enum_name)
            for row in df.index:
                k = df[k_col][row]
                v = df[v_col][row]
                self.enum_qmd_map[enum_name][k] = v

        print(self.enum_qmd_map)


if __name__ == '__main__':
    pds = pandas_test()
    pds.test()
