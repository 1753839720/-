# 1
# import math
# a,b,c,=map(float,input('请输入a，b，c：').split())
# d = b*b-4*a*c
# if d==0:
#     r1=(-b+math.sqrt(d))/2*a
#     print('根为',r1)
# elif d>0:
#     r2=(-b-math.sqrt(d))/2*a
#     r1=(-b+math.sqrt(d))/2*a
#     print('根为',r1,r2)
# elif d<0:
#     print('没有实根')
# else:
#     pass


# 2
# import random
# num1 = random.randint(0,101)
# num2 = random.randint(0,101)
# print(num1,num2)
# ad=int(input('请输入这两个数字的和'))
# if ad == num1+num2:
#     print('ture')
# else:
#     print('flase')
 


# 3
# day = int(input('请输入今天是周几（0-6表示周日-周六）：'))
# frue = int(input('请输入今天之后到未来几天：')) 
# a = (day+frue)%7
# if a == 0:
#      print('今天是周末')
# elif a == 1:
#     print('今天是周一')
# elif a == 2:
#     print('今天是周二')  
# elif a == 3:
#     print('今天是周三')
# elif a == 4:
#     print('今天是周四')
# elif a == 5:
#     print('今天是周五')
# elif a == 6:
#     print('今天是周六')
# else:
#      pass


# 4 
# a,b,c=map(int,input('请输入三个整数：').split())
# x=[a,b,c]
# x.sort()
# print(x)
 
# 5
# x1,x2=map(float,input('请输入包装1的价格和重量：').split())
# y1,y2=map(float,input('请输入包装2的价格和重量：').split())
# a=x1/x2
# b=y1/y2
# if a>b:
#     print('包装1更好')
# else:
#     print('包装2更好')

# 6
# mouth,year=map(int,input('请输入月和天').split())
# if mouth==1 or mouth==3 or mouth==5 or mouth==7 or mouth==8 or mouth==10 or mouth==12:
#     print(year,'年',mouth,'月有31天')
# elif mouth==4 or mouth==6 or mouth==9 or mouth==11:
#     print(year,'年',mouth,'月有30天')
# elif mouth==2:
#    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
#         print(year,'年',mouth,'月有29天')
#    else:
#         print(year,'年',mouth,'月有28天')
# else:
#     pass
# 


# 7
# import random
# a=int(input('请输入猜测（0代表正面，1代表反面）：'))
# b = random.randint(0,1)
# if a==b:
#     print('猜测成功')
# else:
#     print('猜测失败')



# 8
# import random
# computer = random.randint(0,2)
# user= int(input('请输入（0代表剪刀，1代表石头，2代表布：'))
# if computer == user:
#     print('平局')
# elif computer == 1 and user == 0:
#     print('失败')
# elif computer == 0 and user == 2:
#     print('失败')  
# elif computer == 2 and user == 1:
#     print('失败')
# else:
#     print('成功')


# 9
# year = int(input('请输入年份'))
# month = int(input('请输入月份（1-12）'))
# day = int(input('请输入日期（1-31）'))
# if month<=2:
#     m=month+12
#     y=year-1
# else:
#     m=month
#     y=year
# h=int(day+(26*(m+1)/10)//1+(y%100)+((y%100)/4)//1+((y/100)/4)//1+(5*(y/100)))%7 -1
# if ((year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0) and month>2 :
#     h=h+7
# if h == 0:
#     print('今天是周末')
# elif h == 1:
#     print('今天是周一')
# elif h == 2:
#     print('今天是周二')  
# elif h == 3:
#     print('今天是周三')
# elif h == 4:
#     print('今天是周四')
# elif h == 5:
#     print('今天是周五')
# elif h == 6:
#     print('今天是周六')
# else:
#        pass


# 10
# import numpy as np 
# import random
# a=np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
# b=np.random.choice(['梅花','红桃','方块','黑桃'])
# print('这张牌是',b,a)


# 11
# a=(input('请输入一个整数>>'))
# b=a[::-1]
# if a==b:
#     print('是回文数')
# else:
#     print('不是回文数')


# 12
# a,b,c=map(int,input('请输入三边长度：').split())
# if a+b>c or a+c>b or b+c>a:
#     print('yes',a+b+c)
# else:
#     print('no')


# 1
# a=float(input('请输入一个整数'))
# n=0
# m=0
# b=a
# while a!= 0:
#     a=float(input('请输入一个整数'))
        # if a>0:
        #     n+=1
        # else:
        #     m+=1
#     b=b+a
# print(n,m,b/n)


# 2
# a=10000
# b=0
# for i in range(1,11):
#     a=a*1.05
#     b+=a
# print('十年的学费总和是%.2f'%b,'第十年的学费是%.2f'%a)



# 4
# n=0
# for a in range(100,1001):
#     if a%30==0:
#         n+=1
#         print(a,end=' ')
#         if n%10==0:
#             print()



#5
# n=0
# a=0
# while a<12000: 
#     n=n+1
#     a=n*n
# print(n)
# m=0
# b=0
# while b<12000:
#     m=m+1
#     b=m*m*m
# print(m-1)


# 7 
# b=0
# c=0
# for a in range(1,50001):
#     b+=1/a
# print('正向加',b)
# for d in range(50000,0,-1):
#     c+=1/d
# print('反向加',c)


# 8
# b=0
# c=0
# for a in range(1,98,2):
#     b=a/(a+2)
#     c+=b
# print(c)


# 9
# i=int(input('请输入I的值'))
# b=0
# c=0
# n=1
# for a in range(1,i+1):
#     b=((-1)**(n+1))/(2*n-1)
#     c+=b
#     n+=1
# print(4*c)


#10
# l=[]
# for i in range(1,10001):
#     for a in range(1,i):
#         if i%a==0:
#             l.append(a)
#     if sum(l)==i:        
#          print('10000以内完全数为：',i)        
#     l=[]


# 11
# tmp=[]
# for x in range(1,8):
#     for y in range(1,8):
#         if x!=y and sorted([x,y]) not in tmp:
#             tmp.append([x,y])
# print(tmp)
# print(len(tmp))