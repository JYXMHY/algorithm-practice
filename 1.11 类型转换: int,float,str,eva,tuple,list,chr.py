# 1. 类型转换
# 1.1 int()：将一个数值或字符串转换成整数，只能够转换由纯数字组成的字符串
# float ---> int
a = 1.2
print(type(a))  # <class 'float'>
b = int(a)
print(type(b))  # <class 'int'>
print(int(1.8))        # 1
# 浮点型强转整型会去掉小数点后面的数值，只保留整数部分

# str ---> int
a = int('123')     
print(type(a))  # <class 'int'>
# print(int('bingbing'))  # 报错
# 如果字符串中有数字和正负号(+/ -)以外的字符，会报错
print(int('-10'))
# +/=写在前面表示正负号，不可以写在后面
# print(int('10+'))  # 报错

# 用户从控制台输入，判断年龄
# age = int(input('请输入您的年龄：'))   # input默认输入的是字符串类型
# print(type(age))  # <class 'str'>
# if age >= 18:
#     print('成年了')

# 1.2 float()：转换为一个小数
# int ---> float
print(float(11))    # 11.0, 整型转换为浮点型，会自动添加一位小数
print(float(-11))   # -11.0
print(float('+11.345'))
# print(float('10-')) # 报错:如果字符串中有正负号、数字和小数点以外的字符，则不支持转换

# 1.3 str()：转换成字符串类型，任何类型都可以转换成字符串类型
n = 100
print(type(n))  # <class 'int'>
n2 = str(n)
print(type(n2)) # <class 'str'>

# float转换成str会取出末位为0的小数部分
st = str(-1.80)
print(st,type(st))  # -1.8 <class 'str'>
st = str(-1.000)
print(st,type(st))  # -1.0 <class 'str'> 

li = [1, 2, 3]
st = str(li)
print(st,type(st))  # [1, 2, 3] <class 'str'>

# 1.4 eval()：执行一个字符串表达式，并返回表达式的值
print(10 + 10)  # 20
print('10' + '10')  # 1010
print('10 + 10')  # 10 + 10
print(eval('10 + 10'))  # 20 执行运算，并返回运算值
print(eval('10' + '10'))  # 1010 执行字符串拼接
# print(eval('10 + '10.5''))  # 报错：整型和字符串不能相加

# eval()可以实现list，dict，tuple和str之间的转换
# str ---> list
st1 = '[[1,2], [3,4], [5,6]]'
print(type(st1))  # <class 'str'>
li = eval(st1)
print(li, type(li))  # [[1, 2], [3, 4], [5, 6]] <class 'list'>

# str ---> dict
st2 = "{'name': 'Tom', 'age': 18}"
print(type(st2))  # <class 'str'>
dic = eval(st2)
print(dic, type(dic))  # {'name': 'Tom', 'age': 18} <class 'dict'>

# eval()非常强大，但是也很危险，如果字符串中有恶意代码，会被执行

# 1.5 list()：将可迭代对象转换成列表
# 支持转换为list的数据类型：元组，字符串，集合，字典
# str ---> list
print(list('bingbing'))  # ['b', 'i', 'n', 'g', 'b', 'i', 'n', 'g']
# print(list(12345)) # 报错：整型不支持转换成列表

# tuple ---> list
print(list((1, 2, 3)))  # [1, 2, 3]

# set ---> list
print(list({'a','b','c','b'}))  
# 集合转换成列表，会自动去重，无序

# dict ---> list
dic = {'name': 'Tom', 'age': 18}
print(list(dic))  # ['name', 'age'] 默认转换为字典的key
# 字典转换成列表，会取键名作为列表的值



