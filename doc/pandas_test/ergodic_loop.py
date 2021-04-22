"""
    循环遍历excel中的每一行数据，进行处理
    # 对于每一行，通过列名name访问对应的元素

"""
import pandas as pd


class ErgodicLoop:
    def loop(self):
        excel_path = '../../spec/pandas_test.xlsx'
        df = pd.read_excel(excel_path, sheet_name='param')
        print(df)
        # 输出每一行
        # for row in df.iterrows():
        #     print(row[0], row[1])
        # 输出每一行
        for row in df.itertuples():
            print(getattr(row, '姓名'), getattr(row, '成绩'))
        # 按列遍历iteritems():
        # for index, row in df.iteritems():
        #     print(index)  # 输出列名


if __name__ == '__main__':
    test = ErgodicLoop()
    test.loop()
