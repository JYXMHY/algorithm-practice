# 1. 算数运算符
# 1.1 加减乘除
print(1 + 1) # 2
print(1 - 1) # 0
print(1 * 1) # 1
print(1 / 1) # 1.0 使用算数运算符/，商一定会是浮点数, 且除数不能为0
a = 1/1
print(type(a)) # <class 'float'>

# 1.2 //取整除 取商的整数部分，向下取整
# 向下取整：忽略四舍五入原则，只保留整数部分，小数部分直接舍去
a = 5
b = 2
print(a // b) # 2

# 1.3 %取余数 只取余数部分
print(a % b) # 5/2=2...1, 余数为1

# 1.4 **幂运算   m**n = m的n次方
print(a ** b) # 5的2次方=25

print(7.0//2) # 3.0 
# 使用算数运算符若有浮点数，结果也会用浮点数表示
# 幂（最高优先级）> 乘、除、取余数、取整除 > 加、减（最低优先级）
print(3**2+5/2) # 3**2=9, 5/2=2.5, 9+2.5=11.5


# 2. 赋值运算符
# 2.1 = 赋值
num1 = 5
num2 = 8
# 将一个变量的值赋给另外一个变量
num3 = num1
print(num3) # 5
num4 = num2
print(num4) # 8
# 将运算的值赋给变量
total = num3 + num4 
print(total) # 13

# 2.2 += 加法赋值运算符
a = 1
print(a) # 1
a += 1   #等效于 a = a + 1
print(a) # 2

n1 = 99 # 成本价
n2 = 66 # 利润
n3 = n1 + n2 # 售价
print(n3)  # 165
n1 += n2   # n1 = n1 + n2
print(n1)  # 165

# 2.3 -= 减法赋值运算符
b = 1
print (b)
b -= 1 # 等效于 b = b - 1
print (b)
# 赋值运算符必须连着写，中间不能有空格
# n += 10 # NameError: name 'n' is not defined, n没有被定义
# print(10+=3) # SyntaxError: invalid syntax, 10是常量，不能被赋值
# 纯数字不能被赋值，只有变量才能被赋值


# 3. input()输入函数
# input(prompt) # prompt是提示,会在控制台中显示
# name = input('请输入姓名：') # 输入框中会显示请输入姓名：
# print(name) # 输入什么就会打印什么
# pwd = input('请输入密码：')
# print(pwd) # 输入什么就会打印什么


# 4. 转义字符
# 4.1 \t 制表符，一个tab的空格，也称缩紧
print('foever\tstar') # foever  star
print('姓名\t年龄\t电话') # 姓名    年龄    电话

# 4.2 \n 换行符 表示将当前位置移到下一行开头
print(end = '\n') # 换行
print('哈哈')
print('哈哈\n嘻嘻') # 哈哈 换行 嘻嘻

# 4.3 \r 回车符，将当前位置移到本行开头
print('哈哈\r嘻嘻') # 嘻嘻

# 4.4 \\ 反斜杠符号
print('foever\\star') # foever\star,为了保留斜杠
print(r'foever\star') # foever\star,在字符串前加r，表示原始字符串，不会转义