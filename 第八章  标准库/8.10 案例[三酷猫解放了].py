# [案例8.2] 用标准库函数实现钓鱼记账统计   P159
nums = [17,8,7,2,3,6,1,1,5]  # 记录钓鱼数量列表
price = [10.5,6.2,4.7,7.2,12,15,78.1,10.78,7.92]  # 记录鱼价格列表
amount = sum(nums)  # 用sum函数统计总鱼数量
total_1 = [x*y for x,y in zip(nums,price)]  # 用zip函数加列表解析生成新列表
print('总共钓鱼%d条，总共预计金额%0.2f元'%(amount,sum(total_1)))