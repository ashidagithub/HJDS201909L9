# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习类的使用方法
# ------------------------(max to 80 columns)-----------------------------------

import random

from class_hero import Hero

cjsh = Hero('苍狼末裔', '成吉思汗', '射手ARCHER')
cjsh.show_me()

pg = Hero('破晓之神','盘古','战士WARROR')
pg.show_me()

nobody = Hero('','','')
nobody.show_me()
