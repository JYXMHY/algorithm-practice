#3.数值类型
#3.1 int整型（常用），任意大小的整数
# num = 1000
# 检测数据类型的方法 type()
# print(type(num))

#3.2 float浮点型（常用），小数
# num2 = 1.5
# print(type(num2))

#3.3 bool布尔型（常用），True和False, 用于判断真假
# 有固定写法，一个为True，一个为False
# 注意：True和False的首字母要大写
print(type(True))
# 布尔值可以当作整型对待，True相当于整数1，False相当于整数0
print(True + False) # 1 + 0 = 1
print(True + 1) # 1 + 1 = 2

#3.4 complex复数型，用于处理复数
# 固定写法：z = a + bj ----> a是实部，b是虚部，j是虚数单位
print (type(2+3j))
ma = 1 + 2j
ma2 = 2 + 3j
print(ma + ma2) # (1+2j) + (2+3j) = 3+5j

# ma = 1 + 2i
# print(ma) # i是虚数单位，不能用i，只能用j



#4.字符串类型str
#特点：需要加上引号，单引号和双引号都可以，包含了多行内容的时候也可以用三引号
#name = 小明 # 会报错，因为没有加引号
name = '小明'
name2 = "小红"
name3 = '''小刚
哈哈'''

'''
我是注释，不会被执行
print(1234)
'''
# 注意多行注释和用三引号的字符串类型的区别，多行注释是单独存在的，前面不需要变量名
print(type(name))
print(type(name2))
print(name3)



# 5.格式化输出
# 5.1 占位符
# 生成一定格式的字符串
# 5.2 % 
# %s 字符串
name = 'bingbing'
print ('我的名字是%s' % name)
# 占位符只是占据位置，并不会被输出

# %d 整数
age = 18
name = 'bingbing'
print ('我的名字是%s，我的年龄是%d' % (name, age))
# %4d 整数
# 数字设置位数，不够的用空格补齐
a = 123
print ('%6d' % a) # 'XXX123'
print ('%06d' % a) # 表示输出的整数显示位数，不足的话用0补齐，'000123'

# %f 浮点数
a = 3.1415926
print('%f' % a)
# 默认后面有6位小数，按照四舍五入原则，如果不够6位，会用0补齐
# %.4f 数字设置小数位数，表示小数点后保留4位小数
b = 2.34567
print('%.4f' % b) # 2.3457
print('%.7f' % b) # 2.3456700, 保留7位小数，不够的用0补齐

# 6. %% 表示一个%
print ('我是%%的1%%' % ())  # 我是%的1%


# 5.3 f格式化
# 格式：f'{表达式}'
name = 'bingbing'
age = 18
print(f'我的名字是{name}，我今年{age}岁了')


