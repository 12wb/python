d_date1 = {'三酷猫':{'鲫鱼':[17,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]},'加菲猫':{'黑鱼':[8,16]},'大脸猫':{'草鱼':[12,8]}}
d_date2 = {'三酷猫':{'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]},'加菲猫':{'鲤鱼':[9,7.1]}}
d_date3 = {'三酷猫':{'乌龟':[1,78.10],'鲫鱼':[1,10.78],'草鱼':[5,7.92]},'大脸猫':{'鲫鱼':[8,9.8],'螃蟹':[5,15]}}
fish_records = {'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}  # 所有钓鱼记录
nums = 0
amount = 0
day = ''
print('=========每日钓鱼记录=========')
for day,day_record in fish_records.items():  # 循环获取每天记录(元组形式)
    if nums > 0:
       print('-----------------')
    day_nums = 0
    day_amount = 0
    print('%s钓鱼记录为:'%(day)) # 打印当天的日期
    for name1,get_fish_record1_d in day_record.items():  # 循环获取当天钓鱼记录
        print('    %s:'%(name1))  # 打印钓鱼者
        for name2,get_fish_record2_d in get_fish_record1_d.items():  # 获取鱼名和对应值(列表)
            day_nums += get_fish_record2_d[0]  # 当天数量累加
            day_amount += get_fish_record2_d[0]*get_fish_record2_d[1]  # 当天金额累加
            print('%s,数量%d,单价%.2f元'%(name2,get_fish_record2_d[0],get_fish_record2_d[1]))  # 打印名称，数量，单价
    print('%s钓鱼数量为%d,金额为%.2f元'%(day,day_nums,day_amount))  # 打印当天钓鱼数量，金额
    nums += day_nums  # 所有数量累加
    amount += day_amount  # 所有金额累加
print('=========统计结果打印=========')
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount))


