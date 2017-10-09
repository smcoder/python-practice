# -*- coding: UTF-8 -*-

class Parent:
    def myMethod(self):
        print("调用父类的方法")
class Child(Parent):
    def myMethod(self):
        print("调用子类的方法")
# 子类的实例
c = Child() 
# 子类调用重写方法
c.myMethod() 
