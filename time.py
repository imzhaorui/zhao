import pyautogui as pag
import time
list1=[]
while 1:
    a=input("输入分钟数回车，输入q回车结束")
    if a=="q":
        break
    else:
        temp=int(a)+1
        list1.append(temp*12)
lens=len(list1)-1
s=pag.confirm('Are you sure to start?')
if s=="OK":
    i=0
    n=0
    while 1:
        while i<list1[n]:
            time.sleep(5)
            tanchuang1=pag.pixelMatchesColor(1346,529,(153,153,153))
            tanchuang2=pag.pixelMatchesColor(1346,551,(153,153,153))
            tanchuang3=pag.pixelMatchesColor(575,569,(153,153,153))
            tanchuang4=pag.pixelMatchesColor(575,494,(153,153,153))
            tanchuang5=pag.pixelMatchesColor(575,570,(153,153,153))
            if tanchuang1 and tanchuang2 and tanchuang3 and tanchuang4 and tanchuang5:
                pag.moveTo(949,601)
                pag.click()
                time.sleep(1)
                tanchuang1=pag.pixelMatchesColor(1346,529,(153,153,153))
                tanchuang2=pag.pixelMatchesColor(1346,551,(153,153,153))
                tanchuang3=pag.pixelMatchesColor(575,569,(153,153,153))
                tanchuang4=pag.pixelMatchesColor(575,494,(153,153,153))
                tanchuang5=pag.pixelMatchesColor(575,570,(153,153,153))
                if tanchuang1 and tanchuang2 and tanchuang3 and tanchuang4 and tanchuang5:
                    pag.moveTo(949,758)
                    pag.click()
                    tanchuang1=pag.pixelMatchesColor(1346,529,(153,153,153))
                    tanchuang2=pag.pixelMatchesColor(1346,551,(153,153,153))
                    tanchuang3=pag.pixelMatchesColor(575,569,(153,153,153))
                    tanchuang4=pag.pixelMatchesColor(575,494,(153,153,153))
                    tanchuang5=pag.pixelMatchesColor(575,570,(153,153,153))
                    if tanchuang1 and tanchuang2 and tanchuang3 and tanchuang4 and tanchuang5:
                        m=510
                        while not pag.pixelMatchesColor(949,m,(125,126,128)):
                            m+=1
                        pag.moveTo(949,m)
                        pag.click()
            else:
                i+=1
        pag.moveTo(180, 958)
        time.sleep(1)
        pag.click()
        i=0
        n+=1
        if n>lens:
            print("完毕")
            break
    input()
