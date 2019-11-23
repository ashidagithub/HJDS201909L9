# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习类的使用方法
# ------------------------(max to 80 columns)-----------------------------------

from person_chinese import Person, Chinese

print('------ cutting line ------')
man = Person()
man.walk()

print('------ cutting line ------')
Chinese_man = Chinese()
Chinese_man.walk()  # 使用父类的方法
Chinese_man.talk_Chinese()  # 使用子类（自己）的方法
