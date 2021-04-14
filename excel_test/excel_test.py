import numpy as np
import pandas as pd
import os

# 绝对路径
excel_path1 = 'C:\\Users\\ywwei\\Desktop\\test.xlsx'
# 相对路径
excel_path = '../spec/test.xlsx'

# 判断文件是否存在
if os.path.exists(excel_path):
    print("文件存在")
    data = pd.read_excel(excel_path)
    print(data)


