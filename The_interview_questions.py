# 输入日期， 判断这一天是这一年的第几天？
import datetime


def func():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入日期：")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return "输入的日期是{}年的第{}天".format(year, (date1 - date2).days + 1)


"""现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
d.items() 返回可遍历的元组（键值对）,是dict_items类型
sorted 对所有可迭代对象进行排序，sort只针对列表
"""

d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}

print(sorted(d.items(), key=lambda x: x[1]))
