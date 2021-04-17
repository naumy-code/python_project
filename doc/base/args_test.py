import random


# 首先创建学生的类
class Student:
    def __init__(name, age, score, height):
        # 字段的创建与初始化，为了简化代码，突出重点知识，这里全都采用公有字段。
        self.name, self.age, self.score, self.height = name, age, score, height

    # 打印函数
    def __rper__():
        return "(姓名:%s 年龄:%d 成绩:%d 身高:%d)" % (self.name,
                                              self.age, self.score, self.height)


# 根据名字创建一些学生
names = ["张三", "李四", "王五", "赵六"]
ls = []
for name in names:
    s = Student(name, random.randint(13, 17), random.randint(0, 100), random.randint(110, 190))
    ls.append(s)


# 获得装有学生的列表ls

# 编写排序函数
def sort(ll, fuction):  # ll = ls  fuction = older_than 传参既是赋值
    for i in range(len(ll) - 1):
        for j in range(0, len(ll) - 1 - i):
            if fuction(ll[j], ll[j + 1]):
                ll[j], ls[j + 1] = ll[j + 1], ls[j]


# 写一个比较两个学生的函数，左边的年龄大，返回真
def older_than(stu1, stu2):
    return stu1.age > stu2.age


# 写一个比较两个学生的函数，右边的年龄大，返回真
def younger_than(stu1, stu2):
    return stu1.age < stu2.age


# 写一个比较两个学生的函数，左边的成绩差，返回真
def score_worse(stu1, stu2):
    return stu1.score < stu2.score


# 写一个比较两个学生的函数，左边的个子小，返回真
def shorter_than(stu1, stu2):
    return stu1.height < stu2.height


# 调用排序函数，根据的年龄从小到大排序
sort(ls, older_than)
print(ls)

# 调用排序函数，根据的年龄从大到小排序
sort(ls, younger_than)
print(ls)

# 调用排序函数，根据的成绩从高到低排序
sort(ls, score_worse)
print(ls)

# 调用排序函数，根据的身高从高到矮排序
sort(ls, shorter_than)
print(ls)
