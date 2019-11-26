class Car():
    def __init__(self,brand,age):
        self.brand = brand
        self.age = age
    def shuchu(self):
        print(self.brand + '有' +str(self.age) + '岁了 ')

    def __del__(self):  # 析构函数
        print(self.brand + '报废了')
zhaoba = Car('宝马',10)
lisi = Car('劳斯莱斯','8')
zhangsan = Car('奔驰','5')
lisi.shuchu()
zhangsan.shuchu()
zhaoba.shuchu()












