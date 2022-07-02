from TYPE_A_ADD import *
from TYPE_A_SUB import *
from TYPE_B_MOVE_R import *
'''from TYPE_B_MOVE_IM import *
from TYPE_B_MOVE_R import *
from TYPE_D_STORE import *
#from TypeA_MUL import *
from TYPE_C_COMPARE import *
from TYPE_B_RIGHTSHIFT import *
from TYPE_A_XOR import *
from TYPE_A_OR import *
from TYPE_A_AND import *
from TYPE_C_NOT import *
from TYPE_C_COMPARE import *
from TYPE_E_JUMPIFL import *
from TYPE_F_HLT import *

from TYPE_A_AND import *
from TYPE_A_OR import *
from TYPE_A_XOR import *
from TYPE_C_NOT import *
from TYPE_F_HLT import *
from TYPE_D_STORE import *
from TYPE_B_RIGHTSHIFT import *
from TYPE_B_MOVE_R import *
from TYPE_C_DIV import *'''
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
        A_add(j)
    elif j[0]=="sub":
        print(A_sub(j))
    elif j[0]=="mov" and j[2]=="R1" or j[2]=="R2" or j[2]=="R3":
        C_move_R(j)
    '''elif j[0]=="and":
        print(A_and(j))
    elif j[0]=="or":
        print(A_or(j))
    elif j[0]=="xor":
        print(A_xor(j))
    elif j[0]=="not":
        print(C_not(j))
    elif B_rs(j):
        print(B_rs(j))
    elif j[0]=="hlt":
        print(F_hlt(j))
    elif j[0]=="mov" and j[2]=="R1" or j[2]=="R2" or j[2]=="R3":
        print(C_move_R(j))
    elif j[0]=="div":
        print(C_div(j))'''
