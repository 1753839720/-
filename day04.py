# 1按成绩分等级
# a=(40,55,70,58)
# def score(n):
#     best=n[-1]
#     for i in n:
#         if i>=best-10:
#             print(i,'A')
#         elif i>=best-20:
#             print(i,'B')
#         elif i>=best-30:
#             print(i,'C')
#         elif i>=best-40:
#             print(i,'D')
#         else:
#             print(i,'F')
# score(sorted(a))



#2整数列表取逆
# def list_(n):
#     a=n[::-1]
#     print(a)
# list_([1,2,3,4])


# 3读取数字统计个数
# c=[2,5,6,5,4,3,23,43,2]
# def num(n):
#     shu=[]
#     for i in n:
#         b=0
#         for a  in n:               
#             if  a == i:
#                 b+=1
#                 cs=str(a)+' 出现了'+str(b)+'次'
#         shu.append(cs)
#         zong=set(shu)    
#         z_=sorted((list(zong)),key=lambda x:(len(x),x[0])  )
#     for i_ in z_:
#         print(i_)  
# num(sorted(c))  

#4.分析成绩
# s = input('>>').split()
# def sorce(s):
#     l1=[]
#     i=0
#     a=0
#     b=0
#     for _ in s:
#         i +=1
#         _ = int(_)
#         l1.append(_)
#     P = sum(l1)/i
#     for _ in l1:
#         if _ >= P:
#             a+=1
#         else:
#             b+=1
#     print(a,b)
# sorce(s)

#5100个0-9随机数个数
# import random
# def Tj():
#     i_=[]
#     counts=[0,0,0,0,0,0,0,0,0,0]
#     for _ in range(0,1000):
#         a = random.randint(0,9)
#         counts[a] = counts[a]+1
#     for i in range(0,10):
#         i_.append(i)
#     for i  in i_:
#         print(i,'出现了',counts[i],'次')
# Tj()


#6最小元素下标
# def indexOfSmallestElement(lst):
#     l1=[]
#     i=1
#     a=0
#     for _ in lst:
#         _ = int(_)
#         l1.append(_)
#     while i<len(l1):
#         if l1[i]<l1[a]:      
#             a=i
#         i+=1
#     print(a)
# indexOfSmallestElement([2,5,4,9,2,8,])

# 7不用random排序
# import random
# b={}
# def shuffle(n):
#     global b
#     c=[]
#     while len(b)<=len(n)-1:
#         a=random.choice(n)
#         c.append(a)
#         b=set(c)
#         d=list(b)
#         d.sort(key=c.index)
#     print(d)   
# shuffle([0,1,2,3,4,5,6,7,8,9])



# 8.消除重复
# def eliminateDuplicates(lst):
#     l1=set(lst)
#     print(list(l1))
# eliminateDuplicates([1,1,2,5,5,6,4,8])



#9.排序问题
# def isSorted(lst):
#     l1=[]
#     for _ in lst:
#         l1.append(_)
#     l1 = sorted(l1)
#     if l1==lst:
#         print('yes')
#         return True
#     else:
#         print('no')
# isSorted([1,1,3,4,4,5,7,9,10,30,11])


#10.冒泡排序
# def Mp(lst):
#     b=0
#     n=len(lst)
#     for _ in lst:
#         for i in range(0,n-b-1):
#             if lst[i]>lst[i+1]:
#                 lst[i],lst[i+1]=lst[i+1],lst[i]
#         b+=1
#     print(lst)
# Mp([2,6,4,8,9,7,1,3,0,5])




# 11优惠券问题(没看懂)
# def huase()

#12检测四个连续相等的数
# def isConsecutiveFour(n):
#     d=[]
#     for i in str(n):
#         b=0
#         for a in str(n):
#             if a==i:
#                 b+=1
#         d.append(b)
#     e=set(d) 
#     if 4 in e:
#         e.remove(4)
#     print('yes')            
# isConsecutiveFour([666644441])



#1检测ssn
# import re
# def ssn(n):
#     a=re.sub('\D','',n)
#     if len(a) == 9:
#         print('Valid SSN')
#     else:
#         print('Invaild SSN')
# ssn('111-11-1111')

# 2检测第一个字符串是否是第二个的字串
# def chuan(s,n):
#     a=n.find(s)
#     if a>=0:
#         print('yes')
#     else:
#         print('no')
# chuan('1','123')

# 3密码合法（8个字符，包含英文和数字，至少包含两个数字）
# import re
# def mima(n):
#     a=re.sub('\D','',n)
#     print(a)
#     if len(n)>=8 and n.isalnum() == True and len(a)>=2:
#         print('vaild password')
#     else:
#         print('invalid password')

# mima('12aabal1')




# 4输入字符串显示字母数
# def countletters(s):
#     zi=[]
#     for i in s:
#         b=0
#         for a  in s:               
#             if  a == i:
#                 b+=1
#                 zm=str(a)+'出现了'+str(b)+'次'
#         zi.append(zm)
#         zi_=set(zi)
#         zi__=sorted(list(zi_))
#     for i_ in zi__:
#         print(i_)
# countletters('icosnvowvinwbeuiboivn')  




# 5按手机键盘的位置字母转数字(大小写全写，懒得写了)
# def getNumber(n):
#     for i in n:
#         if i=='a' or i=='A' or i=='b' or i=="B" or i=='c' or i=='C':
#             print('2',end='')
#         elif i=='d'or i=='e' or i=='f'or i=='F':
#             print('3',end='')
#         elif i=='g'or i=='h' or i=='i':
#             print('4',end='')
#         elif i=='j' or i=='k' or i=='l':
#             print('5',end='')
#         elif i=='m' or i=='n' or i=='o':
#             print('6',end='')
#         elif i=='p' or i=='q' or i=='r' or i=='s':
#             print('7',end='')
#         elif i=='t' or i=='u' or i=='v':
#             print('8',end='')
#         elif i=='w' or i=='x' or i=='y' or i=='z':
#             print('9',end='')
#         else :
#             print(i,end='') 
#     print()   
# getNumber('1-800-Flowers')

# getNumber('1800flowers')


# 6反向字符串
# def reverse(s):
#     s_=s[::-1]
#     print(s_)

# reverse('000dvnnoinvisn')



#7改写6.29但是没有6.29


#8检测ISBN-13
# def isbn(n):
#     b=[]
#     for i in str(n):
#       b.append(i)
#     b_=[int(x) for x in b ]
#     c=10-(b_[0]+3*b_[1]+b_[2]+3*b_[3]+b_[4]+3*b_[5]+b_[6]+3*b_[7]+b_[8]+3*b_[9]+b_[10]+3*b_[11])%10
#     if c==10:
#         print(str(n)+'0')
#     else:
#         print(str(n)+str(c))
# isbn(978013213080)
# isbn(978013213079)  