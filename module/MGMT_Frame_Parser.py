import pandas as pd


class MGMT_Frame_Parser:

    cwd = '..//..//'

    # 读取QMD_ENUM中的数据
    def qmd_read_excel(self, sheet_nname):
        qmd_test_case_file = self.cwd + 'spec//QMD_ENUM.xlsx'
        df = pd.read_excel(qmd_test_case_file, sheet_nname=sheet_nname)
        return df

    def get_mgmt_type(self, hex_str):
        return self.mgmt_type_map[hex_str]
