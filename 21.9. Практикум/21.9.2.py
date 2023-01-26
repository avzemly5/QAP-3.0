# /usr/bin/python
# -*- coding: utf-8 -*-

class Rectangle:
    def __init__(self, x,y,width,heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
    def str(self):
        return f'Rectangle:{self.x},{self.y},{self.width},{self.heigth}.'
    def get_area(self):
        return self.width * self.heigth

rect_1 = Rectangle(5,10,50,100)
print(rect_1)
print(rect_1.get_area())
