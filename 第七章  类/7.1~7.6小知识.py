'''
# 7.1.2案例[编写第一个类]      P127    求立方体的类
class Box1():  # 类定义，类名为Box1
    def __init__(self,length1,width1,height1):  # 传递类参数的保留函数__init__
        self.length = length1  # 长数据变量
        self.width = width1  # 宽数据变量
        self.height = height1  # 高数变量
    def volume(self):  # 求立方体体积的函数volume，并供实例调用
        return self.length*self.width*self.height
# ===============================================上面为类定义，下面开始调用类，并建立对应的实例
my_box1 = Box1(10,10,10)  # 通过Box1类赋值建立对应的一个实例my_box1
print('立方体体积是%d'%(my_box1.volume()))  # 通过实例调用volume()方法求体积并打印
'''


'''
# 7.2.1 属性值初始化   P130
# 1.在__init__里直接初始化值
# 求立方体的类
class Box1():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
# 上面三行代码直接给length,width,height属性赋值为0。调用Box1()类，生成实例B1如下：
B1 = Box1()
print(B1.length)  # 打印length属性初始值


# 2.传递参数初始化
# 求立方体的类
class Box2():
    def __init__(self,length1,width1,height1):
        self.length = length1
        self.width = width1
        self.height = height1
# ===================================主程序调用Box2()类，并创建B2实例
B2 = Box2(10,10,10)  # 通过对类赋初值
print(B2.length)  # 打印length属性初始值
'''


'''
# 7.2.2 属性值修改    P131
# 1.直接对属性值进行修改
# 求立方体的类
class Box1():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
# ===================================主程序调用Box1()类，并创建B1、B2实例
B1 = Box1()
print(B1.length)  # 读属性值
B1.length = 10  # 修改B1实例length属性值为10
print(B1.length)  # 打印修改后的值
B2 = Box1()  # 创建新实例B2
B2.length = 20  # 修改B2实例length属性值为20
print(B2.length)  # 打印修改后的值


# 2.通过方法对属性值进行修改
# 求立方体的类
class Box1():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
    def setNewLength(self,length1):  # 定义修改属性length的函数
        self.length = length1
# 主程序调用类及实例
b1 = Box1()  # 创建新实例b1
b1.setNewLength(15)  # 通过setNewLength(15)方法修改
print(b1.length)  # 打印修改后的值
'''


'''
# 7.2.3 把类赋值给属性    P132
# [案例7.2]把颜色类赋给颜色属性
class Color1():  # 颜色类Color1
    def __init__(self,index=0):  # index指定颜色列表下标
        self.set_color = ['white','red','black','green']  # 定义列表类颜色属性
        self.index = index  # 定义下标属性，为了可以在实例之间传递
    def setColor(self):
        return self.set_color[self.index]
# ====================================================================
# 求立方体的类
class Box1():  # 类名为Box1
    def __init__(self,length1,width1,height1,c1=0):  # 传递类参数的保留函数__init__
        self.length = length1
        self.width = width1
        self.height = height1
        self.color0 = Color1(c1).setColor()  # 颜色类Color1在此创建实例，并调用setColor()得到color0的值

    def volume(self):  # 求立方体体积函数volume()
        return self.length*self.width*self.height
# 主程序调用类及实例如下：
my_box1 = Box1(10,10,10,1)  # my_box1通过Box1类赋值建立对应的一个实例
print(my_box1.color0)  # 打印color0属性值
'''


'''
# [案例7.3] Box2子类通过继承Box1父类实现
# 求立方体的类
class Box1():  # 定义父类Box1
    def __init__(self,length1,width1,height1):
        self.length = length1
        self.width = width1
        self.height = height1
    def volume(self):
        return self.length*self.width*self.height
# =======================================================
class Box2(Box1):
    def __init__(self, length1, width1, height1):
      super().__init__(length1,width1,height1)
      self.color='white'
      self.material='paper'
      self.type='fish'
    def area(self):
        re = self.length*self.width+self.length*self.height+self.width*self.height
        return re*2
# =======================================================主程序调用类及实例
my_box2 = Box2(10,10,10)
print('立方体体积是%d'%(my_box2.volume()))
print('立方体表面积是%d'%my_box2.area())
print('Box颜色%s，材质%s，类型%s'%(my_box2.color,my_box2.material,my_box2.type))
'''


'''
# [案例7.4] 变量、函数私有化     P135
def TeatPrivate():
    def __init__(self):
        self.__say = 'ok'
    def p(self):
        print(self.__say)
# ==================================主程序调用实例如下
    show = TeatPrivate()
    show.p()
'''


'''
# 7.5.2 案例[把盒子类放到类模块中]    P136
# [案例7.5] 主程序代码文件，通过导入实现对独立类的使用
from Class_module import *  # 从Class_module模块文件导入所有类
myy_box2 = Box2(10,10,10)  # 通过使用Box2类创建my_box2实例
print('立方体体积是%d'%(my_box2.volume()))  # 通过实例调用volume()求体积，并打印
print('立方体表面积是%d'%my_box2.area())
print('Box颜色%s，材质%s，类型%s'%(my_box2.color,my_box2.material,my_box2.type))
'''


'''
# [案例7.6] 静态类的使用     P137
class Static():
    name = 'Tom'  # 类局部变量name，没有定义属性的说法
    age = 20  # 类局部变量age
    address = 'China'  # 类局部变量address
    call = 28680000  # 类局部变量call
    def a():
        i = 0
        i += 1
        print('第一个函数%d'%(i))
    def b(add=1):
        print('第一个函数%d'%(add))
    def c(add=1):
        print('第一个函数%d'%(add))
        return add
'''


# [案例7.7] 静态类的调用     P138
from Class_module import SHost
print(SHost.name)
print(SHost.age)
print(SHost.address)
print(SHost.call)
SHost.name = 'Jerry'  # 直接修改静态变量的值
print(SHost.name)  # 打印变量的name值


