# 2. 深浅拷贝
# 赋值： 会随着原对象的改变而改变
li = [1, 2, 3, 4]
print(li)
li2 = li   # 将li直接赋值给li2
print('li', li)
print('li2', li2)
# 给li列表新增元素
li.append(5)
print('新增后的li', li)
print('新增后的li2', li2) # li2也会新增元素，因为li2和li指向的是同一个内存地址
# 赋值：等于完全共享资源，一个值的改变会完全被另一个值共享

# 2.2 浅拷贝（数据半共享）
# 会创建一个新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
import copy               # 导入copy模块
li = [1, 2, 3, [4, 5, 6]] # 定义一个嵌套列表
li2 = copy.copy(li)       # 浅拷贝
print('li', li)
print('li2', li2)
# 查看内存地址 id()
# print('li内存地址', id(li))
# print('li2内存地址', id(li2))
# 内存地址不同，说明是两个不同的对象
# 修改li的第一层数据
li.append(8)
# print('li', li)
# print('li2', li2)
# 往嵌套列表添加元素
li[3].append(7)
print(li[3])
print('li', li)    # [1, 2, 3, [4, 5, 6, 7], 8]
print('li2', li2)  # [1, 2, 3, [4, 5, 6, 7]]
# li2并没有新增元素，但是嵌套列表中的元素发生了变化
print('li[3]内存地址', id(li[3]))
print('li2[3]内存地址', id(li2[3]))
# li2[3]和li[3]的内存地址是一样的，说明嵌套列表是指向同一个内存地址
# 浅拷贝只拷贝第一层数据，嵌套层数据还是指向原来的内存地址
# 优点：拷贝速度快，占用内存小，拷贝效率高


# 2.3 深拷贝（数据完全独立）
# 完全拷贝数据，包括第一层和嵌套层的数据，两个对象之间没有任何关联
import copy              # 导入copy模块
li = [1, 2, 3, [4, 5, 6]] # 定义一个嵌套列表
li2 = copy.deepcopy(li)   # 深拷贝
print('li', li)
print('li2', li2)
# 查看内存地址 id()
# print('li内存地址', id(li))
# print('li2内存地址', id(li2))
# 内存地址不同，说明是两个不同的对象
li.append(8)
print(li)
print(li2)
# 往嵌套列表添加元素
li[3].append(7)
print(li[3])
print('li', li)   # [1, 2, 3, [4, 5, 6, 7], 8]
print('li2', li2) # [1, 2, 3, [4, 5, 6]]
# li2并没有新增元素，嵌套列表中的元素也没有发生变化
print('li[3]内存地址', id(li[3]))
print('li2[3]内存地址', id(li2[3]))
# li2[3]和li[3]的内存地址是不一样的，说明嵌套列表是指向不同的内存地址
# 深拷贝拷贝所有数据，两个对象之间没有任何关联
# 缺点：拷贝速度慢，占用内存大，拷贝效率低


# 3. 可变类型
# 含义：变量对应的值可以修改，但是内存地址不会发生变化
# 可变类型：列表、字典、集合
li = [1, 2, 3, 4]
print(li)
print('li原内存地址',id(li))
li.append(5)
print(li)
print('li现内存地址',id(li))

dic = {'name': 'Tom', 'age': 18}
print(dic)
print('dic原内存地址',id(dic))
dic['name'] = 'Jerry'
print(dic)
print('dic现内存地址',id(dic))

set = {1, 2, 3}
print(set, id(set))
set.remove(1)
print(set, id(set))
# 可变类型的值可以修改，但是内存地址不会发生变化

# 4. 不可变类型
# 含义：变量对应的值不可以修改，如果修改，会创建一个新的对象
# 不可变类型：数字、字符串、元组
n = 10  # 整型
print('原地址', n, id(n))
n = 20
print('修改后', n, id(n))
# n的值发生变化，内存地址也发生变化

st = 'hello'  # 字符串
print('原地址', st, id(st))
st = 'world'
print('修改后', st, id(st))
# st的值发生变化，内存地址也发生变化

tua = (1, 2, 3)  # 元组
print('原地址', tua, id(tua))
# 不支持新增删除和修改操作
tua = ('a', 'b', 'c')
print('修改后', tua, id(tua))

# 注意：前面所说的深浅拷贝只针对可变类型，不可变类型没有深浅拷贝的概念