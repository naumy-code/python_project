
timing_interval, Option, frame_type, transmission_level, sig, data_mcs, pb_mode, sending_times= \
                    getattr(row, '定时间隔'), getattr(row, 'Option'), getattr(row, '帧类型'), getattr(row, '发送电平'), \
                    getattr(row, 'SIG'), getattr(row, 'Data_MCS'), getattr(row, 'PB模式'), getattr(row, '发送次数')

check_point = '当前的option'
check_result = Option
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = '指定的定时发送间隔'
check_result = timing_interval
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = '帧类型'
check_result = frame_type
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = '发送电平'
check_result = transmission_level
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = 'SIG'
check_result = sig
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = 'Data_MCS'
check_result = data_mcs
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = 'PB模式'
check_result = pb_mode
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = '发送次数'
check_result = sending_times
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)

check_point = '测试结果'
check_result = result
self.test_step_info_add_check_point_info(step_name, (check_point, check_result), True)
