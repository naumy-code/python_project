import datetime
import time
import re
import math
import pandas as pd

from module.common_api import hex_to_int_32, int32_to_hex, int_to_hex, int16_to_hex

'''
    QMD的测试步骤
    1. 测试用例一： 定时发送测试  timing_transmission_test_case     
'''


class TestStepQmd:

    def dat_frame_excel(self, row_index, sheet_name):
        """
        读取QMD_ENUM_DAT的excel
        :param sheet_name:
        :param row_index: 每一行的行索引
        :return: df_list[0] 返回处理后的字典
        """
        # 相对路径
        df = self.parser.qmd_dat_read_excel(sheet_name)
        # Pandas获取Excel表头转换数组形式
        excel_header = df.columns.tolist()
        # 替换Excel表格内的空单元格，否则在下一步处理中将会报错
        df.fillna("", inplace=True)
        df_list = []
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[row_index, excel_header].to_dict()
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
        dat_confg_params['TX_PSDU'] = ('0x', '0000')
        print(dat_confg_params)
        return dat_confg_params

    def field_judgment(self, field, field_value):
        """
        根据名称查找相应的字段大小,然后返回转换后的值
        :param field_value: 字段值
        :param field: 字段
        :return:
        """
        df = self.parser.field_judgment_read_excel("TX_DAT")
        result_data = df[(df.字段 == field)]
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

    def timing_transmission_test_case(self, step_name=None):
        """
        定时发送测试
        :param step_name: 步骤名称
        :return:
        """
        # if step_name is None:
        #     step_name = sys._getframe().f_code.co_name
        self.step.test_step_info_init(step_name)
        df = self.parser.qmd_read_excel('timing_transmission')
        sheet_name = 'timing_transmission'
        count = 0
        list = []
        sum = 0
        sum2 = 0
        # 循环遍历每一种不同的模式
        for row in df.itertuples():
            print("row.Index", row.Index)
            row_index = row.Index
            # 获取测试的开始时间
            localTime = datetime.datetime.now()
            check_point = '测试开始时刻'
            check_result = localTime
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            timing_interval_before = getattr(row, '定时间隔'),
            Option_before = getattr(row, 'Option'),
            frame_type_before = getattr(row, '帧类型'),
            transmission_level_before = getattr(row, '发送电平'),
            sig_before = getattr(row, 'SIG'),
            data_mcs_before = getattr(row, 'Data_MCS'),
            pb_mode_before = getattr(row, 'PB模式'),
            send_times = getattr(row, '发送次数')
            tx_dat_len_before = getattr(row, 'TX_DAT_LEN')
            tx_psdu_before = getattr(row, 'TX_PSDU')

            # 进行类型的转换
            timing_interval = int32_to_hex(timing_interval_before)
            Option = int_to_hex(Option_before)
            frame_type = int_to_hex(frame_type_before)
            transmission_level = int_to_hex(transmission_level_before)
            sig = int_to_hex(sig_before)
            data_mcs = int_to_hex(data_mcs_before)
            pb_mode = int_to_hex(pb_mode_before)
            tx_dat_len = int_to_hex(tx_dat_len_before)
            tx_psdu = int_to_hex(tx_psdu_before)

            # 转换psdu
            tx_psdu_len = tx_dat_len_before * 8
            tx_psdu = tx_psdu.rjust(tx_psdu_len, 0)

            '''
                第一步：A端发送TX_INIT帧
            '''
            init_config = {
                'TYPE': '02',
                'PIB ID': 'A320',
                'PIB值': '00',
                '参数': {
                    '芯片类型': ('0x', '01'),
                    'OPTION': ('0x', Option),
                    'CHANEL_INDEX': ('0X', '00')
                },
            }
            mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(init_config)
            self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_INIT帧')
            # 进行延时操作， 如果不延时操作会出现一些问题，得到的值会相对来说很大，但是延时操作过长的话会造成所得到的值也很大
            time.sleep(10)

            # 循环发送输入的参数次数
            while count < send_times:
                count = count + 1
                '''
                     第二步：A端发送TX_DAT帧
                '''
                dat_confg_params = self.dat_frame_excel(row_index, sheet_name)
                dat_config = {
                    'TYPE': '02',
                    'PIB ID': 'A321',
                    'PIB值': '00',
                    '参数': dat_confg_params
                }
                mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(dat_config)
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_DAT帧')
                # 进行延时操作， 如果不延时操作会出现一些问题，得到的值会相对来说很大，但是延时操作过长的话会造成所得到的值也很大
                time.sleep(10)

                '''
                    第三步：获取各个timing时间
                '''
                mgmt_frame = '82 03 00 9F 8B 81 09 01 7E 01 5F 00 03 00 A3 22 01 FF FF FF FF 7E'
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, '发端获取时间')
                receiving_tx_time = self.tx.app_mgmt.mgmt_frame_recv("发端获取时间")
                print("receiving_tx_time", receiving_tx_time)
                self.tx.app_mgmt.parser.frame_7e_mgmt_parse(receiving_tx_time)
                # 指定定时发送的时间T2
                tx_dat_set_time = self.tx.app_mgmt.parser.filed_map['TX_DAT_SET_TIME']
                # 指定的时刻触发TX_START_OF_PHR中断，QMD记录当前时间T3
                tx_start_of_phr = self.tx.app_mgmt.parser.filed_map['TX_START_OF_PHR']
                tx_dat_set_time = ''.join(''.join(re.findall(r'.{2}', tx_dat_set_time)[::-1]))
                tx_start_of_phr = ''.join(''.join(re.findall(r'.{2}', tx_start_of_phr)[::-1]))
                print("tx_dat_set_time, tx_start_of_phr", tx_dat_set_time, tx_start_of_phr)
                num1 = (int(tx_dat_set_time, 16) - int(tx_start_of_phr, 16)) / 25
                print("num1", num1)
                num2 = math.pow(abs(num1), 2)
                sum = sum + num1
                sum2 = sum2 + num2
                list.append(abs(num1))

            # 误差均值
            mean_num = sum / send_times
            check_point = '实测误差均值'
            check_result = mean_num
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            # 误差最大值
            max_num = max(list)
            check_point = '实测误差最大值'
            check_result = max_num
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            # 误差RMS值
            rms = math.sqrt(sum2 / send_times)
            check_point = '实测误差RMS值'
            check_result = rms
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            if rms < 100:
                check_point = '结论'
                check_result = 'pass'
                self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            else:
                check_point = '结论'
                check_result = 'fail'
                self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            count = 0
            list = []
            sum = 0
            sum2 = 0
            # 获取测试的结束时间
            localTime = datetime.datetime.now()
            check_point = '测试结束时刻'
            check_result = localTime
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            self.test_step_info_end(step_name)

    def send_now_test(self, step_name=None):
        """
        立即发送测试
        :param step_name: 步骤名称
        :return:
        """
        # if step_name is None:
        #     step_name = sys._getframe().f_code.co_name
        self.step.test_step_info_init(step_name)
        df = self.parser.qmd_read_excel('send_now')
        count = 0
        list = []
        sum = 0
        sum2 = 0
        sheet_name = 'send_now'
        # 循环遍历每一种不同的模式
        for row in df.itertuples():
            row_index = row.Index
            # 获取测试的开始时间
            localTime = datetime.datetime.now()
            check_point = '测试开始时刻'
            check_result = localTime
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            Option_before = getattr(row, 'Option'),
            frame_type_before = getattr(row, '帧类型'),
            transmission_level_before = getattr(row, '发送电平'),
            sig_before = getattr(row, 'SIG'),
            data_mcs_before = getattr(row, 'Data_MCS'),
            pb_mode_before = getattr(row, 'PB模式'),
            send_times = getattr(row, '发送次数')
            tx_dat_len_before = getattr(row, 'TX_DAT_LEN')
            tx_psdu_before = getattr(row, 'TX_PSDU')

            # 进行类型的转换
            Option = int_to_hex(Option_before)
            frame_type = int_to_hex(frame_type_before)
            transmission_level = int_to_hex(transmission_level_before)
            sig = int_to_hex(sig_before)
            data_mcs = int_to_hex(data_mcs_before)
            pb_mode = int_to_hex(pb_mode_before)
            tx_dat_len = int_to_hex(tx_dat_len_before)
            tx_psdu = int_to_hex(tx_psdu_before)

            # 转换psdu
            tx_psdu_len = tx_dat_len_before * 8
            tx_psdu = tx_psdu.rjust(tx_psdu_len, 0)

            '''
                第一步：A端发送TX_INIT帧
            '''
            init_config = {
                'TYPE': '02',
                'PIB ID': 'A320',
                'PIB值': '00',
                '参数': {
                    '芯片类型': ('0x', '01'),
                    'OPTION': ('0x', Option),
                    'CHANEL_INDEX': ('0X', '00')
                },
            }
            mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(init_config)
            self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_INIT帧')
            # 进行延时操作， 如果不延时操作会出现一些问题，得到的值会相对来说很大，但是延时操作过长的话会造成所得到的值也很大
            time.sleep(10)

            # 循环发送输入的参数次数
            while count < send_times:
                count = count + 1
                '''
                     第二步：A端发送TX_DAT帧
                '''
                dat_confg_params = self.dat_frame_excel(row_index, sheet_name)
                dat_config = {
                    'TYPE': '02',
                    'PIB ID': 'A321',
                    'PIB值': '00',
                    '参数': dat_confg_params
                }
                mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(dat_config)
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_DAT帧')
                # 进行延时操作， 如果不延时操作会出现一些问题，得到的值会相对来说很大，但是延时操作过长的话会造成所得到的值也很大
                time.sleep(10)

                '''
                    第三步：获取各个timing时间
                '''
                mgmt_frame = '82 03 00 9F 8B 81 09 01 7E 01 5F 00 03 00 A3 22 01 FF FF FF FF 7E'
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, '发端获取时间')
                receiving_tx_time = self.tx.app_mgmt.mgmt_frame_recv("发端获取时间")
                print("receiving_tx_time", receiving_tx_time)
                self.tx.app_mgmt.parser.frame_7e_mgmt_parse(receiving_tx_time)
                # 指定定时发送的时间T2
                tx_dat_set_time = self.tx.app_mgmt.parser.filed_map['TX_DAT_SET_TIME']
                # 指定的时刻触发TX_START_OF_PHR中断，QMD记录当前时间T3
                tx_start_of_phr = self.tx.app_mgmt.parser.filed_map['TX_START_OF_PHR']
                tx_dat_set_time = ''.join(''.join(re.findall(r'.{2}', tx_dat_set_time)[::-1]))
                tx_start_of_phr = ''.join(''.join(re.findall(r'.{2}', tx_start_of_phr)[::-1]))
                print("tx_dat_set_time, tx_start_of_phr", tx_dat_set_time, tx_start_of_phr)
                num1 = (int(tx_dat_set_time, 16) - int(tx_start_of_phr, 16)) / 25
                print("num1", num1)
                num2 = math.pow(abs(num1), 2)
                sum = sum + num1
                sum2 = sum2 + num2
                list.append(abs(num1))

            # 误差均值
            mean_num = sum / send_times
            check_point = '实测误差均值'
            check_result = mean_num
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            # 误差最大值
            max_num = max(list)
            check_point = '实测误差最大值'
            check_result = max_num
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            # 误差RMS值
            rms = math.sqrt(sum2 / send_times)
            check_point = '实测误差RMS值'
            check_result = rms
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

            if rms < 100:
                check_point = '结论'
                check_result = 'pass'
                self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            else:
                check_point = '结论'
                check_result = 'fail'
                self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            count = 0
            list = []
            sum = 0
            sum2 = 0
            # 获取测试的结束时间
            localTime = datetime.datetime.now()
            check_point = '测试结束时刻'
            check_result = localTime
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            self.test_step_info_end(step_name)

    def frame_interrupt_time_test(self):
        """
        帧中断时刻测试
        :return:
        """
        print("***")


if __name__ == '__main__':
    test_case = TestStepQmd()
    # 定时发送测试
    test_case.timing_transmission_test_case()
