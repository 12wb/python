num1,num2,num3 = 5,6,9  #  定义三种鱼数量的数字变量并赋予初始值
price1,price2,price3 = 8.1,8.2,8  #  定义三种鱼单价变量并赋予初始值
fish1,fish2,fish3 = '鲫鱼','鲤鱼','草鱼'  #  定义三种鱼的名称变量并赋予初始值
date = '2017年12月'                       #  定义日期字符串变量
Total_Num = num1+num2+num3  #  总的鱼数
Total_Amount = num1*price1+num2*price2+num3*price3  #  总金额
print("----"*4+"三酷猫记账单"+"----"*4)   #  打印记账单第一行
print('钓鱼地点'+'钓鱼日期'+'     鱼名'+'数量(条)    '+'单价(元)')  #  打印记账单第二行
print('左小河    '+date+'1日  '+fish1+' '+str(num1)+'     '+str(price1))  #  打印记账单第三行
print('右小河    '+date+'2日  '+fish2+' '+str(num2)+'     '+str(price2))  #  打印记账单第四行
print('长江      '+date+'3日  '+fish3+' '+str(num3)+'     '+str(price3))  #  打印记账单第五行
print("----"*10+'---')  #  打印记账单第六行
print('鱼数总计%d条，市场价格总计%.2f元，每天平均钓鱼数量约%d条(%f条)'%(Total_Num,Total_Amount,int(Total_Num/3),Total_Num/3))  #  打印记账单第七行
print('鱼的平均价格%f，%.2f,%d'%(Total_Amount/Total_Num,Total_Amount/Total_Num,Total_Amount/Total_Num))   #  打印记账单第八行
print('记账日期:2018年10月18日，记账人:三酷猫')
