import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import numpy as np
import random
import math
import pylab
import time
n = 400
a=np.empty([n,2])
x1=x2=test=x11=x22=x1Stand=x2Stand=x1Test=x2Test=x1Neib=x2Neib=mis1=mis2=tm1=tm2=np.empty([0,2])
#Заполняем общую выборку
for i in range(n):
    for j in range(2):
        if j % 2 == 0:
            a[i][j] = random.randint(0,100)
        else:
            a[i][j] = random.randint(40,150)
k=math.ceil(n*7/10)

#Простая форма
'''for i in range(k):
    for j in range(2):
         if j % 2 == 0:
                if a[i][j] < 50:
                    x1=np.append(x1, [a[i]], axis=0)
                if a[i][j] > 50:
                    x2=np.append(x2, [a[i]], axis=0)'''
#Сложная форма
for i in range(k):
    for j in range(2):
         if j % 2 == 0:
                if a[i][j] < 70:
                    if a[i][j+1] > 100:
                        x1=np.append(x1, [a[i]], axis=0)
                if a[i][j] < 30:
                    x1=np.append(x1, [a[i]], axis=0)        
                if a[i][j] >40:
                    if a[i][j+1] < 80:
                        x2=np.append(x2, [a[i]], axis=0)
                if a[i][j] >80:
                    x2=np.append(x2, [a[i]], axis=0)
#Смешанная форма
'''h=0
for i in range(k):
    for j in range(2):
         if j % 2 == 0:
                if a[i][j] < 65:
                    if a[i][j] > 40:
                        if h%2==0:
                            x1=np.append(x1, [a[i]], axis=0)
                            if h==2:
                                h=0
                            else:
                                h=h+1
                    else:
                        x1=np.append(x1, [a[i]], axis=0)
                if a[i][j] >40:
                    if a[i][j] < 65:
                        if h%2==1:
                            x2=np.append(x2, [a[i]], axis=0)
                            h=h+1
                    else:
                        x2=np.append(x2, [a[i]], axis=0)'''  
#Заполняем тестовую выборку
for i in range(n-k):
    test=np.append(test, [a[k]], axis=0)
    k=k+1
