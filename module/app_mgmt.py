import time

from module.common_api import print_with_time_stamp


class app_mgmt:
    def mgmt_frame_send(self, mgmt_frame, comments='', sleep_time=0.1):
        print_with_time_stamp('MGMT SEND(%S): %S' % (comments, mgmt_frame))
        tx_bytearray = bytearray.fromhex(mgmt_frame)
        self.dev.send(tx_bytearray)
        time.sleep(sleep_time)

    def mgmt_frame_rece(self, comments=''):
        mgmt_frame_rx = ''
        rap_buffer = []
        is_7e_found = False
        is_7e_found, rap_buffer = frame_7e_reve(self.dev)
        if is_7e_found:
            if self.dev.config['协议类型'] == '485':
                p = '.*7D 5E(.*)7D 5E'
                ret = match_pattern(p, hex_list_tohex_str(rap_buffer), 1)
                if set is not None:
                    mgmt_frame_rx = '7E' + ret[0] + '7E'
                    print_with_time_stamp('MGMT RECV(%s): %s' % (comments, mgmt_frame_rx))
                else:
                    print_with_time_stamp('485 RECV(%s): %s' % (comments, hex_list_to_hex_str(rap_buffer)))
                    mgmt_frame_rx = hex_list_to_hex_str(rap_buffer)
            else:
                mgmt_frame_rx = hex_list_to_hex_str(rap_buffer)
                mgmt_frame_rx = mgmt_frame_rx.replace('7D 5D', '7D').replace('7D 5E', '7E')
                print_with_time_stamp('MGMT RECV(%s): %s' % (comments, mgmt_frame_rx))

        return mgmt_frame_rx
