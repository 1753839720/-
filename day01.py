# 1.
# C=float(input('请输入温度摄氏度'))
# F=1.8*C + 32
# print('华氏温度为 %.2f' %F)



# 2.
# import math
# radius=float(input('请输入半径'))
# length=float(input('请输入高'))
# area = radius*radius*math.pi
# vloume = area * length
# print('底面积为 %.2f' %area)
# print('体积为 %.2f' %vloume)




# 3.
# feet = float(input('请输入英尺'))
# meters = feet*0.305
# print(  meters ,'米' )




# 4.
# M=float(input('请输入水量kg'))
# final=float(input('请输入最终温度'))
# initial=float(input('请输入初始温度'))
# Q=M*(final-initial)*4184
# print('需要的能量是', Q)





# 5.
# balance = float(input('请输入差额'))
# interest_rate = float(input('请输入年利率：'))
# insterest = balance * (interest_rate / 1200)
# print('利息:%.5f'%insterest)
# 







# 6.
# v0=float(input('请输入初始速度'))
# v1=float(input('请输入末速度'))
# t=float(input('请输入时间S'))
# a=(v1-v0)/t
# print('加速度为%.4f' %a)





 
# 7.
# monthly=float(input('请输入存款数'))
# mount= int (input('请输入存的时间（月份）'))
# a=1
# b=monthly*(1.00417**a)
# c=mount-1
# while a<= c:
#     b=(b+100)*(1.00417)
#     a=a+1
# print(b)



# 8.
# number=input('请输入一个0-1000的整数')
# ge=int(number[2])
# shi=int(number[1])
# bai=int(number[0])
# zong=ge+shi+bai
# print('和为',zong)


# 3.1
# import math 
# r=float(input('请输入顶点到中心的距离')) 
# s=2*r*math.sin(math.pi/5)
# Area=5*s*s/(4*math.tan(math.pi/5))
# print(Area)


# 3.2
# import math
# x1,y1=map(float,input('请输入经纬度(x1,y1)').split())
# x2,y2=map(float,input('请输入经纬度(x2,y2)').split())
# radius=6371.01
# a=math.radians(x1)
# b=math.radians(y1)
# c=math.radians(x2)
# d=math.radians(y2)
# d=radius*math.acos(math.sin(a)*math.sin(c)+math.cos(a)*math.cos(c)*math.cos(b-d))
# print(d)


# 3.4
# import math
# s=float(input('请输入边长'))
# Area=5*s*s/(4*math.tan(math.pi/5))
# print(Area)


# 5
# a=int(input('请输入一个数字'))
# print(chr(a))

# 6
# name = input('请输入姓名:')
# time = float(input('请输入工作时间:'))
# moeny = float(input('请输入每小时报酬:'))
# a = float(input('请输入联邦预扣税率:'))
# b = float(input('请输入州预扣税率:'))
# print('员工姓名：',name)
# print('每周工作时间：',time)
# print('一小时工资：',moeny)
# print('总工资:',moeny*time)
# print('扣除的税收：')
# print('   联邦扣除（20.0%）：',a*moeny*time)
# print('   州扣除（9.0%）：',b*moeny*time)
# print('   总扣除：',(a+b)*moeny*time)
# print('应得的工资：',(1-a-b)*moeny*time)

# 7
# num=input('请输入一个整数：')
# b=num[::-1]
# print(b)