allObj1=allObj2=allMis1=allMis2=0
print(len(test))
nX=2
#Измерение времени
'''for f in range(min(len(x1),len(x2))-1):
    time1=time2=0
    for h in range(30):
        for i in range(nX):
            x11=np.append(x11, [x1[i]], axis=0)
        for i in range(nX):
            x22=np.append(x22, [x2[i]], axis=0)
        t1=time.time()
        #Считаем 1 эталон
        s=0
        for i in range(len(x11)):
            s=s+x11[i][0]
        x=s/nX
        s=0
        for i in range(len(x11)):
            s=s+x11[i][1]
        y=s/nX
        x1Stand=np.append(x1Stand, [[x,y]], axis=0)
        #Считаем 2 эталон
        s=0
        for i in range(len(x22)):
            s=s+x22[i][0]
        x=s/nX
        s=0
        for i in range(len(x22)):
            s=s+x22[i][1]
        y=s/nX
        x2Stand=np.append(x2Stand, [[x,y]], axis=0)
        #Считаем 1 радиус
        s=0
        for i in range(len(x11)):
            s=s+math.pow(math.sqrt(math.pow((x1Stand[0][0]-x11[i][0]),2)+math.pow((x1Stand[0][1]-x11[i][1]),2)),2)
        r1=math.sqrt(s/nX)
        #Считаем 2 радиус
        s=0
        for i in range(len(x22)):
            s=s+math.pow(math.sqrt(math.pow((x2Stand[0][0] - x22[i][0]),2)+math.pow((x2Stand[0][1]-x22[i][1]),2)),2)
        r2=math.sqrt(s/nX)
        for i in range(len(test)):
            k = math.sqrt(math.pow((test[i][0]-x1Stand[0][0]),2) + math.pow((test[i][1] - x1Stand[0][1]),2))/r1-math.sqrt(math.pow((test[i][0]-x2Stand[0][0]),2) + math.pow((test[i][1] - x2Stand[0][1]),2))/r2
            if k < 0 :
                x1Test=np.append(x1Test, [test[i]], axis=0)
            if k > 0 :                                             x2Test=np.append(x2Test, [test[i]], axis=0)
        time1=time1+(time.time()-t1) 
        t1=time.time()
        for i in range(len(test)):
            l=100000
            for j in range(len(x11)):
                if l > math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2)):
                    cl=1
                    l=math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2))
            for j in range(len(x22)):
                if l > math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2)):
                    cl=2
                    l=math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2))
            if cl==1:
                x1Neib=np.append(x1Neib, [test[i]], axis=0)
            else:
                x2Neib=np.append(x2Neib, [test[i]], axis=0)
        time2=time2+(time.time()-t1)
        mis=0
        #print(len(test))
        #print(len(x2Test))
        for i in range(len(x1Test)):
            if x1Test[i][0]>50:
                mis=mis+1
        for i in range(len(x2Test)):
            if x2Test[i][0]<50:
                mis=mis+1
        mis1=np.append(mis1, [[nX,mis]], axis=0)
        allMis1=allMis1+mis
        mis=0
        for i in range(len(x1Neib)):
            if x1Neib[i][0]>50:
                mis=mis+1
        for i in range(len(x2Neib)):
            if x2Neib[i][0]<50:
                mis=mis+1
        mis2=np.append(mis2, [[nX,mis]], axis=0)
        allMis2=allMis2+mis
        
        allObj1=allObj1+len(x1Test)+len(x2Test)
        allObj2=allObj2+len(x1Neib)+len(x2Neib)
        for i in range(len(x11)):
            x11=np.delete(x11, 0, 0)
        for i in range(len(x22)):
            x22=np.delete(x22, 0, 0)
        for i in range(len(x1Test)):
            x1Test=np.delete(x1Test, 0, 0)
        for i in range(len(x2Test)):
            x2Test=np.delete(x2Test, 0, 0)
        for i in range(len(x1Neib)):
            x1Neib=np.delete(x1Neib, 0, 0)
        for i in range(len(x2Neib)):
            x2Neib=np.delete(x2Neib, 0, 0)
    nX=nX+1
    time1=time1/30
    time2=time2/30
    tm1=np.append(tm1, [[nX,time1]], axis=0)
    tm2=np.append(tm2, [[nX,time2]], axis=0)
#print(mis1)
print((allObj1-allMis1)*100/allObj1)
print((allObj2-allMis2)*100/allObj2)
plt.subplot(1,1,1)
for i in range(len(tm1)):
    plt.plot(tm1[i][0], tm1[i][1], "o", color='g')
for i in range(len(tm2)):
    plt.plot(tm2[i][0], tm2[i][1], "o", color='b')
#plt.ylim(0, min(len(x1), len(x2)))
plt.grid(True)
plt.ylabel('время выполнения методов')
plt.xlabel('количество элементов в обучающей выборке')
plt.title ("Зависимость времени работы методов от размера обучающей выборки")'''

