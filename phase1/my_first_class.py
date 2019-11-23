# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   第一个类
# ------------------------(max to 80 columns)-----------------------------------


class MyClass:

    # 类的属性  property
    # public property -----------
    name = '张三'
    sex = '男'
    # protected property -----------
    #_address = '南京东路100号'
    #_mobile = '123-4567-8989'
    # private property -----------
    __bank_account = '987654321'
    __bank_password = 'hello123'

    # 类的方法
    # public method -----------
    def work(self):
        print('I\'m working...')
        return

    def study(self):
        print('I\'m studying...')
        return
    # protected method -----------
    '''
    def _game(self):
        print('I\'m gaming...')
        return
    '''
    # private method -----------

    def __drink(self):
        print('I\'m drinking...')
        return

    def __smoke(self):
        print('I\'m somking...')
        return
