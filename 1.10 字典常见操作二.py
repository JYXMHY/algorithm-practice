# 2.3 字典的操作二
#   1. len()求长度
dic = {'name': 'Tom', 'age':18}
print(len(dic)) # 2
dic = {'name': 'Tom', 'age':18, 'tel': '110'}   
print(len(dic)) # 3, 字典中有三个键值对
li = [1, 2, 3, 4]
print(len(li)) # 4
st = 'hello'
print(len(st)) # 5

#   2. keys()获取字典中所有的key
dic = {'name': 'Tom', 'age':18, 'tel': '110'}
print(dic.keys()) # dict_keys(['name', 'age', 'tel'])
# for循环取出所有的key
for i in dic.keys():
    print(i) # name age tel

#   3. values()获取字典中所有的value
dic = {'name': 'Tom', 'age':18, 'tel': '110'}
print(dic.values()) # dict_values(['Tom', 18, '110'])
# for循环取出所有的value
for i in dic.values():
    print(i) # Tom 18 110

#   4. items()获取字典中所有的键值对，键值对是元组形式
dic = {'name': 'Tom', 'age':18, 'tel': '110'}
print(dic.items()) # dict_items([('name', 'Tom'), ('age', 18), ('tel', '110')])
# for循环取出所有的键值对
for i in dic.items():
    print(i, type(i)) # ('name', 'Tom') ('age', 18) ('tel', '110') <class 'tuple'>
    # i是元组类型

# 2.4 字典的应用场景
# 使用键值对，存储描述一个物体的相关信息


# 3.集合 set
# 3.1基本格式：集合名 = {元素1, 元素2, 元素3}
s1 = {1, 2, 3}
print(type(s1)) # <class 'set'>
s1 = {}         # 定义一个空字典
s1 = set()      # 定义一个空集合

# 3.2 集合具有无序性，不支持下标
s1 = {'a', 'b', 'c', 'd', 'e', 'f'}
print(s1) # 每次输出的顺序都不一样
s2 = {1, 2, 3, 4, 5}
print(s2) # 数字运行结果一样

# 集合无序的实现方式涉及hash表
print(hash('a')) 
print(hash('b')) 
print(hash('c'))
# 每一次运行结果都不同，hash值不同，那么在hash表中的位置也不同，这就实现了无序性
print(hash(1))
print(hash(2))
print(hash(3))
# python中int整型的hash值是它本身，所以数字的hash值是固定的，所以集合中的数字是有序的
print(hash('1'))
print(hash('2'))
print(hash('3'))
# 字符串的hash值是不固定的，所以集合中的字符串是无序的
# 无序性；不能修改集合中的值

# 3.3 集合具有唯一性：可以自动去重
s1 = {1, 2, 4, 6, 3, 2, 4}
print(s1) # {1, 2, 3, 4, 6} 重复的元素会自动去重

# 3.4 集合的操作
#   1. 增加元素
# add()：添加的是一个整体
# s2 = {1, 2, 3, 4}
# print('原集合：', s2)
# 集合的唯一性，决定了如果需要添加的元素已经存在，那么不会添加
# s2.add(4)
# s2.add(5)
# s2.add(5,6) # 报错，add()只能添加一个元素
# s2.add((5, 6)) # 添加元组
# print('现集合：', s2)

# update()：把传入的元素拆分，一个个放进集合中
# s2 = {1, 2, 3, 4}
# print('原集合：', s2)
# s2.update('567') 
# s2.update([5, 6, 7])
# s2.update((8, 9, 10))
# s2.update({11, 12, 13}) # 添加元素必须是能够被我们for循环取值的可迭代对象
# print('现集合：', s2)

#   2. 删除元素
# remove()：删除集合中的指定元素，如果元素不存在，会报错
s2 = {1, 2, 3, 4}
s2.remove(2)
# s2.remove(5) # 报错，元素不存在
print('现集合：', s2)

# pop()：对集合进行无序排列，然后将无序排列后的第一个元素删除
s2 = {1, 2, 3, 4}
s2.pop()
print('现集合：', s2) # {2, 3, 4}
s2 = {'a', 'b', 'c', 'd'}
s2.pop()
print('现集合：', s2) # 随机删除，因为无序排列在hash表中