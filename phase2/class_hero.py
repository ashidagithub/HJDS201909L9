# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   英雄的类
# ------------------------(max to 80 columns)-----------------------------------


class Hero():
    skin = '英雄的原始皮肤'
    name = '英雄的姓名'
    position = '英雄的定位'

    ab_viability = 0
    ab_damage = 0
    ab_effect = 0
    ab_difficulty = 0

    def show_me(self):
        print('\n英雄的介绍：xxxxxxxx')
        print('\n生存能力=[%d]，攻击伤害=[%d]，技能效果=[%d]，上手难度=[%d]' % (
            self.ab_viability, self.ab_damage, self.ab_effect, self.ab_difficulty))
        return

    def show_story(self):
        print('\n英雄的故事：xxxxxxxx')
        return

    def show_history(self):
        print('\n史实中的英雄：其实他没那么厉害。。。。')
        return
