import numpy as np
import pandas as pd
import os

'''
    实现功能: 给定某一行的几个数值，得到这一行的全部信息
    columns函数返回的是列数: print(data.columns)
    获取行数: len(data)
    获取某一列的数据: data['姓名']
    获取前十行符合条件的数据: data[(data.姓名 == '李四') & (data.成绩 == 12) & (data.分数 == 3)][:10] 
    pd.read_csv()方法中header参数，默认为0，标签为0（即第1行）的行为表头。若设置为-1，则无表头
    对series的数据可以使用：变量名.index和变量名.values显示数据内容
    去掉表头：header=None 
    测试master分支
'''


def excel_test(sheet_name, name, grade, course):
    # 绝对路径
    absolute_path = 'C:\\Users\\ywwei\\Desktop\\test.xlsx'
    # 相对路径
    excel_path = '../spec/test.xlsx'
    result = None
    # 判断文件是否存在

    if os.path.exists(excel_path):
        print("文件存在")
        df = pd.read_excel(excel_path, sheet_name=sheet_name, header=None)
        print(df)
        print(df.iloc[3, 4])
        df.iloc[3, 4] = 'zhansan'
        # 将修改后的数据保存到excel中
        df.to_excel(excel_path, sheet_name=sheet_name, index=False, header=None)
        print(df)

        # print(df.loc[df['姓名'] == name, ['姓名', '班级']])
        # result_data = df[(df.姓名 == name) & (df.成绩 == grade) & (df.班级 == course)]
        # result = result_data['班级']
        # result = result.values
        print(type(result))

    return result


if __name__ == '__main__':
    param1 = '李四'
    param2 = 12
    param3 = 3
    sheet_name = 'param'
    print("测试结果: ", excel_test(sheet_name, param1, param2, param3))

