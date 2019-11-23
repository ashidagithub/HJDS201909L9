# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习类的使用方法
# ------------------------(max to 80 columns)-----------------------------------

import random

from class_hero import Hero

cjsh = Hero()

cjsh.skin = '苍狼末裔'
cjsh.name = '成吉思汗'
cjsh.position = '射手ARCHER'
cjsh.ab_viability = random.randint(1,100)
cjsh.ab_damage  = random.randint(1,100)
cjsh.ab_effect = random.randint(1,100)
cjsh.ab_difficulty = random.randint(1,100)

cjsh.show_story()
cjsh.show_me()
cjsh.show_history()
