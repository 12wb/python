n = int(input("请输入数字："))
ans = 0
for i in range(1, n+1):
    t = i
    ok =False
    while t>0:
        g = t % 10
        if g==2 or g==0 or g==1 or g==9:
            ok = True
        t = t // 10
    if ok:
        ans += i
print(ans)
