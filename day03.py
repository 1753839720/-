#1五角数
# X=0
# def getPentagonalNumber(n):
#     global X
#     for i in range(1,n+1):
#         print(i*(3*i-1)//2,end='  ') 
#         X+=1
#         if X%10==0:
#             print()
# getPentagonalNumber(100)


#2计算各个数字之和
# b=0
# def sumDigits(n):
#     global b
#     for i in str(n):
#         a=int(i)
#         b+=a
#     print(b)
# sumDigits(12345)    


#3.比大小
# def displaySortedNumbers(num1,num2,num3):
#     num1 = float(num1)
#     num2 = float(num2)
#     num3 = float(num3)
#     if num1 > num2:
#         if num1 > num3:
#             if num2 > num3:
#                 print('The sorted numbers are:%.2f %.2f %.2f'%(num3,num2,num1))
#             else:
#                 print('The sorted numbers are:%.2f %.2f %.2f'%(num2,num3,num1))
#         else:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num2,num1,num3))
#     else:
#         if num1 > num3:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num3,num1,num2))
#         elif num2 > num3:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num1,num3,num2))
#         else:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num1,num2,num3))

# num1,num2,num3 = input('Enter three numbers:').split(',')
# displaySortedNumbers(num1,num2,num3)


#5.打印字符
# j = 0
# def printChars(ch1,ch2,numberPerLine):
#     global j
#     num1 = ord(ch1)
#     num2 = ord(ch2)
#     for i in range(num1,num2+1):
#         print(chr(i),end='\000')
#         j += 1
#         if j % int(numberPerLine) == 0:
#             print('\n')

# ch1,ch2,numberPerLine = input('请输入指定字符和个数：').split(',')
# printChars(ch1,ch2,numberPerLine)


#6.天数
# def numberOfDaysInYear(year):
#     for i in range(year,year+11):
#         if (i%4 == 0 and i%100!=0) or (i%100==0 and i%400==0):
#             day = 366
#         else:
#             day = 365
#         print('%s年有%d天'%(i,day))

# numberOfDaysInYear(2010)


#7.两点距离
# import math
# def distance(x1,y1,x2,y2):
#     h = math.sqrt((x1-x2)**2+(y1-y2)**2)
#     print('两点间距离为：%f'%h)

# distance(1,2,3,4)


#8梅森素数（不会，找的运行不了，使用埃拉托斯特尼筛法运行运算比较快）
#知乎找的
# def eratosthenes(p):
#     # p=(2**n)-1
#     IsPrime = [True]*(p+1)
#     IsPrime[1] = False  
#     for i in range(2,int(p**0.5)+1):
#         if IsPrime[i]:
#             for j in range(i*i,n+1,i):
#                 return{x for x in range(2,n+1) if IsPrime[x]}
#     if __name__ == "__main__":
#         print(eratosthenes(120))
#百度找的 
# import math
# MAX_INT = 2**31-1
# marks_bool = [True] * (MAX_INT + 1)
# for i in range(2,int(math.sqrt(MAX_INT)) + 1):
#     j = i
#     k = j
#     while j * k <= MAX_INT:
#         marks_bool[j * k] = False
#         k += 1
# sum_int = 0
# for i in range(2,MAX_INT + 1):
#     if marks_bool[i] is True:
#         sum_int += 1
# print(sum_int)

#9.日期
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("Current date and time is :", localtime)
# main()

#10.掷骰子
# import random

# def panduan():
#     num1 = random.randint(1,7)
#     num2 = random.randint(1,7)
#     if num1 + num2 == 2 or num1 + num2 == 3 or num1 + num2 == 12:
#         print('You rolled %d + %d = %d \nYou lose'%(num1,num2,num1+num2))
#     elif num1 + num2 == 7 or num1 + num2 == 11:
#         print('You rolled %d + %d = %d \nYou win'%(num1,num2,num1+num2))
#     else:
#         point = num1 + num2
#         print('You rolled %d + %d = %d '%(num1,num2,num1+num2))
#         print('point is %d'%point)
#         num1 = random.randint(1,7)
#         num2 = random.randint(1,7)
#         if num1 + num2 == point:
#             print('point is %d'%point)-['']
#             print('You rolled %d + %d = %d \nYou win '%(num1,num2,num1+num2))
#         elif  num1 + num2 == 7:
#             print('point is %d'%point)
#             print('You rolled %d + %d = %d \nYou lose'%(num1,num2,num1+num2))

# panduan()
