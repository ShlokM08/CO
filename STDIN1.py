from TYPE_A_ADD import *
from TYPE_A_SUB import *
from TYPE_A_AND import *
from TYPE_A_OR import *
from TYPE_A_XOR import *
from TYPE_C_NOT import *
from TYPE_F_HLT import *
from TYPE_D_STORE import *
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