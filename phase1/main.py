# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习类的使用方法
# ------------------------(max to 80 columns)-----------------------------------


from my_01_class import MyClass

me = MyClass()

# 可以成功的调用公有属性及方法
if me.sex == '男':
    print ('my name is %s, I am a boy.' % me.name)
elif me.sex == '女':
    print ('my name is %s, I am a girl.' % me.name)
else:
    print ('my name is %s, I am a ...' % me.name)

me.work()
me.study()

# read private property
print(me.__bank_account)
