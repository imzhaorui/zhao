import random
def line():
    print ("----------",end="")
def start_game():
    line()
    print ("欢迎来到勇者世界",end='')
    line()
    print ('\n')
    temp_name=input('尊敬的勇者，你的名字是：')
    return temp_name
def walk():
    line()
    print ("你遇到一个野怪",end="")
    line()
    temp=input("1=战斗")
    if temp=="1":
        return fight()
def fight():
    global HP
    temp_exp=0
    beast_level=level
    beast_attack=10+(3*beast_level)
    beast_defence=11+(1.5*beast_level)
    beast_HP=200+(10*beast_level)
    while HP>=0 and beast_HP>=0:
        line()
        print ("现在是你的回合了",end='')
        line()
        print ('\n')
        line()
        print ("你要做什么？",end='')
        line()
        temp=input("1=攻击")
        if temp=="1":
            hurt1=5*(attack-beast_defence+random.randint(0,5))
            beast_HP -=hurt1
            print ("你对野怪造成了",end="")
            print (str(hurt1),end="")
            print ("点伤害")
            hurt2=5*(beast_attack-defence+random.randint(0,5))
            temp_HP =HP-hurt2
            HP=temp_HP
        print ("野怪对你造成了",end="")
        print (str(hurt2),end="")
        print ("点伤害，你现在的HP为",end="")
        print(str(HP)) 
    line()
    print ("战斗结束",end="")
    line()
    print ('\n')
    if beast_HP>0:
        print ("你扑街")
    else:
        print ("野怪扑街")
        temp_exp=level*50
        print ("exp+"+str(temp_exp))
    HP=200+(10*level)
    print ("光之女神为你恢复了HP")
    return temp_exp
def person():
    global attack
    global defence
    global HP
    global player_id
    attack=10+(3*level)
    defence=11+(1.5*level)
    HP=200+(10*level)
    player_id="姓名："+player_name+"\n等级："+str(level)+"\n攻击："+str(attack)+"\n防御："+str(defence)+"\nHP："+str(HP)+"\nexp："+str(exp)

player_name=start_game()
print (player_name,'，真是一个响亮的名字')
exp=0
level=old_level=1

while 1:
    person()
    level=int (level+(exp/200))
    if old_level !=level:
        old_level=level
        exp=0
        person()
        print ("你的等级提升到了lv "+str(level))
        print (player_id)
    line()
    print ("请问你要做什么呢：",end='')
    line()
    temp=input("1=赶路，2=查看个人信息，3=退出游戏")
    if temp=="1":
        exp=walk()+exp
    elif temp=="2":
        print(player_id)
    elif temp=="3":
        break
    else:
        line()
        print ("请输入正确的内容",end="")
        line()
        print ('\n')
        continue
    person()

