import pandas as pd

"""
    进行excel的字典输出。
    首先表头作为字典的k
    每一列的值作为v
    excel_header = df.columns.tolist()
    效果: ['定时间隔', 'Option', '帧类型', '发送电平', 'SIG', 'Data_MCS', 'PB模式', '发送次数', 'TX_DAT_LEN', 'TX_PSDU']
    其中Excel转换为dict的关键函数为 .to_dict()
    需要达到的效果为：
            config = {
                ”表头一“： ”随机值一“
                ”表头二“： ”随机值二“
                ”表头三“： ”随机值三“
            }
"""


class dict:

    def dict_case(self, sheet_name):
        """
        :param sheet_name:
        :return:
        """
        # 相对路径
        excel_path = '../../../spec/QMD_ENUM_DAT.xlsx'
        df = pd.read_excel(excel_path, sheet_name=sheet_name, header=0)
        # for row in df.itertuples():
        #     print(row.Index)
        # Pandas获取Excel表头转换数组形式
        excel_header = df.columns.tolist()
        # 替换Excel表格内的空单元格，否则在下一步处理中将会报错
        df.fillna("", inplace=True)
        df_list = []
        for i in df.index.values:
            # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
            df_line = df.loc[i, excel_header].to_dict()
            # 将每一行转换成字典后添加到列表
            df_list.append(df_line)
        dat_confg_params = df_list[0]
        print(dat_confg_params)
        for index in dat_confg_params:
            # '芯片类型': ('0x', '01'),
            # '芯片类型': "('0x', '1'),"
            dat_confg_params[index] = ('0x', dat_confg_params[index])
            print()
        print(dat_confg_params)



if __name__ == '__main__':
    sheet_name = 'timing_transmission'
    # sheet_name = 'Sheet2'
    dict = dict()
    dict.dict_case(sheet_name)
