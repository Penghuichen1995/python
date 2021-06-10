#冒泡排序
# a = [2,10,8,5,20]
# n = len(a)
# print(n)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#             print(a)
# print(a)


#输入年月日，判断是当年第几天
import calendar
#a = calendar.monthrange(1995,5)
# def which_day(y,m,d):
#     b = calendar.mdays
#     total = 0
#     for i in range(len(b)):
#         if i <m:
#             total += b[i]
#         else:
#             break
#     print(total)
# which_day(1995,6,15)

#通过用户输入两个数字，并计算两个数字之和
# while True:
#     a = input('number1:')
#     b = input('number2:')
#     if int(a) == 0:
#          break
#     elif int(b) == 0:
#         break
#     sum = int(a)+int(b)
#     print('两数之和:{}'.format(sum))

#通过用户输入一个数字，并计算这个数字的平方根
# import cmath
# a = input('输入一个数：')
# b = cmath.sqrt(int(a))
# print('平方根是：{}'.format(b))

#如何将摄氏温度转华氏温度
# a = input('输入温度：')
# b = (float(a)*1.8) +32
# print(b)

#使用 if...elif...else 语句判断数字是正数、负数或零
# while True:
#     a = input('输入一个数字：')
#     try:
#         if int(a)>0:
#             print('是正数')
#         elif int(a)==0:
#             print('是为零')
#         else:
#             print('是负数')
#     except ValueError:
#             print('输入无效')
#             break

#判断字符串是否为数字
# while True:
#     a =input('输入字符串:')
#     try:
#         if float(a) or float(a):
#             print('是数字')
#     except ValueError:
#         print('不是数字字符串')
#     try:
#         import unicodedata
#         unicodedata.numeric(a)
#     except (TypeError,ValueError):
#         pass

#move_zeros([1, 0, 1, 2, 0, 1, 3]) ，预期返回结果： [1, 1, 2, 1, 3, 0, 0]
move_zeros=[1, 0, 1, 2, 0, 1, 3]
a = len(move_zeros)
for i in range(a):
    for j in range(0,a-1):
        if move_zeros[j]==0:
            move_zeros[j],move_zeros[j+1] = move_zeros[j+1],move_zeros[j]
        j = j+1
print(move_zeros)

#实现一个trim()函数，去除字符串首尾的空格（不能使用strip()方法