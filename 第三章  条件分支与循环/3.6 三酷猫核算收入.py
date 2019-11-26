fish_record = '鲫鱼5条，鲤鱼8条，鲢鱼7条,草鱼2条，黑鱼6条，乌龟1只'
fish_price = '8,5,3,2,9,8'  # 单位:元
num1 = 0
sum1 = 0
Amount = 0
i = 0
while i < len(fish_price)/2:
    num1 = int(fish_record[2+i*5])
    sum1 = sum1 + num1  # 水产品数量累计
    Amount = Amount+int(fish_price[i*2])*num1  # 收入累计
    i += 1  # 循环增1的控制语句                                 
    print('三酷猫钓上水产品数为%d，预计收入%d元。'%(sum1,Amount))

