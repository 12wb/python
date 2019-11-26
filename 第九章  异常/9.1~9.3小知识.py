'''
# 捕捉异常示例     P164
# [案例9.1] 给函数加上出错捕捉机制
def print_D(dic):
    i = 0
    try:  # 捕捉机制开始
        len1 = len(dic)
        while i < len1:
            print(dic.popitem())
            i+=1
    except:  # 捕捉异常信息
        print("传递值类型出错，必须为字典型！")  # 给出友好的提示
# ===============================================调用print_D函数如下
print_D({1:'a',2:'b'})  # 正常字典类型
print_D([1,2,3])  # 传入错误对象
'''


'''
# 带finally子句的异常处理      P165
# 示例一:
try:
    1/0  # 除数为零错误
except:  # 捕捉异常
    print("除数不能为零")  # 给出错误异常提示
finally:  # 执行finally字句
    print("程序执行结束")  # 打印程序结束提示信息
'''


'''
# 示例二:
try:
    print(1/2)
except:  # 捕捉异常
    print("除数不能为零")  # 给出错误异常提示
finally:  # 执行finally字句
    print("程序执行结束")  # 打印程序结束提示信息
'''


'''
# 示例三:演化强制执行finall子句的效果    P166
import sys
try:
    1/0
except:
    print("除数不能为零")
    sys.exit()
finally:
    print("程序执行结束！")
print("我能执行吗？")
'''


# 捕捉特定异常信息
# 示例一:指定一个特定出错类     P167
try:
    i+=1  # i没有预先定义，将出错
except NameError:  # 确定是对象没有定义出错
    print("i变量名先要初始定义，才能做自增运算！")  # 出错提示


# 示例二:指定多个特定出错类     P167
try:
    i+=1
except (NameError,TypeError):
    print("i变量名先要初始定义，才能做自增运算！")  # 出错提示


# 抛出异常
# 示例一:带参数的触发     P168
i = '1'  # 字符串
if type(i)!=int:  # 判断是否为整型
    raise TypeError('i类型出错！')