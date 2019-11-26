"""
#  多个变量赋值   P23
one = two = therr = 10
print(one, two, therr)  # 函数允许多值打印输出，用逗号分隔变量
"""



"""
one,two,three=10,10,10
print(one,two,three)  #  print输出值也为连续的三个值
"""



"""
#   字符串   P24
name = 'Tom'  #  单引号字符串变量
name1 = "Jerry"  #  双引号字符串变量
name2 = '''Sreck'''  #  三引号字符串变量
print(name,name1,name2,'《Tome&Jerry》')  #  最后一项是直接使用字符串
#上述字符串变量赋值过程，也可以改为如下：
name,name1,name2 = 'Tom',"Jerry",'''Sreck'''  #一行多字符串变量赋值
print(name,name1,name2)
"""



"""
text1 = '''带格式的文本，往往含有特殊格式控制符号，如
制表符TAB(\t),又如  #  两个空格代替了\t
换行符[\n]'''       #  利用\n换行符，把]在另外一行独立显示出来
print(text1)  
"""



"""
#   字符串值合并   P26
name = 'Tom'
job = 'teacher'
record = name + ',' + job  #用加号合并三个字符串
print(record)              #打印合并后的字符串变量record
"""



"""
#   字符串值修改   P26
name = 'Three cool cat'
new_name = name[:11] + 'dogs'
print(new_name)
#name[6] = 'C'       解释器将报赋值错误
"""



"""
#获取字符串长度     P26
hello = 'Hello,三酷猫！' #  把一个汉字看作一个字符串长度
len(hello)               #  用len函数求字符串长度
print(len(hello))
"""



"""
#  r/R原始字符串控制符号   P26
print('C:\back\name')   #  字符串含特殊转义符号，\b和\n  若没有使用r情况下，\b转为了退格符，实现了退一格的效果
#  \n转为了换行符，实现其后字母的换行显示
print(r'C:\back\name')  #  在使用r符号情况下，字符串原样输出，特殊转义符不起作用

#  重复输出字符串(*)       P26
print('Cat'*2)  #  重复显示两个Cat，2*'Cat'与'Cat'*2等价

#  格式化字符串(%)         P27
age = 10
print("Tom's name is %d"%(age))  #  %d为格式化整数
"""


#  二进制
"""
bin(14)  #  bin()函数把十进制转为二进制
print(bin(14))  #  输出二进制的值0b1110
"""



"""
#  赋值运算符
x,y = 10,20
x + y
print(x + y)
x += y
print(x)
"""



