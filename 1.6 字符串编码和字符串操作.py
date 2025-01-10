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
print('好好学习，天天向上'* 5)
