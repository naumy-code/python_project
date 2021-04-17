"""
    test_case_qmd
"""
import sys

from config.auto_test_config_map import auto_test_config_map
from module.common_api import print_with_time_stamp
from test_step.qmd_test.TestStepQmd import TestStepQmd


def test_case_name_info(args):
    pass


class TestCaseQmd:

    def setUp(se1f):
        print("come in")
        super(TestCaseQmd, self).setUp()
        print_with_time_stamp("TestCaseQmd.setUp")

    def tearDown(self):
        print_with_time_stamp("TestCaseQmd.tearDown")
        super(TestCaseQmd, self).tearDown()

    def test_case_timing_trans(self):
        test_case_name_info = {
            'name_cn': 'G3间隔时间测试',
            'id': 'GDEV-1048',
            'name_en': sys._getframe().f_code.co_name
        }

        test_case = test_case_name_info['name_cn']
        # svn_info = auto_test_config_map['SVN版本号’]
        # self.check_whether_m1_pass(test_case, svn_info)
        # 打开监控器
        # jkq_start(self.jke_config, self.jke_logger, 'test_case_timing_trana', self.hw_id)
        test_step = TestStepQmd(test_case_name_info, self.default_config)
        # 将网络模型设置独立到case之外，这样可以方便切换网络棋型测试该用例
        test_step.jdq_off_on('继电器下电后上电')
        test_step.send_tx_init("发送TX_INIT帧设置好option及channel_index)test_step.send_tx dat(发送TX_DAT帧设置帧类型")
        test_step.timing_transmission_test_case("发送TX_DAT帧设置帧类型")


if __name__ == '__main__':
    test_case = TestCaseQmd()
    test_case.test_case_timing_trans()
