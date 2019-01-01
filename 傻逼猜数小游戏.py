import random
print ('这是我给一个傻逼写的一个傻逼小游戏')
print ("游戏开始后电脑会自动生成一个0到100之间的数")
print ('输入你猜的数后如果猜错了屏幕会显示范围')
print ("如果猜对了程序自动关闭")
r=random.randint(0,101)
da=[100]
xiao=[0]
while 1:
    g=int(input())
    if g>r:
        da.append(g)
        print (str(max(xiao))+"-"+str(g))
    elif g<r:
        xiao.append(g)
        print (str(g)+"-"+str(min(da)))
    else:
        break
