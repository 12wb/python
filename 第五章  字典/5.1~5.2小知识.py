"""
# 字典键值具有唯一性         P77
d3 = {1:'car',2:'bus',2:'bus'} # 定义字典变量，其中两个键值一样
len(d3)  # 字典对象把重复的元素归成了一个
print(len(d3))
"""

"""
# 利用赋值给字典添加元素        P78
d1 = {'Tom':2,'Jim':5}
d1['Mike'] = 8  # 字典变量添加新元素"Mike:8
print(d1)
"""

"""
# 利用setdefault()方法给字典增加元素     P79
d1 = {'Tom':2,'Jim':5,'Mike':9}
d1.setdefault('Alice',10)
d1.setdefault('tim')  # 未指定值
print(d1)
"""

"""
# 字典值查找      P79
# 字典名 + [Key]查找
d2 = {'red':1,'green':2,'yellow':3}
print(d2['green'])  # 打印键为"green的值，如果指定了一个不存在的值，则会报错

# 利用get()方法查找      P79
d2 = {'red':1,'green':2,'yellow':3}
d2.get('green')  # 通过get()方法获取green的值，如果指定了一个不存在的值，则会显示空值
print(d2['green'])
"""

"""
# 字典值修改
# 利用赋值修改键对应的值     P80
d1 = {'Tom':2,'Jim':5,'Mike':8}
d1['Mike'] = 9  # 对已经存在的键Mike赋新值9
print(d1)

# 利用update()方法修改键对应的值    P80
# 更新字典里键对应的值
d1 = {'Tom':2,'Jim':5,'Mike':8}
d2 = {'Tom':10,'Mike':11}
d1.update(d2)
print(d1)

# 新增键值对     P80
d1.update({'Jack':12})
print(d1)
"""

"""
# 字典元素的删除
# 利用del函数删除      P81
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
del(d1['Jim'])
print(d1)

# 利用pop()方法删除     P81
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
p1 = d1.pop('Mike')
print(d1)

# 利用popitem()方法删除      P81
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
k1,v1 = d1.popitem()  # 随机删除并返回一个键值对
print(k1,v1)  # 执行k1，v1(其实以元组形式)
print(d1)
t1 = d1.popitem()  # 随机删除并返回一个键值
print(t1)
type(t1)
print(type(t1))  # 显示元组类型
"""

"""
# 字典遍历操作
# 遍历所有键值对     P82
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
for get_L in d1.items():  # 循环获取元组
    print(get_L)  # 问题：为什么打印后会自动换行


d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
d1.items()
type(d1.items)
print(type(d1.items))  # 结果是一个功能或方法类

# 遍历所有键     P82
# 利用字典变量循环遍历
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
for gets in d1:  # 循环获取字典的键
    print(gets)

# 利用key()方法获取字典键     P82
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
for gets1 in d1.keys():
    print(gets1)

# 遍历所有值      P82
# 通过键遍历值
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
for get_key in d1:  # 循环获取字典的值
    print(d1[get_key])

# 通过valuse()方法获取字典值     P83
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
for get_v in d1.values():  # 循环获取字典所有值
    print(get_v)
"""

"""
# 字典其他操作方法
# in成员操作     P83
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
if'jim' in d1.keys():  # 判断Jim是否在key()获取的集合内
    print('Jim在键集合内！')
else:
    print('Jim不在键集合内！')

# clear()方法    P83
d5 = {'OK':1,'莫名其妙':2,222:3}
d5.clear()  # 清空字典变量d5里的所有元素
print(d5)

# copy()方法     #P83
d6 = {'八宝粥':13.5,'小米粥':5,'皮蛋粥':8}
d7 = d6.copy()
id(d6)
print(id(d6))
id(d7)
print(id(d7))
d8 = d7
id(d8)
print(id(d8))
d6['小米粥'] = 4.8
print(d6)
print(d7)
del(d6['皮蛋粥'])
print(d6)
print(d7)  # 显示d7元素不受d6删除元素影响

# fromkeys()方法      P84
d8 = {}.fromkeys(['pen','rule','paper'])  # formkeys(）指定相关键生成空值字典
print(d8)
"""

"""
# 字典嵌入字典        P85
no1 = {'张三':35.5,'李四':200,'王五':800}
no2 = {'Tom':99.8,'John':183,'Jim':429}
no3 = {'阿毛':12,'阿狗':33}
rest = {'1号':no1,'2号':no2,'3号':no3}  # 字典键对应的值都为字典的rest
print(rest)
total = 0  # 金额累计初始变量
for get_values in rest.values():  # 循环获取字典型的值
    total = total + sum(get_values.values())  # 获取并统计字典值
    print('餐厅今天营业额为:%.2f'%(total))
"""

"""
# 列表嵌入字典        P85
L1 = [35.5,200,800]
L2 = [99.8,183,429]
L3 = [12,33]
rest1 = {'1号桌消费':L1,'2号桌消费':L2,'3号桌消费':L3}  # 列表嵌入字典
print(rest1)
for get_k,get_L in rest1.items():  # 循环获取字典元素(元组形式)
    print('%s:%.2f元'%(get_k,sum(get_L)))  # sum函数统计每桌消费金额，并打印
"""

# 字典嵌入列表       P86
no1 = {'张三':35.5,'李四':200,'王五':800}
no2 = {'Tom':99.8,'John':183,'Jim':429}
no3 = {'阿毛':12,'阿狗':33}
list1 = [no1,no2,no3]  # 字典对象嵌入列表变量中
print(list1)
i = 0  # 循环控制变量初始化
total =0  # 消费总额变量初始化
r_L = len(list1)  # 获取list1变量的元素个数
get_d = {}  # 定义一个空的字典变量
sum1 = 0  # 每桌的消费总额变量初始化
while i < r_L:  # 循环开始
    get_d = list1[i]  # 获取下标为i的列表元素(一个字典)
    sum1 = sum(get_d.values())  # 对获取字典的所有值进行求和并赋值
    total += sum1  # 进行总金额累加求和
    print(get_d)
    print('第%d桌日消费:%.2f元'%(i+1,sum1))
    i += 1  # 循环控制增1
    print('该餐厅日消费总额为:%.2f元'%(total))