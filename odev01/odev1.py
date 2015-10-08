__author__ = 'fturan'
import numpy as np
import matplotlib.pyplot as py
mu1=2.0
mu2=4.0
sigma1=0.6
sigma2=1.4


x1=np.random.normal(mu1,sigma1,10000)
x2=np.random.normal(mu2,sigma2,10000)
#print(x2)

for i in range(0,10000):
    x1[i]=round(x1[i])
    x1[i]+=1
print(x1)


for i in range(0,10000):
    x2[i]=round(x2[i])
    x2[i]+=1
print(x2)

histogram1=[0.0]*40
histogram2=[0.0]*40

for i in range(0,10000):
    for j in range(0,40):
        if x1[i]>-20 and x1[i]<20 and x1[i]==j:
              histogram1[j]+=1
plt.hist(range(-20,21),400,weights=histogram1,color='blue')
#print(histogram1)



for i in range(0,10000):
    for j in range(0,40):
        if x2[i]>-20 and x2[i]<20 and x2[i]==j:
              histogram2[j]+=1
#print(histogram2)
plt.hist(range(-20,21),400,weights=histogram2,color='blue')


toplam1=sum(histogram1)
for i in range(len(histogram1)):
    histogram1[i]=histogram1[i]/toplam1
print(histogram1)

toplam2=sum(histogram2)
for i in range(len(histogram2)):
    histogram2[i]=histogram2[i]/toplam2
print(histogram2)


while(histogram1[i]<41 and histogram2[i]<41):
    if histogram1[i]<histogram2[j]:

    if histogram1[i]>histogram2[j] :

    if histogram1[i]==histogram2[j]:
        histogram1[i]==0



