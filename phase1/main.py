# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   my first class
# ------------------------(max to 80 columns)-----------------------------------

from my_first_class import MyClass

a = MyClass()
a.name = 'Arche'
print(a.name)
print(a.sex)

#print(a.__bank_account)
#print(a.__bank_password)
print(a.read_account( ))

a.work()
a.name = 'Archer'
a.work()