#Зависимость количества ошибок от размера обучающей выборки
for f in range(min(len(x1),len(x2))-1):
    for i in range(nX):
        x11=np.append(x11, [x1[i]], axis=0)
    for i in range(nX):
        x22=np.append(x22, [x2[i]], axis=0)
    #Считаем 1 эталон
    s=0
    for i in range(len(x11)):
        s=s+x11[i][0]
    x=s/nX
    s=0
    for i in range(len(x11)):
        s=s+x11[i][1]
    y=s/nX
    x1Stand=np.append(x1Stand, [[x,y]], axis=0)
    #Считаем 2 эталон
    s=0
    for i in range(len(x22)):
        s=s+x22[i][0]
    x=s/nX
    s=0
    for i in range(len(x22)):
        s=s+x22[i][1]
    y=s/nX
    x2Stand=np.append(x2Stand, [[x,y]], axis=0)
    #Считаем 1 радиус
    s=0
    for i in range(len(x11)):
        s=s+math.pow(math.sqrt(math.pow((x1Stand[0][0]-x11[i][0]),2)+math.pow((x1Stand[0][1]-x11[i][1]),2)),2)
    r1=math.sqrt(s/nX)
    #Считаем 2 радиус
    s=0
    for i in range(len(x22)):
        s=s+math.pow(math.sqrt(math.pow((x2Stand[0][0] - x22[i][0]),2)+math.pow((x2Stand[0][1]-x22[i][1]),2)),2)
    r2=math.sqrt(s/nX)
    for i in range(len(test)):
        k = math.sqrt(math.pow((test[i][0]-x1Stand[0][0]),2) + math.pow((test[i][1] - x1Stand[0][1]),2))/r1-math.sqrt(math.pow((test[i][0]-x2Stand[0][0]),2) + math.pow((test[i][1] - x2Stand[0][1]),2))/r2
        if k < 0 :
            x1Test=np.append(x1Test, [test[i]], axis=0)
        if k > 0 :                                             x2Test=np.append(x2Test, [test[i]], axis=0)

    for i in range(len(test)):
        l=100000
        for j in range(len(x11)):
            if l > math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2)):
                cl=1
                l=math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2))
        for j in range(len(x22)):
            if l > math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2)):
                cl=2
                l=math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2))
        if cl==1:
            x1Neib=np.append(x1Neib, [test[i]], axis=0)
        else:
            x2Neib=np.append(x2Neib, [test[i]], axis=0)
    mis=0
    #print(len(test))
    #print(len(x2Test))
    for i in range(len(x1Test)):
        if x1Test[i][0]>50:
            mis=mis+1
    for i in range(len(x2Test)):
        if x2Test[i][0]<50:
            mis=mis+1
    mis1=np.append(mis1, [[nX,mis]], axis=0)
    allMis1=allMis1+mis
    mis=0
    for i in range(len(x1Neib)):
        if x1Neib[i][0]>50:
            mis=mis+1
    for i in range(len(x2Neib)):
        if x2Neib[i][0]<50:
            mis=mis+1
    mis2=np.append(mis2, [[nX,mis]], axis=0)
    allMis2=allMis2+mis
    nX=nX+1
    allObj1=allObj1+len(x1Test)+len(x2Test)
    allObj2=allObj2+len(x1Neib)+len(x2Neib)
    for i in range(len(x11)):
        x11=np.delete(x11, 0, 0)
    for i in range(len(x22)):
        x22=np.delete(x22, 0, 0)
    for i in range(len(x1Test)):
        x1Test=np.delete(x1Test, 0, 0)
    for i in range(len(x2Test)):
        x2Test=np.delete(x2Test, 0, 0)
    for i in range(len(x1Neib)):
        x1Neib=np.delete(x1Neib, 0, 0)
    for i in range(len(x2Neib)):
        x2Neib=np.delete(x2Neib, 0, 0)
    
#print(mis1)
print((allObj1-allMis1)*100/allObj1)
print((allObj2-allMis2)*100/allObj2)
plt.subplot(1,1,1)
for i in range(len(mis1)):
    plt.plot(mis1[i][0], mis1[i][1], "o", color='g')
for i in range(len(mis2)):
    plt.plot(mis2[i][0], mis2[i][1], "o", color='b')
#plt.ylim(0, min(len(x1), len(x2)))
plt.grid(True)
plt.ylabel('количество ошибок')
plt.xlabel('количество элементов в обучающей выборке')
plt.title ("Зависимость количества ошибок от размера обучающей выборки")

