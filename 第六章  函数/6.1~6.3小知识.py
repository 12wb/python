"""
# 案例[6.1]不带参数求因数函数案例     P100
def factor_no_para():  # 不带参数的求因数的自定义函数
    i = 1
    nums =10
    print('%d的因数是:'%(nums))
    while i <= nums:  # 循环求10的因数
        if nums%i == 0:  # 能整除10的整数是10的因数
            print('%d'%(i))  # 打印因数
        i+=1
# ==============================自定义函数体结束,下面为调用自定义函数
factor_no_para()  # 调用自定义函数
tt = type(factor_no_para)  # 检查是否是函数类型
print(tt)
# ==============================自定义函数执行结果如下:
"""


"""
# 案例[6.2]带参数求因数函数案例      P101
def find_factor(nums):  # 带参数nums的求因数的自定义函数
    i = 1
    str1 = ''
    print('%d的因数是:'%(nums))
    while i <= nums:  # 循环求参数nums传递值的因数
        if nums%i == 0:
            str1 = str1+' '+str(i)  # 用字符串循环记录一个整数的因数
        i += 1
    print(str1)
# ====================================
num2_L = [10,15,18,25]  # 定义四个整数的列表
i = 0
num_len = len(num2_L)
while i < num_len:
    find_factor(num2_L[i])  # 循环调用find_factor(nums)
    i += 1
"""


"""
# return语句在函数中除了返回值外,还起中断函数执行作用     P102
def test_re():
    return 1
    print("OK")
print(test_re())  # 问题？运行结果跟平常不一样
"""


"""
# [案例[6.3]带返回值的求因数函数案例      P102
def find_factor(nums):  # 带参数nums的求因数的自定义函数
    i = 1
    str1 = ' '
    while i <= nums:  # 循环求参数nums传递值的因数
        if nums%i == 0:  # 能整除nums的整数是nums的因数
            str1 = str1 + ' ' + str(i)
        i += 1
    return str1  # 返回因数字符串
# ===================================调用自定义函数
num2_L = [10,15,18,25]  # 定义四个整数列表
i = 0
num_len = len(num2_L)
return_str = ''
while i < num_len:
    return_str = find_factor(num2_L[i])  # 循环调用find_dactor(nums),并返回因数字符串
    print('%d的因数是:%s'%(num2_L[i],return_str))  # 打印正整数求因数结果
    i += 1
"""  # 问题？  案例6.3跟6.2运行结果中为什么案例6.2实现了换行显示


"""
# 自定义函数的完善,[案例6.5(建立函数模块)]      P105
def find_factor(nums):  # 带参数nums的求因数的自定义函数
    '''
    find_factor('a')
    nums是传递一个正整数的参数
    以字符串形式返回一个正整数的所有因数'''  # 用一个三个单引号来包括描述文档
    if type(nums)!=int:  # 不是整数,提示出错,并终止函数执行
        print('输入值类型出错,必须是整数!')  # 提示传递值类型出错
        return   # 终止函数执行
    if nums <= 0:
        print('输入值范围出错,必须正整数!')
    i = 1
    str1 = ' '
    while i <= nums:  # 循环求nums传入值的因数
        if nums % i == 0:  # 求传入值的因数
            str1 = str1 + ' ' + str(i)
        i += 1
    return str1  # 返回因数
"""

"""
# 位置参数          P108
# 示例一:两个固定参数的自定义函数调用
def test1(name,age):  # 带两个固定参数
    print('姓名%s,年龄%s'%(name,age))
test1('Tom',11)  # 调用函数时，所传值必须与参数对应上
"""

"""
# 关键字参数              P108
# 关键字参数对应指定
def test1(name,age): 
    test1(name='John',age=20)  # 所有参数都用“参数名=值”的方式指定
    test1(age=20,name='John')
    test1('John',age=20)
    # test1(name='John',20) # 该指定调用将出错，不支持左边指定，右边不指定方式
"""


"""
# 示例四:传递西瓜的多特征属性值     P110
def watermelon(name,*attributes):  # 带*的为可以传递任意数量值的参数
    print(name)
    print(type(attributes))  # 验证attributes的类型，打印结果显示为元组型
    description = ''
    for get_t in attributes:  # 暗示是以集合类型进行操作
        description+=''+get_t  # 形成字符串属性说明内容
    print(description)
# 调用自定义函数watermelon
watermelon('西瓜','甜','圆形','绿色')  # 调用自定义函数，任意参数传3个值
print('------------------')
watermelon('西瓜','甜','圆形','绿皮','红瓤','无籽')  # 任意参数传5个值
"""


"""
# 示例五:传递西瓜的多特征属性  “键=值”        P110
def watermelon(name,**attributes):  # 带**的为可以传递任意数量“键=值”的参数
    print(name)
    print(type(attributes))  # 验证attris的类型
    return attributes  # 返回字典类型对象
# 调用自定义函数watermelon
print(watermelon('西瓜',taste='甜',shape='圆形',color='绿色'))
"""


"""
# [案例6.6] 用元组形式传递西瓜的特性         P111
# 传递元组
def watermelon(name,attributes):  # 自定义函数，传递元组，列表，字典
    print(name)
    print(type(attributes))  # 验证attris的类型
    return attributes
get_t = watermelon('西瓜',('甜','圆形','绿色'))  # 调用自定义函数，带元组传递
print(get_t)  # 打印元组

# 传递列表
get_L = watermelon('西瓜',['甜','圆形','绿色'])
print(get_L)

# 传递字典
attri = {'taste':'甜','shape':'圆形','color':'绿色'}  # 定义字典变量
get_D = watermelon('西瓜',attri)  # 传递字典对象
print(get_D) # 打印返回的字典对象
"""


