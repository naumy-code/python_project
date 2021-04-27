import pandas as pd


class MGMT_Frame_Parser:

    cwd = '..//..//'

    # 读取QMD_ENUM中的数据
    def qmd_read_excel(self, sheet_name):
        qmd_test_case_file = self.cwd + 'spec//QMD_ENUM.xlsx'
        df = pd.read_excel(qmd_test_case_file, sheet_name=sheet_name)
        return df

    # 读取QMD_ENUM_DAT中的数据
    def qmd_dat_read_excel(self, sheet_name):
        qmd_test_case_file = self.cwd + 'spec//QMD_ENUM_DAT.xlsx'
        df = pd.read_excel(qmd_test_case_file, sheet_name=sheet_name)
        return df

    def get_mgmt_type(self, hex_str):
        return self.mgmt_type_map[hex_str]
