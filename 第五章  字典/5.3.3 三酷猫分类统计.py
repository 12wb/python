d_date1 = {'鲫鱼':[17,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}
d_date2 = {'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}
d_date3 = {'乌龟':[1,78.10],'鲫鱼':[1,10.78],'草鱼':[5,7.92]}
fish_records = {'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}
nums = 0  # 钓鱼总数量初始化定义
amount = 0  # 钓鱼总金额初始化定义
day = ''  # 日期记录变量初始化定义
day_record = {}  # 钓鱼每天记录字典初始化定义
stat_record = {}  # 统计记录初始化定义
name_n = ''  # 最大数量的鱼
max_nums = 0  # 数量
name_a =''  # 金额的鱼
max_amount = 0  # 金额
print('=========每日钓鱼记录=========')
for day,day_record in fish_records.items():  # 循环获取每天记录(元组形式)
    print('%s钓鱼记录为:'%(day))  # 打印当天日期
    for name,sub_recods in day_record.items():  # 循环获取当天鱼与数量，单价关系的记录
        nums += sub_recods[0]  # 数量累加
        amount += sub_recods[0]*sub_recods[1]  # 金额累加
        print('      %s数量%d,单价%.2f元' % (name, sub_recods[0], sub_recods[1]))

        if name in stat_record:  # 判断鱼是否在统计字典里，存在，则做累计处理
            stat_record[name][0] += sub_recods[0]  # 每种鱼数量累计
            stat_record[name][1] += sub_recods[0]*sub_recods[1]  # 每种鱼金额累计
        else:
            stat_record[name] = [sub_recods[0],sub_recods[0]*sub_recods[1]]  # 第一次累计，直接在字典里赋值
print('=====按鱼进行数量,金额统计=====')
for name1,get_L in stat_record.items():
    print('%s的总量%d,金额为%.2f元'%(name1,get_L[0],get_L[1]))  # 打印鱼统计情况
    get_nums_d = {name1:get_L[0]}  # 取最大鱼数量
    if get_L[0] > max_nums:  # 找最大数量的鱼
        name_n = name1
        max_nums = get_L[0]
    get_amount_d ={name1:get_L[1]}
    if get_L[1] > max_amount:  # 最大金额的鱼
        name_a =name1
        max_amount = get_L[1]
print('====最大值,总数量,总金额统计====')
print('最大数量的鱼是%s,%d条'%(name_n,max_nums))  # 印最大数量的鱼
print('最大金额的鱼是%s,%.2f元'%(name_a,max_amount))  # 印最大金额的鱼
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount))  # 印总数量，总金额
