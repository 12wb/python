# 1 求2000年3月1日与1961年10月15日相差几天？
from datetime import datetime,date,time
date1 = date(1999,1,20)
date2 = date(2019,5,21)
print('%s与%s相差'%(date1.ctime(),date2.ctime()),date1-date2)
# 2 求上午8:50:18与下午2:0:7相差多少秒
time1 = time(8,50,18)
time2 = time(14,0,7)
print(datetime.combine(date1,time2)-datetime.combine(date1,time1))
tt = datetime.combine(date1,time2)-datetime.combine(date1,time1)
print(tt.total_seconds())