"""
# clear()方法    P58
listColor = ['red',1,'green',2,'yellow',3]    
len(listColor)  # 获取元素
listColor.clear()
print(listColor)
len(listColor)
"""


"""
# pop()方法    P58
listpop = ['球1','球2','球3']  
get_one = listpop.pop()  # pop默认列表尾部操作
print(get_one,'',listpop)  # 打印元素和删除后的列表元素
get_one = listpop.pop(0)
print(get_one,'',listpop)
listpop.pop(2)  # 在listpop里试图弹出不存在的元素
"""


"""
# remove方法()   P58
listpop = ['球1','球2','球3','球2']  # 元素球2有两个
listpop.remove('球2')  # 删除左边第一个元素球2
print(listpop)
"""


"""
# del函数
listpop = ['球1','球2','球3','球2']
del(listpop[2])  # 删除下标为2的列表
print(listpop)
del listpop  # 删除listpop列表对象
listpop  # 调用listpop对象，调用后会出错并显示listpop没有被定义
"""


# 列表元素合并extend()方法     P59
# 方法1
"""team1 = ['张三','李四','王五']
team2 = ['Tom','jack','john']
team1.extend(team2)  # 把列表team2合并到列表team1中
print(team1)
"""


"""
# 方法2
team1 = ['张三','李四','王五']
team2 = ['Tom','jack','john']
id(team1)  # 获取team1的内存地址号
team1 = team1 + team2
id(team1)
print(team1)
"""


"""
# 示例一:用sort()方法实现增序，减序排列    P60
fruit = ['banana','pear','apple','peach']
fruit_1 = fruit.copy()  # 复制新列表fruit_1
fruit_1.sort()  # 对新列表元素进行增序排列
print(fruit_1)  # 打印增序排列，其排列结果是永久性，print后元素之间，首字母从小到大排序，增序。
fruit_h = fruit.copy()  # 对新列表元素进行减序排列
fruit_h.sort(reverse=True)  # 对新列表元素进行减序排列
print(fruit_h)  # 打印增序排列，其排列结果是永久性，print后元素之间，首字母从大到小排序，减序。
"""


"""
# 示例二:通过key()参数影响sort()排序规则     P60
listA = ['Tom,','tim','john','Jack']  # 元素首字母带大小写的列表
listA1 = listA.copy() # 复制一个新列表list
listA1.sort()  # 对listA元素进行默认排序
print(listA1)  # 执行后大写字母在前
listB = listA.copy() # 复制一个新列表listB
listB.sort(key=str.lower) # 先把大写转换为小写，再进行排序
print(listB)  # 执行后按照小写字母进行比较和增序排序
"""


"""
# count()方法:通过count()方法实现对列表指定元素的个数统计
vegtable = ['白菜','萝卜','青菜','芹菜','花菜','白菜']
vegtable.count('白菜')
print(vegtable.count('白菜'))
"""

"""
# reverse方法:通过reverse方法实现对列表元素的永久性反向记录
# 示例一:实现列表中数字元素反向记录
l_to_m = [9,8,7,6,5,4,3,2,1]
print(l_to_m)
l_to_m.reverse()  # 反向l_to_m中的所有元素
print(l_to_m)
"""

"""
# 示例二:实现列表中字符串元素反向记录
fruit = ['banana','pear','apple','peach']
fruit.reverse()  # 反向fruit中的所有元素
print(fruit)
"""


"""
# 列表解析
# 示例一:对集合0到10中，除了0外，其他元素做平方运算       P62
Nums = [i**2 for i in range(11)if i>0]  # i**2，对每个元素求平方，i in range迭代获取元素，if字句判断元素
print(Nums)
"""


"""
# 示例二:等价一般代码实现
Nums = []  # 定义空列表
for i in range(1,11):  # 循环获取1到10的元素
    Nums.append(i**2)  # 获取的每个元素求平方，存入列表
print(Nums)
"""
# 一个元素的元组定义及使用
"""
test3 = 1  # 给变量test3赋值      P68
type(test3)  # 用type函数检查test3对象类型
print(test3)
"""


"""
# 给元组赋一个元素应该这样使用    P68
test3 = ('ok，')  # 给test3变量赋一个元组元素，必须带逗号
type(test3)  # 用type函数检查test3对象类型
print(test3)
"""


"""
# 建立元组         P70
select_nums = (1,2,3,4,5)
select_Names = ('中国','美国','英国','法国','俄罗斯')
select_mix = ('中国',1,'美国',2,'英国',3,'法国',4,'俄罗斯',5)
select_nested = ('排名',select_nums)  # 元组作为元素
print(select_nested)  # 元组嵌套元组结果
list1 = ['OK']  # 定义列表
select_nested1 = ('排名',select_nums,list1)  # 列表作为元组的元素
print(select_nested1)  # 含列表的元组
"""


"""
# 循环查找某一个特定的元素
select_Names = ('中国','美国','英国','法国','俄罗斯')
for get_name in select_Names:  # 遍历select_Names对象元素
    if get_name == '法国':
        print('法国的下标是%d'%select_Names.index('法国'))
        break
"""


"""
# 统计元素
# 示例一：通过count()方法直接统计
nums = (1,5,7,5,0,3,5)
nums.count(5)  # 统计值为5的元素
print(nums.count(5))

# 示例二：通过len()函数统计
len(nums)
print(len(nums))  # 统计元组对象的元素个数

# 示例三：利用sum函数直接对元组求和
nums = (1,5,7,5,0,3,5)
sum(nums)
print(sum(nums))  # 利用Python内置函数sum求和

#示例四：统计元组所有元素的累计和
nums = (1,5,7,5,0,3,5)
sum1 = 0
for add in nums:
    sum1 = sum1 + add
    print('元组和为:%d'%(sum1))
"""


"""
# 合并元组
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)
"""

# 转换元组
# 示例一：列表转换为元组
list1 = ['Tom','John','Tim']
l_to_t = tuple(list1)  # 列表转元组
type(l_to_t)  # 获取l_to_t对象的类型

# 示例二：元组转换为列表
t_to_l = list(l_to_t)  # 把元组转为列表对象，在示例一的基础上执行
type (t_to_l)  # 获取t_to_l对象类型
print(t_to_l)
