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


#   3. return后面的代码不会执行，print()后面的代码会执行
#   4. return可以返回多个值，print()只能打印一个值
#   5. return可以接收返回值，print()不能接收返回值


