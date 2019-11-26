"""
#  while循环  P41
#  示例一
i = 0
while i < 3:
    i += 1  # i做加1运算
print(i) 
"""
"""
#  示例二(嵌套)
i,j = 0,2  # 循环2次，第三次终止循环
while i < 2:  # 循环2次，打印2次
    while i < j:
        print("%d,"%((i+1)*j))
        j = 1
        i += 1  # 该行仅受第一个while控制，通过缩进格式对齐控制代码行范围。如果把i+=1控制语句去掉，程序将进入无限循环状态或发生内存溢出等问题。
"""


"""
#  for循环  P44
#  示例一:利用自定义集合对象实现for循环
fish_record = '鲫鱼5条，鲤鱼8条，鲢鱼7条，草鱼2条，黑鱼6条，乌龟1只'
i = 0
for var in fish_record:  # 循环一次var获取一个字符。一个汉字为一个双字节字符
    if var == '条':
        i = i+1
        print(i)
"""
"""
# 示例二:利用内建范围函数range实现for循环  P44
for i in range(9):  # range(9)为0到9的有序集合
    if i!= 0:  # 0既不是奇数也不是偶数
        if i%2==0:
            print('%d是偶数'%(i))
"""
"""
# 示例三:range函数另一种用法  P45
for i in range(1,5,2):  # 1为开始值，5为结束值，2为循环时数字递增的步长
    print(i)
"""


"""
# 循环控制语句  P45
# 示例:利用break语句，实现高效率的循环查找过程。  P46
cm = 'Tom,Jerry,Sreck!'
for i in range(len(cm)):
    print('for循环%d次'%(i+1))  # 检查循环次数
    if cm [i:i+3]=='Tom':  # 条件判断
        print('Tom is %d'%(i))
        break  # 跳出for循环
    print('for继续循环吗？%d次'%(i+1))
"""
"""
# 示例:求9以内的偶数      P47
for i in range(1,9):
    if i%2!= 0:  # 判断是否为偶数
        continue  # 非偶数直接返回到for循环开始位置，继续下一个循环
    print('%d是偶数.'%(i))
"""


"""
# 复杂条件及处理     P47
#  成员运算符
# 示例一:三酷猫找乌龟改进(字符串成员集合)
fish_record = '鲫鱼5条，鲤鱼8条，鲢鱼7条，草鱼2条，黑鱼6条，乌龟1只'
if '乌龟' in fish_record:  # 乌龟在字符串集合里，in运算结果是True
    print("乌龟在字符串里！")  
else:
    print("乌龟不在字符串里")
"""
"""
# 示例二:数字序列成员判断
if 2 not in range(10):  # 2不在0到9的序列里，值为True
    print("2不在集合里！")  # 上一行，值为True，执行本行
else:                   # 2在0到9的序列里，值为False，执行else下的子代码
    print("2在集合里！")
"""
"""
# 身份运算符   P48
# 示例一:身份运算符作为条件判断使用
t1 = '乌龟'
t2 = '乌龟'
if t1 is t2:
    print('俩只乌龟来自一个地址！')
"""
"""
# 求10的因数
i = 1
result = ''
total = 0
while i <= 10:
    if 10 % i == 0:
        result = result+str(i)+','
        total += i
    i += 1
    print('10的所有因数为%s，因数累加和为%d'%(result,total))
"""












