import pandas as pd


def find_values_in_excel(sheet_name, field):
    # 相对路径
    excel_path = '../../../spec/MGMT_PIB.xlsx'
    df = pd.read_excel(excel_path, sheet_name=sheet_name, dtype=object)
    print(df)
    result_data = df[(df.字段 == field)]
    print(result_data)
    field_length = result_data['字段大小(比特)'].values
    field_length = field_length[0]
    print("field_length", field_length)


if __name__ == '__main__':
    sheet_name = "TX_DAT"
    field = 'TX_TIMER'
    find_values_in_excel(sheet_name, field)