#Зависимость количества ошибок от количества выбросов
'''nX=120
for f in range(100):
    for i in range(nX):
        x11=np.append(x11, [x1[i]], axis=0)
    for i in range(nX):
        x22=np.append(x22, [x2[i]], axis=0)
    for i in range(f):
        tmp=x11[i]
        x11[i]=x22[i]
        x22[i]=tmp
    #Считаем 1 эталон
    s=0
    for i in range(len(x11)):
        s=s+x11[i][0]
    x=s/nX
    s=0
    for i in range(len(x11)):
        s=s+x11[i][1]
    y=s/nX
    x1Stand=np.append(x1Stand, [[x,y]], axis=0)
    #Считаем 2 эталон
    s=0
    for i in range(len(x22)):
        s=s+x22[i][0]
    x=s/nX
    s=0
    for i in range(len(x22)):
        s=s+x22[i][1]
    y=s/nX
    x2Stand=np.append(x2Stand, [[x,y]], axis=0)
    #Считаем 1 радиус
    s=0
    for i in range(len(x11)):
        s=s+math.pow(math.sqrt(math.pow((x1Stand[0][0]-x11[i][0]),2)+math.pow((x1Stand[0][1]-x11[i][1]),2)),2)
    r1=math.sqrt(s/nX)
    #Считаем 2 радиус
    s=0
    for i in range(len(x22)):
        s=s+math.pow(math.sqrt(math.pow((x2Stand[0][0] - x22[i][0]),2)+math.pow((x2Stand[0][1]-x22[i][1]),2)),2)
    r2=math.sqrt(s/nX)
    for i in range(len(test)):
        k = math.sqrt(math.pow((test[i][0]-x1Stand[0][0]),2) + math.pow((test[i][1] - x1Stand[0][1]),2))/r1-math.sqrt(math.pow((test[i][0]-x2Stand[0][0]),2) + math.pow((test[i][1] - x2Stand[0][1]),2))/r2
        if k < 0 :
            x1Test=np.append(x1Test, [test[i]], axis=0)
        if k > 0 :                                             x2Test=np.append(x2Test, [test[i]], axis=0)

    for i in range(len(test)):
        l=100000
        for j in range(len(x11)):
            if l > math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2)):
                cl=1
                l=math.sqrt(math.pow((x11[j][0]-test[i][0]),2)+math.pow((x11[j][1]-test[i][1]),2))
        for j in range(len(x22)):
            if l > math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2)):
                cl=2
                l=math.sqrt(math.pow((x22[j][0]-test[i][0]),2)+math.pow((x22[j][1]-test[i][1]),2))
        if cl==1:
            x1Neib=np.append(x1Neib, [test[i]], axis=0)
        else:
            x2Neib=np.append(x2Neib, [test[i]], axis=0)
    mis=0
    for i in range(len(x1Test)):
        if x1Test[i][0]>50:
            mis=mis+1
    for i in range(len(x2Test)):
        if x2Test[i][0]<50:
            mis=mis+1
    mis1=np.append(mis1, [[f,mis]], axis=0)
    allMis1=allMis1+mis
    mis=0
    for i in range(len(x1Neib)):
        if x1Neib[i][0]>50:
            mis=mis+1
    for i in range(len(x2Neib)):
        if x2Neib[i][0]<50:
            mis=mis+1
    mis2=np.append(mis2, [[f,mis]], axis=0)
    allMis2=allMis2+mis
    allObj1=allObj1+len(x1Test)+len(x2Test)
    allObj2=allObj2+len(x1Neib)+len(x2Neib)
    for i in range(len(x11)):
        x11=np.delete(x11, 0, 0)
    for i in range(len(x22)):
        x22=np.delete(x22, 0, 0)
    for i in range(len(x1Test)):
        x1Test=np.delete(x1Test, 0, 0)
    for i in range(len(x2Test)):
        x2Test=np.delete(x2Test, 0, 0)
    for i in range(len(x1Neib)):
        x1Neib=np.delete(x1Neib, 0, 0)
    for i in range(len(x2Neib)):
        x2Neib=np.delete(x2Neib, 0, 0)
    
#print(mis1)
print((allObj1-allMis1)*100/allObj1)
print((allObj2-allMis2)*100/allObj2)
plt.subplot(1,1,1)
for i in range(len(mis1)):
    plt.plot(mis1[i][0], mis1[i][1], "o", color='g')
for i in range(len(mis2)):
    plt.plot(mis2[i][0], mis2[i][1], "o", color='b')
#plt.ylim(0, min(len(x1), len(x2)))
plt.grid(True)
plt.ylabel('количество ошибок')
plt.xlabel('количество выбросов в обоих выборках')
plt.title ("Зависимость количества ошибок от количества выбросов")'''

plt.show()    
