"""
    定义用户的类
"""


class User:
    @staticmethod
    def function():
        name = '张三'
        age = 18
        return name, age


if __name__ == '__main__':
    user = User()
    name, age = user.function()
    print("姓名{0},年龄{1}".format(name, age))
