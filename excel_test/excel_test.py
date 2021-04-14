import numpy as np
import pandas as pd
import os

'''
    columns函数返回的是列数 print(data.columns)
'''

def excel_test(param1, param2, param3):
    # 绝对路径
    absolute_path = 'C:\\Users\\ywwei\\Desktop\\test.xlsx'
    # 相对路径
    excel_path = '../spec/test.xlsx'
    result = None
    # 判断文件是否存在
    if os.path.exists(excel_path):
        print("文件存在")
        data = pd.read_excel(excel_path, sheet_name='param')
        # print(data)
        for i in data.rows:
            grade = data['成绩']
            print(grade)






    return result


if __name__ == '__main__':
    param1 = 20
    param2 = 28
    param3 = 3
    excel_test(param1, param2, param3)


