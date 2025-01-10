# 1. 字符串编码
# 本质上就是二进制与语言文字的一一对应关系，即将文字转换为二进制，以便计算机能够识别。
# Unicode编码：所有字符都是2个字节，好处：字符与数字之间转换速度快，缺点：占用空间大

# 1.4 字符串编码转换
a = 'hello'
print(type(a)) # str,字符串是以字符为单位进行处理
a1 = a.encode()     # 编码，默认utf-8
print('编码后:',a1)          
print(type(a1)) # bytes,以字节为单位进行处理
a2 = a1.decode()    # 解码，默认utf-8
print('解码后:',a2)
print(type(a2)) # str,字符串是以字符为单位进行处理
# 注意：对于bytes，只需要知道他和字符串类型之间的互相转换

st = '这里是中国'   
st1 = st.encode('utf-8') # 编码
print(type(st1)) # bytes
st2 = st1.decode('utf-8') # 解码
print(type(st2)) # str

# 2 字符串操作
# 2.1 +字符串拼接
print(10+10) # 20 数字相加,算数运算符
print('10'+'10') # 1010 字符串拼接,字符串连接符
name1 = '小明'
name2 = '小红'
print(name1+name2) # 小明小红
print(name1 , name2, sep='')  # 小明小红，原本是小明 小红
# sep: 表示多个打印内容之间的分隔符,指定为空字符串（''），则会改变输出格式。

# 2.2 *重复输出
print('好好学习，天天向上\n'* 5)
# 需要输出多少次，*后面就写多少次
print('&\t'* 10)

# 2.3 成员运算符 in
# 作用：检查字符串中是否包含了某个字符串（即某个字符或多个字符）
# in: 如果包含的话，返回 True，不包含返回 False
# not in: 如果不包含的话，返回 True，包含返回 False
name = 'bingbing'   
print('b' in name) # True
print('a' in name) # False
print('b' not in name) # False
print('a' not in name) # True
print('bin' in name) # True
print('binb'in name) # False

# 2.4 下标
# Python中下标从0开始
# 作用：通过下标能够快速找到对应的数据
# 格式：字符串名[下标值]
name = 'foreverstar'
# 从左往右数，下标从0开始
print(name[0])
print(name[1])
# print(name[12])  # 索引错误，取值的时候超过下标范围
# 从右往左数，下标从-1开始，-1，-2...
print(name[-1])
print(name[-2])
# print(name[-12]) # 索引错误

# 2.5 切片
# 含义：指对操作的对象截取其中一部分的操作
# 语法：[开始位置：结束位置；步长]
# 包前不包后：即从起始位置开始，到结束位置的前一位结束（不包含结束位置本身）
st = 'abcdefghijk'
print(st[0:4]) # abcd
print(st[4:7]) # efg
print(st[3:])  # defghijk --下标为3之后的全部截取到
print(st[:7])  # abcdefg --下标为7之前的全部截取到
# 从右往左
print(st[-1:]) # k
print(st[:-1]) # abcdefghij
# 步长：表示选取间隔，不写步长，则默认是1
# 步长的绝对值大小决定切取的间隔，正负号决定切取的方向
# 正数表示从左往右取值，负数表示从右往左取值
st = 'abcdefghijk'
print(st[-1::1])  # 从右往左切只能取到一个值k
print(st[-1::-1]) # 从左往右切kjihgfedcba
print(st[-1:-5:-1]) # kjih