"""
# [案例6.7]            P112
# 在自定义函数内部修改直接传递的列表元素，会影响函数外面的列表对象
def EditFrult(name,attributes):  # attributes将用于传递列表对象
    attributes[0] = attributes[0]*0.9  # 打九折，修改列表对象
    return attributes  # 返回修改后的列表对象
# 调用EditFrult函数如下：
attri_L = [21,'甜','圆形','绿色']  # 21为原价格
#get_L = EditFrult('西瓜',attri_L)  # 调用EditFrult，并返回修改后的列表
#print(get_L)  # 打印返回的列表对象
print(attri_L)  # 打印原始列表对象

# 调用EditFrult函数改成如下方式
get_L =EditFrult('西瓜',attri_L.copy())  # 利用列表copy()方法实现对象的复制
print(get_L)
"""


"""
# 函数与变量作用域
# 全局变量与局部变量
# 示例一:演示全局变量与局部变量的作用范围      P113

j = 5  # j为全局变量，在定义并赋值时确定
def suml(i):  # i在函数第二行被赋值，明确为内部局部变量
    i = i+j  # j全局变量可以被函数内部访问
    return i
i = 8  # i在函数外面被赋值，非函数内部的i
print('j值为%d，是全局变量；i值为%d是局部变量'%(j,suml(5)))  # 打印执行结果
print('函数外面的i值为%d，是新的变量，而非函数内的i'%(i))  # 打印外面i
"""


"""
# 示例二:全局变量在函数体里用global关键字声明后才能用于修改操作       P114
j = 5  # 全局变量j
k = 2  # 全局变量k
def suml():
    global j  # 声明j为全局变量
    j = j + 5  # 全局变量加5，j变成了新的局部变量
    k = 4  # 新定义了局部变量k，其值为4
    return k
print('全局变量j的值还是为%d，不受新局部变量j的影响'%(j))
print('全局变量k的值为%d，函数返回局部变量k的值为%d'%(k,suml()))
"""


"""
# 示例三:闭包变量的使用        P114
j = 5  # 全局变量j
def sum0():  # 外部函数sum0
    k = 2  # 闭包变量k
    def suml():  # 嵌套内部函数suml
        #nonlocal k  # 声明后k为suml()的局部变量
        #k = j + 5
        i = k + j  # 局部变量i
        return i
    return suml()
print('调用sum0结果%d'%(sum0()))
"""


"""
# 匿名函数定义及特点
# 代码示例           P115
lambda x,y:x*y  # 在同一行定义匿名函数
print(lambda x,y:x*y)
a = lambda x,y:x*y  # 定义匿名函数并赋值给a
a(2,3)  # a具有匿名函数功能，通过参数传递
print(a(2,3))  # 输出匿名函数俩数相乘结果为6
"""


"""
# 使用递归函数        P116
# [案例6.8]求1，2.3，...，n加法
def recursion_sum(num):  # 定义递归函数
    if num == 1:  # 分解到最小数1
        return num  # 返回最小数1给上一层
    return recursion_sum(num-1)+num  # 自己调用自己，重复动作：两个相邻数相加
# 调用递归函数
print(recursion_sum(4))


# 对应的一般循环实现过程如下：        P116
def suml(num):
    i = 1
    add = 0
    while i <= num:
        add = add + i
        i += 1
    return add
print(suml(4))
"""

"""
# [案例6.9]跟踪递归函数在内存中开辟新地址的情况
def recursion_sum(num):  # 定义自定义递归函数
    if num == 1:  # 分解到最小数1
        return num  # 返回最小分解数1给上一层
    tt = recursion_sum(num-1)+num  # 自己调用自己，重复动作，两个相邻数相加
    print('第%d次递归'%(num))  # 用print跟踪递归次数
    print('返回值%d在内存中地址:%d'%(tt,id(tt)))  # 跟踪递归过程变量地址的变化
    return tt  # 返回递归结果
# 调用递归函数
print(recursion_sum(10))  # 调用递归函数对1，2，...，10进行累加
"""


# 利用递归函数实现二分法查找     P118
# [案例6.10]二分法查找
def r_dichotomy(nums,find,left,right):  # 二分法查找，自定义递归函数
    middle = (right+left)//2  # 求商的整数，取中间值的下标
    if nums[middle]==find:  # 找到列表中的值
        return middle  # 返回值对应的下标
    if right == left+1:  # 若指定范围只有一个未找元素
        if nums[middle]!=find:  # 而且没有找到
            return -1  # 返回-1，-1代表没有找到
    if nums[middle] > find:  # 值的查找范围在[left,middle]之间
        return r_dichotomy(nums,find,left,middle)  # 在左边递归查找
    elif nums[middle] < find:  # # 值的查找范围在[middle,right]之间
        return r_dichotomy(nums,find,middle+1,right)  # 在右边递归查找
# 调用递归函数代码如下:
nums_L = [1,2,3,4,8,16,20,30]  # 必须提供排序的列表，才能供二分法使用
print(r_dichotomy(nums_L,2,0,len(nums_L)))  # 在列表里查找值为2的元素的下标