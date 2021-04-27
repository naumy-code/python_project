import pandas as pd
from module.common_api import int_to_hex, int32_to_hex, int16_to_hex

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
    pandas处理读取文件时以0开头的缺失问题 dtype=object
"""



class dict:

    def find_values_in_excel(self, field, field_value):
        """
        根据名称查找相应的字段大小
        :param field_value: 字段值
        :param field: 字段
        :return:
        """
        # 相对路径
        excel_path = '../../../spec/MGMT_PIB.xlsx'
        df = pd.read_excel(excel_path, sheet_name='TX_DAT', dtype=object)
        print(df)
        result_data = df[(df.字段 == field)]
        print(result_data)
        field_length = result_data['字段大小(比特)'].values
        field_length = field_length[0]
        print("field_length", field_length)
        print('field_value', type(field_value))
        if field_length == 8:
            converted_filed_data = int_to_hex(int(field_value))
        if field_length == 16:
            converted_filed_data = int16_to_hex(field_value)
        if field_length == 32:
            converted_filed_data = int32_to_hex(field_value)
        if field_length == 128:
            converted_filed_data = '01000000000000000000000000000000'
        return converted_filed_data

    def dict_case(self, sheet_name):
        """
        :param sheet_name:
        :return:
        """
        # 相对路径
        excel_path = '../../../spec/QMD_ENUM_DAT.xlsx'
        df = pd.read_excel(excel_path, sheet_name=sheet_name, header=0, dtype=object)
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
        for k in dat_confg_params:
            print("key", k)
            v = int(dat_confg_params[k])
            # 找到相应的字段大小
            filed_data = self.find_values_in_excel(k, v)
            dat_confg_params[k] = ('0x', filed_data)
        dat_confg_params['TX_PSDU'] = '01000000000000000000000000000000'
        print(dat_confg_params)


if __name__ == '__main__':
    sheet_name = 'timing_transmission'
    # sheet_name = "TX_DAT"
    # sheet_name = 'Sheet2'
    dict = dict()
    dict.dict_case(sheet_name)
