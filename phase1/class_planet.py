# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23

# Description:
#   完成一个行星的类
# ------------------------(max to 80 columns)-----------------------------------
import math

G = 6.67259E-11

class Planet:

    # public property
    name = '某行星'
    D = 0
    M = 0

    def __init__(self, planet_name, diameter, mass):
        '类的初始化函数'
        # 行星的基础数据
        self.name = planet_name
        self.D = diameter
        self.r = self.D * 0.5
        self.M = mass
        # 行星的物理量
        self.V = self.cal_V()
        self.P = self.cal_P()
        self.g = self.cal_g()
        self.Ve = self.cal_Ve()
        return

    def cal_V(self):
        '输入行星的半径，返回行星的体积'
        #r = self.D * 0.5
        # 体积计算公式 V = 4/3 * pi * r3
        V = 4 / 3 * math.pi * self.r * self.r * self.r
        return V

    def cal_P(self):
        '根据质量和半径计算行星的密度'
        #V = self.cal_V()
        return self.M / self.V / 1000000000000

    def cal_g(self):
        '计算行星的重力加速度'
        '''
        g = self.M * G / r / r / 1000000
        g = self.M * G / (r**2) / math.pow(10, 6)
        '''
        g = self.M * G / math.pow(self.r, 2) / math.pow(10, 6)
        return g

    def cal_Ve(self):
        '计算行星的逃逸速度'
        Ve = math.sqrt(2 * G * self.M / self.r / 1000) / 1000
        return Ve

    def report(self):
        '自行汇报所有的物理量'
        print('My name is %s' % self.name)
        print('My diameter is %d km, my mass is %0.2e kg' % (self.D, self.M))
        print('My volume is %0.2e stere' % self.V)
        print('My density is %0.2f g/cm3' % self.P)
        print('My acceleration of gravity is %0.2f m/s2' % self.g)
        print('My escape velocity is %0.2f km/s' % self.Ve)
        return
