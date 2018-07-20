import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.stats import entropy

n = 500
x = np.zeros((1,n))
y = np.zeros((1,n))
k=0
random.seed(1000)
while k<n:
    x_tmp = random.uniform(0,10)
    y_tmp = random.uniform(0,30)
    if ((x_tmp - 7)**2) + ((y_tmp - 10)**2) / 24 <= 1:
        x[0][k] = x_tmp
        y[0][k] = y_tmp
        k += 1
a1=np.vstack((x,y))

k=0
random.seed(500)
while k<n:
    x_tmp = random.uniform(0,10)
    y_tmp = random.uniform(0,30)
    if ((x_tmp - 9)**2) + ((y_tmp - 10)**2) / 24 <= 1:
        x[0][k] = x_tmp
        y[0][k] = y_tmp
        k += 1
a2=np.vstack((x,y))

a = np.hstack((a1,a2))

Acentered = (a[0] - a[0].mean(), a[1] - a[1].mean())
m = (x.mean(), y.mean())
covmat = np.cov(Acentered)
l, vecs = np.linalg.eig(covmat)

v1 = vecs[:,0]
Anew_w1 = np.dot(v1,Acentered)
v2 = vecs[:,1]
Anew_w2 = np.dot(v2,Acentered)

sko1 = np.std(Anew_w1)
sko2 = np.std(Anew_w2)
print("sko1 = ", sko1)
print("sko2 = ", sko2)

hist1 = np.histogram(Anew_w1, 20)
h1 = hist1[0] / len(Anew_w1)
print("enrt1 = ", entropy(h1))
hist2 = np.histogram(Anew_w2, 20)
h2 = hist2[0] / len(Anew_w2)
print("enrt2 = ", entropy(h2))

#print(vecs)
w1_bx=[0, vecs[0][0]]
w1_by=[0, vecs[1][0]]
w2_bx=[0, vecs[0][1]]
w2_by=[0, -vecs[1][1]]
#print(Acentered[0][1])
plt.subplot(1,1,1)

#for i in range(len(Acentered[0])):
#    plt.plot(Acentered[0][i], Acentered[1][i], "o", ms = 3, color='r')
#plt.plot(w1_bx, w1_by, linewidth=4.0, color='g', label='w1')
#plt.plot(w2_bx, w2_by, linewidth=4.0, color='m', label='w2')
#plt.axis([-5, 5, -6, 6])
#plt.title ("Отцентрованная выборка")
#plt.ylabel('Y')
#plt.xlabel('X')

#for i in range(len(a1[0])):
#    plt.plot(a1[0][i], a1[1][i], "o", color='r', ms = 3)
#for i in range(len(a2[0])):
#    plt.plot(a2[0][i], a2[1][i], "o", color='b', ms = 3)
#plt.axis([4, 12, 4, 16])
#plt.title ("Исходная выборка")
#plt.ylabel('Y')
#plt.xlabel('X')

plt.hist(Anew_w2, 20, edgecolor='w', linewidth=3)
plt.title ("Гистограмма проекции на w2")
#
#plt.hist(Anew_w1, 20, edgecolor='w', linewidth=3)
#plt.title ("Гистограмма проекции на w1")

plt.grid(True)
plt.legend()
plt.show()

