import numpy as np
import module
import pandas as pd
import os
import time, datetime

from module.common_api import hex_to_int_32

'''
    按行按列遍历Dataframe的几种方式:
        # 对于每一行，通过列名name访问对应的元素
        for row in df.iterrows():
            print(row['c1'], row['c2']) # 输出每一行
        for row in df.itertuples():
            print(getattr(row, 'c1'), getattr(row, 'c2')) # 输出每一行
        按列遍历iteritems():
        for index, row in df.iteritems():
            print(index) # 输出列名
'''


class TestStepQmd:

    def timing_transmission_test_case(self, step_name=None):
        # 获取测试的开始时间
        localTime = datetime.datetime.now()
        check_point = '测试开始时刻'
        check_result = localTime
        self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

        '''
            :param 下电，上电:
            :return　None:
        '''
        # if step_name is None:
        #     step_name = sys._getframe().f_code.co_name
        self.step.test_step_info_init(step_name)
        # 相对路径
        file_path = '../../../spec/back_up/timing_transmission.xlsx'
        if os.path.exists(file_path):
            print("文件存在")
            df = pd.read_excel(file_path, sheet_name='timing_transmission')
            print(df)
            for row in df.itertuples():
                print("row", getattr(row, 'Option'))
                timing_interval, Option, frame_type, transmission_level, sig, data_mcs, pb_mode, sending_times = \
                    getattr(row, '定时间隔'), getattr(row, 'Option'), getattr(row, '帧类型'), getattr(row, '发送电平'), \
                    getattr(row, 'SIG'), getattr(row, 'Data_MCS'), getattr(row, 'PB模式'), getattr(row, '发送次数')

                '''
                    第一步：A端发送TX_INIT帧
                '''
                init_config = {
                    'TYPE': '02',
                    'PIB_ID': 'A320',
                    'PIB值': '00',
                    '参数': {
                        '芯片类型': ('0x', '01'),
                        'OPTION': ('0x', Option),
                        'CHANEL_INDEX': ('0X', '00')
                    },
                }
                mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(init_config)
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_INIT帧')

                '''
                    第二步：A端发送TX_DAT帧
                '''
                dat_config = {
                    'TYPE': '02',
                    'PIB ID': 'A321',
                    'PIB值': '00',
                    '参数': {
                        '芯片类型': ('0x', '01'),
                        'FRAME_TYPE': ('0x', '01'),
                        'FRAME_TIMER': timing_interval,
                        'SIG': sig,
                        'TX_LEVEL': transmission_level,
                        'TX_DAT_MCS': data_mcs,
                        'TX_DAT_PB': pb_mode,
                        'TX_FORCE_ENABLE': ('0x', '00'),
                        'TX_DAT_LEN': ('0x', '1000'),
                        'TX_PHR': ('0x', '01000000000000000000000000000000'),
                        'TX_PSDU': ('0x', '01000000000000000000000000000000'),
                    }
                }
                mgmt_frame = self.tx.app_mgmt.parser.mgmt_frame_for_pib_gen(dat_config)
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, 'A端发送TX_DAT帧')

                '''
                    第三步：获取各个timing时间, 是获取发端的数据还是收端的数据？
                '''
                mgmt_frame = self.tx.app_mgmt.mgmt_frame_gen_pib_get(pib_id='A322')
                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, '发端获取时间')
                receiving_tx_time = self.tx.app_mgmt.mgmt_frame_recv("发端获取时间").split(' ')

                tx_dat_set_time = hex_to_int_32[receiving_tx_time[(4 + 8) * 2:((4 + 8) + 4) * 2]]

                self.tx.app_mgmt.mgmt_frame_send(mgmt_frame, '收端获取时间')
                receiving_rx_time = self.tx.app_mgmt.mgmt_frame_recv("收端获取时间").split(' ')
                tx_dat_set_time = hex_to_int_32[receiving_tx_time[(16 + 8) * 2:((16 + 8) + 4) * 2]]

            # 获取测试的结束时间
            localTime = datetime.datetime.now()
            check_point = '测试结束时刻'
            check_result = localTime
            self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
            self.test_step_info_end(step_name)


if __name__ == '__main__':
    test_case = TestStepQmd()
    # 定时发送测试
    test_case.timing_transmission_test_case()
