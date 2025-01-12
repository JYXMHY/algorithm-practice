# 4. 列表
# 基本格式：列表名 = [元素1, 元素2, 元素3, ...]
# 所有元素放在[]中，元素与元素之间用逗号隔开
# 列表中的元素可以是任意数据类型，包括列表
li = [1, 2, 'a', 4]
print(type(li)) # <class 'list'>
print(li[0]) # 1
# 列表也可以进行切片操作
print(li[1:3]) # [2, 'a']
# 列表是可迭代对象，可以使用for循环遍历
for i in li:
    print(i)

# 4.1 列表常见操作
# 1.增加元素
li = ['one', 'two', 'three']
# append()：在列表末尾添加一个元素
li.append('four')
print(li) # ['one', 'two', 'three', 'four']

# insert()：在指定位置插入一个元素
li.insert(1, '1')
print(li) # ['one', '1', 'two', 'three', 'four']，指定位置如果有元素，原有元素就会后移
# li.insert('zero')   # 报错，insert() 没有指定下标位置

# extend()：在列表末尾添加一个列表
li.extend(['five', 'six']) 
print(li) # ['one', '1', 'two', 'three', 'four', 'five', 'six'] 
li.extend('seven')
print(li) # ['one', '1', 'two', 'three', 'four', 'five', 'six', 's', 'e', 'v', 'e', 'n']
# 注意：extend()添加的是一个列表，如果是字符串，会将字符串拆分成单个字符添加到列表中

# 2.修改元素
# 直接通过下标就可以进行修改
li = [1,2,3]
li[1] = 'a'
print(li) # [1, 'a', 3]

# 3.查询
# in：判断元素是否在列表中，如果在返回True，否则返回False
# not in：判断元素是否不在列表中，如果不在返回True，否则返回False
li = ['a', 'b', 'c', 'd']
print('b' in li) # True
print('e' in li) # False
print('b' not in li) # False

# 用户输入昵称，昵称重复则不能使用
# 定义一个列表，存储已经注册的昵称
# name_list = ['bingbing', 'xiaoming', 'xiaohong']
# while True:
#     name = input('请输入昵称：')
#     # 判断昵称是否已经存在
#     if name in name_list:
#         print(f'{name}已经被注册，请重新输入')
#     # 如果不存在，就添加到列表中
#     else:
#         print(f'{name}注册成功')
#         # 把新的昵称添加到列表中
#         name_list.append(name)
#         print(name_list)
#         break

# index: 返回指定数据所在位置的下标，如果不存在，会报错
# count: 返回指定数据在列表中出现的次数，如果不存在，返回03
# 跟字符串的操作一样


# 4.删除元素
# del：根据下标删除元素
li = ['a', 'b', 'c', 'd']
# del li    # 删除整个列表
del li[2]   # 删除下标为2的元素
print(li)

# pop()：删除指定下标的元素，如果不指定下标，默认删除最后一个元素
li = ['a', 'b', 'c', 'd']
li.pop(1)   # 删除下标为1的元素
print(li)   # ['a', 'c', 'd']
li.pop()    # 删除最后一个元素
print(li)   # ['a', 'c']
# li.pop('a')   # 报错，pop()不支持删除指定元素,只能根据下标删除
# li.pop(10)    # 报错，下标超出范围

# remove()：根据元素的值删除元素，如果元素不存在，会报错
li = ['a', 'b', 'c', 'd']
li.remove('b')  # 删除元素b
print(li)       # ['a', 'c', 'd']
# li.remove('e')  # 报错，元素不存在
li = ['a', 'b', 'c', 'd', 'b']
li.remove('b')  
print(li)       # ['a', 'c', 'd', 'b']，默认删除第一个匹配的元素

# 5.排序
# sort()：对列表进行排序，默认是从小到大
li = [3, 2, 1, 4]
li.sort()
print(li)   # [1, 2, 3, 4]

# reverse(): 倒序，将列表倒置（反过来）
li = [1, 5, 3, 2, 4]
li.reverse()
print(li)   # [4, 2, 3, 5, 1]

# 6.列表推导式
# 格式一：[表达式 for 变量 in 列表]
# 注意：in后面不仅可以放列表，还可以放可迭代对象，如range()函数
li = [1, 2, 3, 4, 5, 6]
# [print(i*5) for i in li]  # 前面的i是表达式，后面的i是变量，li是列表
li = []
# for i in range(1, 6):
#     print(i)
#     li.append(i)
# print(li)
[li.append(i) for i in range(1, 6)] # 更简便的写法
print(li)

# 格式二：[表达式 for 变量 in 列表 if 条件]
# 把基数放进列表中
li = []
# [for i in range(1, 11):
#     if i % 2 == 1:
#         li.append(i)
# print(li)   # [1, 3, 5, 7, 9]
[li.append(i) for i in range(1, 11) if i % 2 == 1]
print(li)   # [1, 3, 5, 7, 9]

# 7.列表嵌套
# 含义：一个列表里面又有一个列表
li = [1, 2, 3, [4, 5, 6]] # [4, 5, 6]是里面的列表
print(li[2])    # 3
print(li[3])    # [4, 5, 6] --取出里面的列表
print(li[3][1]) # 5 --取出内列表的元素