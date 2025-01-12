# 1. 元组
# 基本概念：元组是不可变的序列，用()表示，元素之间用逗号隔开
# 1.1 格式：元组名 = (元素1, 元素2, ...)
# 所有元素包含在小括号内，元素与元素之间用逗号隔开，不同元素也是可以不同的数据类型
tuan = (1, 2, 3, 'a', 'b', 'c')
print(type(tuan)) # <class 'tuple'>
tub = (1,) # 如果元组中只有一个元素，末尾必须加上逗号，否则返回这个唯一的值的数据类型
tua = () # 空元组
print(type(tub)) # <class 'tuple'>

# 1.2 元组和列表的区别
#   1. 元组只有一个元素末尾必须加逗号，列表不需要
# li = [1]
# print(type(li))
#   2. 元组只支持查询操作，不支持增删改操作
# li = [1,2,3]
# li[1] = 'a'
# print(li)

tua = (1,2,3,1)
# print(tua[2])  # 元组也有下标，从左往右，从0开始
# tua[2] = 'a'   # 报错：元组不支持修改操作
# count(), index(), len()跟列表用法相同
print(tua.index(2))
print(tua.count(1))
print(len(tua))
print(tua[1:]) # 也可以切片操作

# 1.3 应用场景
#   1. 函数的参数和返回值

#   2. 格式化输出后面的()本质上就是一个元组
name = 'Tom'
age = 20
print('我叫%s，今年%d岁' % (name, age))
info = (name, age)
print(type(info)) # <class 'tuple'>
print('我叫%s，今年%d岁' % info)

# 3. 数据不可以被修改，保护数据的安全


# 2. 字典
# 基本概念：字典是一种可变的容器模型，可存储任意类型对象
# 2.1 格式：字典名 = {key1: value1, key2: value2, ...}
# 键值对：key-value形式保存，键和值之间用：隔开，键值对之间用逗号隔开
dic = {'name': 'Tom', 'age':18}
print(type(dic)) # <class 'dict'>
# 字典中的key是唯一的，value是可以重复的
dic = {'name': 'Tom', 'age':18, 'name': 'Jerry'}
print(dic) # {'name': 'Jerry', 'age': 18} key是唯一的，后面的值会覆盖前面的值
dic = {'name': 'Tom',  'name1': 'Tom'}
print(dic) # {'name': 'Tom', 'name1': 'Tom'} value可以重复

# 2.2 字典的操作
#   1. 查看元素
# 变量名[key]
dic = {'name': 'Tom', 'age':18}
print(dic['name']) # Tom
# print(dic[2]) # 报错：字典中不可以根据下标，查找元素需要根据key，key相当于下标
print(dic['age']) # 18
# print(dic['sex']) # 报错：key不存在

# 变量名.get(key)
dic = {'name': 'Tom', 'age':18}
print(dic.get('name')) # Tom
print(dic.get('tel')) # None，key不存在返回None
print(dic.get('tel', '不存在')) # 不存在 ---如果没有这个key，返回自己设置的默认值

#   2. 修改元素
# 变量名[key] = value
dic = {'name': 'Tom', 'age':18}
dic['name'] = 'Jerry' # 列表通过下标修改元素，字典通过key修改元素
print(dic) # {'name': 'Jerry', 'age': 18}

#   3. 添加元素
# 变量名[key] = value
# 如果key存在就修改，如果key不存在，就是添加元素
dic = {'name': 'Tom', 'age':18}
dic['tel'] = '110' # 此时没有tel这个key，就是添加元素
print(dic) # {'name': 'Tom', 'age': 18, 'tel': '110'}
dic['tel'] = '119' # 此时有tel这个key，就是修改元素
print(dic) # {'name': 'Tom', 'age': 18, 'tel': '119'}

#   4. 删除元素
# 删除整个字典：del 字典名
# dic = {'name': 'Tom', 'age':18}
# del dic
# print(dic) # 报错：dic已经被删除了，找不到这个字典

# 删除指定的键值对：del 字典名[key]
dic = {'name': 'Tom', 'age':18}
del dic['name']
print(dic) # {'age': 18}
# del dic['tel'] # 报错：key不存在

# clear()清空字典: 清空字典中的所有元素,但是字典还是存在
# 字典名.clear()
dic = {'name': 'Tom', 'age':18}
dic.clear()
print(dic) # {}

# pop()删除指定的键值对，并返回删除的值,如果key不存在，报错
# 字典名.pop(key)
dic = {'name': 'Tom', 'age':18}
dic.pop('name')
print(dic) # {'age': 18}
# dic.pop('tel') # 报错：key不存在
dic = {'name': 'Tom', 'age':18}
dic.popitem() # 3.7之前的版本是随机删除一个键值对，3.7之后是默认删除最后一个键值对
print(dic)
