class TestCaseQmd():

    def setUp(se1f):
        print("come in")
        # super(TestCaseQmd, self).setUp()
        # print_with_time_stamp(" TestCaseQmd.setUp")


    def tearDown(self):
        # print_with_time_stamp(" TestCaseQmd.tearDown")
        super(TestCaseQmd, self).tearDown()

    def test_case_timing_trans(self):
        test_case_name_info = {}
        # test_case_name_info['name_en'] = sys._getframe().f_code.co_name
        test_case_name_info['name_cn'] = 'G3间隔时间测试'
        test_case_name_info['id'] = 'GDEV-1048'
        test_case = test_case_name_info['name_cn']
        # svn_info = auto_test_config_map[' SVN版本号’]
        # self.check_whether_m1_pass(test_case, svn_info)



    def timing_transmission(self):
        print("dddd")


if __name__ == '__main__':
    test_case = TestCaseQmd()
    test_case.test_case_timing_trans()
