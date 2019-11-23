# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   完成一个行星的类
# ------------------------(max to 80 columns)-----------------------------------

import math

G = 6.67259E-11


class Planet:

    name = '某行星'
    D = 0
    M = 0

    def cal_V(self):
        '输入行星的半径，返回行星的体积'
        # 体积计算公式 V = 4/3 * pi * r3
        r = self.D * 0.5
        V = 4 / 3 * math.pi * r * r * r
        V = 4 / 3 * math.pi * math.pow(r, 3)
        V = 4 / 3 * math.pi * (r**3)

        return V

    def cal_P(self):
        '根据质量和半径计算行星的密度'
        r = self.D * 0.5
        V = self.cal_V()
        return self.M / V / 1000000000000

    def cal_g(self):
        '计算行星的重力加速度'
        r = self.D * 0.5
        g = self.M * G / r / r / 1000000
        g = self.M * G / (r**2) / math.pow(10, 6)
        g = self.M * G / math.pow(r, 2) / math.pow(10, 6)
        return g

    def cal_Ve(self):
        '计算行星的逃逸速度'
        r = self.D * 0.5
        Ve = math.sqrt(2 * G * self.M / r / 1000) / 1000
        return Ve

    def report(self):
        '自行汇报自己的各种信息'

        print('My name is %s' % self.name)
        print('My diameter is %d km, my mass is %0.2e kg' % (self.D, self.M))
        print('My volume is %0.2e stere' % self.cal_V())
        print('My density is %0.2f g/cm3' % self.cal_P())
        print('My acceleration of gravity is %0.2f m/s2' % self.cal_g())
        print('My escape velocity is %0.2f km/s' % self.cal_Ve())

        return


if __name__ == '__main__':
    Mercury = (4878, 3.02E+23)
    p = Planet()
    p.name = 'Mercury'
    p.D = Mercury[0]
    p.M = Mercury[1]
    p.report()
