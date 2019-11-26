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


class SHost():
    name = 'Tom'  # 类局部变量name，没有定义属性的说法
    age = 20  # 类局部变量age
    address = 'China'  # 类局部变量address
    call = 28680000  # 类局部变量call
