nums = 0  # 统计数量变量
amount = 0  # 统计金额变量
i = 0  # 循环控制变量
fish_records = ['1月1日','鲫鱼',18,10.5,'1月1日','鲤鱼',8,6.2,'1月1日','鲢鱼',7,4.7,'1月2日','草鱼',2,7.2,'1月2日','鲫鱼',3,12,'1月2日','黑鱼',6,15,'1月3日','乌龟',1,71,'1月3日','鲫鱼',1,9.8]
print('钓鱼日期名称数量单价(元)')
print('-----------------------------')
while i < len(fish_records):
    nums = nums + fish_records[i+2]  # 累计数量
    amount = amount + fish_records[i+2]*fish_records[i+3]  # 累计金额
    print('%s,%s,%.2f,%.2f'%(fish_records[i],fish_records[i+1],fish_records[i+2],fish_records[i+3]))
    i = i+4  # 循环控制
print('-----------------------------')
print('         总数:%d,总金额%.2f元'%(nums,amount))

