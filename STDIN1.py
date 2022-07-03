from TYPE_A_ADD import *
from TYPE_A_MUL import A_mul
from TYPE_A_SUB import *
from TYPE_B_MOVE_IM import B_mov_i
from TYPE_B_MOVE_R import *
from TYPE_C_COMPARE import C_compare
from TYPE_C_NOT import *
from TYPE_A_AND import *
from TYPE_A_OR import *
from TYPE_A_XOR import *
from TYPE_B_RIGHTSHIFT import *
from TYPE_C_DIV import *
from TYPE_D_STORE import D_store
from TYPE_E_JUMPIFL import E_jump_less
from TYPE_F_HLT import *
from TYPE_D_LOAD import D_load
from TYPE_B_LEFTSHIFT import B_leftshift
from TYPE_E_UNCONDITIONALJUMP import E_u_jump
from TYPE_E_JUMPIFG import E_jumpifg
from TYPE_E_JUMPIFE import E_jumpife

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



'''add R1 R2 R3
sub R1 R2 R3
not R1 R2
and R1 R2 R3
or R1 R2 R3
xor R1 R2 R3
rs R1 $10
div R3 R4'''

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
#print(L)
l=[]
for j in L:
    if j!=[]:
        l.append(j)
for j in l:
    #print(j[0])
    if j[0]=="add":
        A_add(j)
    elif j[0]=="sub":
        print(A_sub(j))
    elif j[0]=="not":
        C_not(j)
    elif j[0]=="and":
        A_and(j)
    elif j[0]=="or":
        print(A_or(j))
    elif j[0]=="xor":
        A_xor(j)
    elif j[0]=="div":
        C_div(j)
    elif j[0]=="hlt":
        F_hlt(j)
    elif j[0]=="rs":
        B_rs(j)
    elif j[0]=="mov":
        if j[2]=="R1" or j[2]=="R2" or j[2]=="R3":
            C_move_R(j)
        elif '$' in j[2]:
            print(B_mov_i(j))
    elif j[0]=='st':
        print(D_store(j))
    elif j[0]=='mul':
        print(A_mul(j))
    elif j[0]=='cmp':
        print(C_compare(j))
    elif j[0]=='jlt':
        print(E_jump_less(j))
    elif j[0]=='ls':
        print(B_leftshift(j))
    elif j[0]=='ld':
        print(D_load(j))
    elif j[0]=='jmp':
        print(E_u_jump(j))
    elif j[0]=='jgt':
        print(E_jumpifg(j))
    elif j[0]=='je':
        print(E_jumpife(j))
        
