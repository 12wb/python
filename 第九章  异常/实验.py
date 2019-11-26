x = input('输入x:')
y = input('输入y:')
try:
    i = int(x)*int(y)
    print(i)
except:
    print('输入有错误，%s，%s'%(x,y))