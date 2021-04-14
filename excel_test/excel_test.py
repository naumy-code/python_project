import numpy as np
import pandas as pd
import os

'''
    实现功能: 给定某一行的几个数值，得到这一行的全部信息
    columns函数返回的是列数: print(data.columns)
    获取行数: len(data)
    获取某一列的数据: data['姓名']
    获取前十行符合条件的数据: data[(data.姓名 == '李四') & (data.成绩 == 12) & (data.分数 == 3)][:10] 
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
        # print(data.loc['李四'])
        print(data.loc[data['姓名'] == param1, ['姓名', '分数']])
        print(data[(data.姓名 == '李四') & (data.成绩 == 12) & (data.分数 == 3)][:10])
        data1 = data[(data.姓名 == '李四') & (data.成绩 == 12) & (data.分数 == 3)]
        print("result", data1['分数'])


    return result


if __name__ == '__main__':
    param1 = '李四'
    param2 = 12
    param3 = 4
    excel_test(param1, param2, param3)


