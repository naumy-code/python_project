"""
    实现需求： 动态的使用Excel获取表头作为字典的key值，value值为随机生成。
    例如：
        config = {
            ”表头一“： ”随机值一“
            ”表头二“： ”随机值二“
            ”表头三“： ”随机值三“
        }
"""


class auto_excel_dict:
    def auto_excel(self):
        print("**")


if __name__ == '__main__':
    list_enum = ['1', '2', '3', '4', '5']

    dic = {
        "1": "v1",
        '2': "v2",
    }
    for a in list_enum:
        print(a)
        dic[a] = 'bbb'

    print(dic)
