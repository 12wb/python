d_date1 = {'鲫鱼':[18,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}
d_date2 = {'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}
d_date3 = {'乌龟':[1,71],'鲫鱼':[1,9.8],'草鱼':[5,7.2],'黄鱼':[2,40]}
fish_records = {'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}
d_date1['鲫鱼'] = [17,10.5]  # 修改键'鲫鱼'对应的值
del(d_date3['黄鱼'])  # 删除键'黄鱼'指定的元素
for get_name,get_L in d_date3.items():  # 1月3日所有单价都上浮10%
    get_L[1] = get_L[1]*1.1  # 把列表对应的单价乘以1.1，并修改列表单价
    d_date3[get_name] = get_L  # 修改字典变量对应的值
nums = 0
amount = 0
day = ''
day_record = {}
for day,day_record in fish_records.items():
    print('%s钓鱼记录为:'%(day))
    for name,sub_recods in day_record.items():
        nums += sub_recods[0]
        amount += sub_recods[0]*sub_recods[1]
        print('      %s数量%d,单价%.2f元'%(name,sub_recods[0],sub_recods[1]))
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount))