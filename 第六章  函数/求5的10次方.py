# 自定义函数求
def recursion_power(num):  # 定义递归函数
    if num == 1:  # 分解到最小数1
        return 5  # 返回最小分解数1给上一层
    return recursion_power(num-1)*5  # 自己调用自己，重复动作：两个相邻数相乘
# 调用递归函数：
print(recursion_power(10))


# 一般循环方法求
i = 2
num = 5
while i <= 10:
    num = num*5
    i += 1
print("5的10次方是%d"%(num))

