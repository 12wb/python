fish_records = [18,8,7,2,3,6,1,1]
i = 0  # 循环控制变量
compare = 0  # 比较元素初始值
fish_len = len(fish_records)  # 获取列表长度
while i < fish_len:
    j = 1  # 循环控制变量
    while j < fish_len-i:  # 循环一遍，长度减1
        if fish_records[j-1] > fish_records[j]:  # 比较前后两元素哪个大
            compare = fish_records[j-1]  # 前一个大的放到临时比较变量里
            fish_records[j-1] = fish_records[j]  # 把小的元素放到前面
            fish_records[j] = compare  # 把临时变量里的大元素放到后面
        j += 1  # 内循环控制变量加1
    i += 1  # 外循环控制变量加1
print(fish_records)
