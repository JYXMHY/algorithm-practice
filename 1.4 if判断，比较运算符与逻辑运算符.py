#1. if判断基本格式
# if 判断条件:
#     满足条件做的事情

age = 21
if age < 18:
    print('未成年不能上网')

# e.g. 用户从控制台输入成绩，如果满分，输出“你真棒”，如果60分，输出“你需要努力”
# score = input('请输入成绩：')
# if score == '100': # 注意：input()输入的是字符串类型,所以这里要用字符串类型的100,加上引号
#     print('你真棒')
# if score == '60':
#     print('你需要努力')


#2. 比较（关系）运算符
# == 比较两个对象是否相等，相等返回True，不相等返回False
# != 比较两个对象是否不相等，不相等返回True，相等返回False
a = 666
b = 999
print (a==b) # False
print (a!=b) # True
# > 大于
# < 小于
print (a>b) # False
print (a<b) # True

if a < b:
    print('a小于b')
if a > b:
    print('a大于b') # 不会输出，因为a小于b


#3. 逻辑运算符
# 3.1 and 逻辑与，左右两个条件都满足，结果为True，否则为False
a = 'haha'
b = 'hehe'
if a == 'haha' and b == 'hehe':
    print('a和b都在笑')

# 3.2 or 逻辑或，左右两个条件有一个满足，结果为True，否则为False
fruit = 'apple' # 表示室友带回来的水果
if fruit == 'apple' or fruit == 'banana':
    print('带回来了水果')

# 3.3 not 逻辑非，表示相反的结果
print(not 3>9) # True


#4. 三目运算（三元表达式）
# 基本格式：为真结果 if 判断条件 else 为假结果
a = 8
b = 5
# if a <= b:
#     print('a小于等于b') # 为真结果
# else:
#     print('a大于b')    # 为假结果
print('a小于等于b') if a <= b else print('a大于b')


#5. if-else判断
# if 条件:
#     满足条件时要做的事情
# else:
#     不满足条件时要做的事情
a = 999
if a == 666:
    print('nice')
else:  # 注意：else后面不需要加条件
    print('bad')


#6. if-elif判断
# if-else 二选一  if-elif 多选一
# if 条件1:
#     满足条件1时要做的事情
# elif 条件2:
#     满足条件2时要做的事情
# elif 条件3:
#     满足条件3时要做的事情
# 前面的条件满足了，后面的条件就不会判断了,可以有很多个elif

score = 120
if 85 <= score <= 100:
    print('优秀')
elif 60 <= score < 85:
    print('及格')
elif 0 <= score < 60:
    print('不及格')
else:
    print('分数无效')
# else可以表示所有条件都不符合的这样一个情况 if-elif-else可以保证只有一个条件会被执行


#7. if嵌套 一个if语句中包含另一个if语句
# if 条件1:
#     事情1
#     if 条件2:
#         事情2
# else:
#     不满足条件做的事情
# 注意：内存if判断和外层if判断都可以是if-else结构

# 定义一个布尔型变量，表示是否有车票
ticket = False  # True表示有车票,False表示没有车票
# 定义一个浮点型变量保存体温
temp = 38.5
# 外层if判断是否有车票
if ticket == True:
    print('有车票，可以进站--->', end='')
    # 正常人腋下体温是36.3-37.2, 内层if判断体温是否正常
    if 36.3 <= temp <= 37.2:
        print('体温正常，可以进站')
    else:
        print('体温异常，隔离')
else:
    print('没有车票，不能进站')

