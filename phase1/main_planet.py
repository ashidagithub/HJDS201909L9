# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   Use planet class
# ------------------------(max to 80 columns)-----------------------------------

from class_planet import Planet

# 水星的基础数据
#Mercury = (4878, 3.02E+23)
# 实例化一个 Planet 类，并赋予其水星数据
#p = Planet('Mercury', 4878, 3.02E+23)
#p.report()

all_planets = []
p1 = Planet('Mercury', 4878, 3.02E+23)
all_planets.append(p1)
p2 = Planet('xxx', 4878, 3.02E+23)
all_planets.append(p2)
p3 = Planet('xxx', 4878, 3.02E+23)
all_planets.append(p3)

for p in all_planets:
    p.report()
