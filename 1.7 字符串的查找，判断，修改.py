# 3. 字符串常见操作
# 3.1 查找
# 1.find()：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标值，否则返回-1
# find(子字符串，开始位置下标，结束位置下标)
# 注意：开始位置和结束位置下标可以省略，表示在整个字符串中查找
name = 'bingbing'
print(name.find('i'))        # 1 --第一个i的下标为1
print(name.find('bing'))     # 0 --第一个bing，b的下标为0
print(name.find('b', 3))     # 4 --从下标为3的位置开始找b，第一个b的下标为4
print(name.find('b', 5))     # -1 --从下标为5的位置开始找b，没有找到，返回-1
print(name.find('b', 3, 5))  # 4 --从下标为3到5之间找b，第一个b的下标为4 
# 包前不包后
print(name.find('b', 3, 4))  # -1 --从下标为3到4之间找b，没有找到，返回-1

# 2.index()：检测某个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标值，否则报错
# index(子字符串，开始位置下标，结束位置下标)
# 注意：开始位置和结束位置下标可以省略，表示在整个字符串中查找
name = '我命由我不由天'
print(name.index('命'))        # 1 --第一个命的下标为1
# print(name.index('命', 2))   # 报错 --从下标为2的位置开始找命，没有找到，报错
print(name.index('命', 1, 3))  # 1 --从下标为1到3之间找命，第一个命的下标为1
# 同样遵循包前不包后原则
# 和find()的区别：find()找不到返回-1，index()找不到会报错

# 3.count(): 返回某个子字符串在字符串中出现的次数，如果没有出现，返回0
# count(子字符串，开始位置下标，结束位置下标)
# 注意：开始位置和结束位置下标可以省略，表示在整个字符串中查找
name = 'bingbing'
print(name.count('b'))        # 2 --b出现的次数为2
print(name.count('a'))        # 0 --a出现的次数为0
print(name.count('b', 1))     # 1 --从下标为1的位置开始找b，b出现的次数为1
print(name.count('b', 1, 3))  # 0 --从下标为1到3之间找b，b出现的次数为0
# 同样遵循包前不包后原则
print(name.count('b', 1, 4))  # 0 --从下标为1到4之间找b，b出现的次数为0


# 3.2 判断
# 1.startswith()：检查字符串是否以指定字符串开头，是返回True，否返回False
# 如果设置开始和结束位置下标，表示在指定范围内查找
# startswith(指定字符串，开始位置下标，结束位置下标)
st = 'mohaoyan'
print(st.startswith('mo')) # True --以mo开头
print(st.startswith('hao')) # False --不以hao开头
print(st.startswith('m', 0, 1)) # True --从下标为0到1之间以m开头

# 2.endswith()：检查字符串是否以指定字符串结尾，是返回True，否返回False
# 如果设置开始和结束位置下标，表示在指定范围内查找
# endswith(指定字符串，开始位置下标，结束位置下标)
st = 'mohaoyan'
print(st.endswith('yan')) # True --以n结尾
print(st.endswith('yen')) # False --不以yen结尾
print(st.endswith('y', 3, 6)) # True --从下标为3到6之间以y结尾,包前不包后

# 3.isupper()：检测字符串中所有的字母是否都为大写，是返回True，否返回False
st = 'MOHAOYAN'
print(st.isupper()) # True --都是大写字母
print('mohaoyan'.isupper()) # False --不都是大写字母


# 3.2 修改元素
# 1.replace()：把字符串中的旧字符串替换成新字符串，返回新的字符串
# replace(旧字符串，新字符串，替换次数)
# 注意：替换次数可以省略，表示全部替换
name = '好好学习，天天向上'
print(name.replace('天', '时')) # 好好学习，时时向上 --把所有的天替换成时
print(name.replace('天', '时', 1)) # 好好学习，时天向上 --只替换1次，替换第一个天

# 2.split()：指定分隔符来切割字符串，返回分割后的字符串‘列表’
# split(分隔符，分割次数)
# 注意：分割次数可以省略，表示全部分割
st = 'hello,python'
print(st.split(',')) # ['hello', 'python'] --以逗号分割
# 如果字符串不包含分割内容，就不进行分割，会作为一个整体
print(st.split('.')) # ['hello,python'] --不包含.，作为一个整体
print(st.split('o')) # ['hell', ',pyth', 'n'] --以o分割
print(st.split('o', 1)) # ['hell', ',python'] --以o分割，只分割1次

# 3.capitalize()：把字符串的第一个字符大写，其他字符小写
st = 'hello'
print(st.capitalize()) # Hello --首字母大写，其他小写

# 3.lower()：把字符串的所有大写字符改为小写
st = 'heLLO'
print(st.lower()) # hello --大写全部小写

# 4.upper()：把字符串的所有小写字符改为大写
st = 'heLLO'
print(st.upper()) # HELLO --小写全部大写




