# 1. 函数
# 含义：将独立的代码块组织成一个整体，使其具有特定的功能的代码集，调用函数可以完成某个功能
# 作用：提高代码的复用性，减少冗余代码，使代码更加简洁
# 基本格式
# 1. 定义函数
# def 函数名(参数):
#     函数体
# 2. 调用函数
# 函数名(参数)
# def login():
#     print('这是登录函数')
#     print('_______')
# login()
# login()
# 调用几次，函数里的代码就会运行几次，每次调用的时候，函数都会从头开始执行

# 编写一个打招呼的函数并调用它
# say_hello() 调用函数前必须保证函数已经被定义，已经存在
def say_hello():
    print('hello')
    print('world')
say_hello()

# 2. 返回值
# 含义：函数执行完后，最后给调用者的一个结果
# 作用：
# 1. return会给函数的执行者返回值
def buy():
    return '烟'
buy() 
print(buy()) # 调用函数，接收返回值

# 2. 函数中遇到return，表示此函数结束，不继续执行
# def buy():
#     return           # 一个返回值也没有，返回的结果是None
#     return '烟', 20  # 返回多个值，返回的是元组
#     return 20        # 函数中遇到return，return下面的代码不会执行
# print(buy()) # 烟
# 返回值的三种情况总结
#   1. 一个返回值也没有，返回的结果是None
#   2. 返回一个值，返回的结果是这个值
#   3. 返回多个值，返回的结果是元组

# return和print()的区别
#   1. return是函数的结束，print()是打印内容
def funa():
    # return 123
    print(123)
    print(456)
funa()

#   2. return是返回计算值，print()是打印内容
def add():
    a = 10
    b = 20
    # return a + b
    print(a + b)
add()


# 3. 函数的参数
# 3.1 形参和实参
# 定义格式：
# def 函数名(形参a, 形参b): # 形参：定义函数时，小括号里面的变量
#     函数体
#     ...（如a=1, b=2）
# 调用格式：
# 函数名(实参1, 实参2)      # 实参：调用函数时，小括号里面具体的值
def add(a, b):           # a,b就是形参
    return a + b
print(add(1, 3))         # 1，3就是实参
# 传参 a=1, b=3


# 3.2 函数参数
# 1. 位置参数（必备参数）
# 含义：传递和定义参数的顺序及个数必须一致
# 格式：def func(a, b):
def funa(name, age, sex):
    print(name)
    print(age)
    print(sex)
funa('Tom', 18, 'male')  # 写了几个就必须要传几个，不可以多传，也不可以少传
# funa('Tom', 18) # 报错：缺少一个位置参数
# 位置也是固定的，name对应Tom，age对应18，sex对应male，不能乱传

# 2. 默认参数
# 含义：给形参一个默认值，调用函数时，如果没有传递参数，则使用默认值
# 注意：默认参数必须放在位置参数后面，包括函数的定义和调用
# 格式：def func(a=20):
def funb(b = 8, a = 8):
    print(a)
funb()    # 没有传参，使用默认值,默认值是8
funb(10)  # 传参，使用传入的参数,传入的是10
# 因为 b 是第一个参数，它被赋值为 10;   a 没有传值，因此仍使用默认值 8。
# 设置默认值：没有传值会根据默认值来执行代码，传了值根据传入的值来执行代码

# 3. 可变参数
# 含义：传入的值的数量是可以改变的，可以传入多个，也可以不传
# 格式：def func(*args): 不一定非要是args，可以是其他的例如*names
def func(*args):
    print(args)       # args是一个元组
    print(type(args)) # <class 'tuple'>
func()                # 不传参，返回的是一个空元组
func(1)               # 传一个参数，返回的是一个元组
func(1, 2, 3)         # 传多个参数，返回的是一个元组
func('海绵宝宝', '派大星', '章鱼哥') # 传多个参数，返回的是一个元组

# 4. 关键字参数
# 含义：传入的参数是一个字典
# 格式：def func(**kwargs): 不一定非要是kwargs，可以是其他的例如**names
def func(**kwargs):
    print(kwargs)       # kwargs是一个字典
    print(type(kwargs)) # <class 'dict'>
func()                  # 不传参，返回的是一个空字典
func(name = 'Tom')      # 传值的时候需要键值对的形式，返回的是一个字典
func(name = 'Tom', age = 18) # 传多个参数，返回的是一个字典
# 作用：可以扩展函数的功能

# 4. 函数嵌套
# 4.1 嵌套调用
# 含义：在一个函数里面调用另外一个函数
def study():
    print('晚上在学习')
def course():
    study()              # 在course函数内调用study函数
    print('Python基础')
# 调用
# study()
course()
# 4.2 嵌套定义
# 含义：在一个函数里面定义另外一个函数
def study():           # 外函数
    print('晚上在学习')
    def course():      # 内函数
        print('Python基础')
        # study()       # 不要在内函数中调用外函数，会陷入死循环，直到超过递归的最大深度
    course()           # 注意缩进，定义和调用是同级的，调用如果在定义里面则永远调用不到
study() # 调用study函数，course函数不会被调用




