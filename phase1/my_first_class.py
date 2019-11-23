# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   my first class
# ------------------------(max to 80 columns)-----------------------------------

class MyClass:

    # 类的属性  property
    # public property -----------
    name = '张三'
    sex = '男'

    # private property -----------
    __bank_account = '987654321'
    __bank_password = 'hello123'

    def read_account(self):
        return  self.__bank_account

    def work(self):
        print(' %s is working...' % self.name)
        return
