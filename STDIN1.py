from TYPE_A_ADD import *
from TYPE_A_SUB import *
file=open("TO_READ.txt","r")
asi=[]
L=[]
for line in file:
    asi.append(line.rstrip())
#print (asi)
c=0
for i in asi:
    i=i.split()
    c+=1
    L.append(i)

for j in L:
    if j[0]=="add":
        add(j)
    elif j[0]=="sub":
        sub(j)