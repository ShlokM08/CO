from TYPE_A_ADD import A_add
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
#from Memory_Address import mem_add
from DICT_VALUE import *
import sys
file=open("TO_READ.txt","r")
asi=[]
L=[]
for line in file:
#with open("TO")
    asi.append(line.rstrip())
'''for line in sys.stdin:
    asi.append(line.rstrip())'''
#print (asi)
asii=[]
for line in asi:
    if line!='':
        asii.append(line)
c=0
err=[]
c_err=0
for i in asii:
    c_err+=1
    if '\t' in i:
        err.append(c_err)
for i in asii:
    i=i.split()
    c+=1
    L.append(i)
#print(L)
l=[]
num_of_var=0
for j in L:
    if j!=[]:
        l.append(j)
lst=[]
var_list=[]
dict={}
var_start=len(asii)-num_of_var
for j in l:
    if len(j)==2:
        if j[0]=="var":
            var_list.append(j[1])
    
        num_of_var+=1
for variable in var_list:
    dict[variable]=format(var_start,"08b")
    var_start+=1
#print(dict)
label_value={}
if ["hlt"] not in l:
    print("Missing HLT insturction")
list_of_instructions=[]

c_var=0
for j in l:
        if j[0]=='var':
            c_var+=1
        else:
            break
c_op=0

for j in l:
    c_op+=1


    if j[0]!="mov" and "FLAGS" in j[1:]: 
        print(f'ERROR:Illegal use of FLAG Register in line {c_op}')
    
    #if j[0] in list(op_code.keys())[:20]:
        #print(j[0])
    for i in j:
        if i not in op_code.keys() and j.count(i)>1:
            print(f'Error: Syntax Error at line {c_op}!')
            break
    for ch in err:
        if ch==c_op:
            print('Error: Space Error')
            break

        '''if j.count(j[0])>1:
            print(f'Error: Syntax Error in line {c_op}')'''

    if j[0]=='var' and l.index(j)+1>c_var:
        print(f'Error: Variable at line {c_op} not defined in the beginning')

    else:
        #print(j)
        lenght_of_list=len(j[0])
        j1=[]
        for v in j:
            x=v.split(":")
            j1.append(x)
        for t in j1:
            if len(t)>1:
                if t[1]=="":
                    label_num=int(l.index(j)+1)-num_of_var
                    label_value[t[0]]=format(label_num,"08b")
                    
        if j[0][0:lenght_of_list-1]  in label_value:
            #print("check",j[0][0:lenght_of_list-1])
            j.pop(0)
        if j!=[]:
            if j[0] in type_A:
                    try:
                        if j[0]=="add":
                            found=0
                            print(A_add(j))
                            x=A_add(j)
                            lst.append(x)
                        elif j[0]=="sub":
                            print(A_sub(j))
                            x=A_sub(j)
                            lst.append(x)
                        elif j[0]=="mul":
                            print(A_mul(j))
                            x=A_mul(j)
                            lst.append(x)
                        elif j[0]=="xor":
                            print(A_xor(j))
                            x=A_xor(j)
                            lst.append(x)
                        elif j[0]=="and":
                            print(A_and(j))
                            x=A_and(j)
                            lst.append(x)
                        elif j[0]=="or":
                            print(A_or(j))
                            x=A_or(j)
                            lst.append(x)
                    except:
                        print(f'ERROR:Undefined Register in line {c_op}')
            elif j[0] in type_B and '$' in j[2]:
                if j[1] not in reg:
                    print(f'ERROR:Incorrect value of register in line {c_op}')
                elif j[1]=="FLAGS":
                    print(f'ERROR:Illegal use of FLAG Register in line {c_op}')
                elif j[0]=="mov" :
                    #print(keypresent(j))
                    if '$' in j[2]:
                        num=''
                        for ch in j[2]:
                            if ch!='$':
                                num+=ch
                        try:
                            num=int(num)
                            if num<256:
                                print(B_mov_i(j))
                                x=B_mov_i(j)
                                lst.append(x)
                            else: print('Error: Illegal Immediate Value')
                        except: print('Error: Illegal Immediate Value')
                elif j[0]=="rs":
                        num=''
                        for ch in j[2]:
                            if ch!='$':
                                num+=ch
                        try:
                            num=int(num)
                            if num<256:
                                print(B_rs(j))
                                x=B_rs(j)
                                lst.append(x)
                            else: print('Error: Illegal immediate Value')
                        except:
                            print('Error: Illegal Immediate Value')
                elif j[0]=="ls":
                    num=''
                    for ch in j[2]:
                        if ch!='$':
                            num+=ch
                    try:
                        num=int(num)
                        if num<256:
                            print(B_leftshift(j))
                            x=B_leftshift(j)
                            lst.append(x)
                        else: print('Error: Illegal Immediate Value')
                    except:
                        print('Error: Illegal Immediate Value')
            elif j[0] in type_C:
                if j[0]=="mov":
                    if j[2] in reg and j[2]!="FLAGS" and j[1] in reg:
                        print(C_move_R(j))
                        x=C_move_R(j)
                        lst.append(x)
                    elif j[2]=="FLAGS":
                        print(f'Error: Illegal usage FLAG in line {c_op}')
                elif j[0]=="div":
                    print(C_div(j))
                    x=C_div(j)
                    lst.append(x)
                elif j[0]=="not":
                    print(C_not(j))
                    x=C_not(j)
                    lst.append(x)
                elif j[0]=="cmp":
                    print(C_compare(j))
                    x=C_compare(j)
                    lst.append(x)
            elif j[0]in type_D:
                    if j[0]=="ld":
                        found=0
                        for ch in l:
                            if ch[0]=='var':
                                if ch[1]==j[2]:
                                    found=1
                                    break
                        l_err=1
                        for ch in l:
                            if ':' in ch[0]:
                                if j[1] in ch[0]:
                                    l_err=0
                                    break

                        
                        if found==1 and l_err==1:
                            print(D_load(j,dict))
                            x=D_load(j,dict)
                            lst.append(x)
                        else:
                            if found==0:
                                print(f'Error: Variable {j[2]} not defined')
                            elif l_err==0:
                                print('Error: Misuse of label as variable')
                    elif j[0]=="st":
                            found=0
                            for ch in l:
                                if ch[0]=='var':
                                    if ch[1]==j[2]:
                                        found=1
                                        break
                            l_err=1
                            for ch in l:
                                if ':' in ch[0]:
                                    if j[1] in ch[0]:
                                        l_err=0
                                        break
                            if found==1 and l_err==1:
                                print(D_store(j, dict))
                                x=D_store(j,dict)
                                lst.append(x)
                            else: 
                                if found==0:
                                    print(f"Error: Variable {j[2]} not defined")
                                elif l_err==0:
                                    print('Error: Misuse of label as variable')
                                
            elif j[0] in type_E:
                if j[0]=="jmp":
                    found=0
                    lbl=0
                    for ch in l:
                        if ch[0]=='var':
                            if ch[1]==j[1]:
                                found=1
                                break
                    for ch in l:
                        if ':' in ch[0]:
                            if j[1] in ch[0]:
                                lbl=1
                                break
                    
                    if lbl==1:
                        print(E_u_jump(j,label_value))
                        x=E_u_jump(j,label_value)
                        lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                elif j[0]=="jlt":
                    found=0
                    lbl=0
                    for ch in l:
                        if ch[0]=='var':
                            if ch[1]==j[1]:
                                found=1
                                break
                    for ch in l:
                        if ':' in ch[0]:
                            if j[1] in ch[0]:
                                lbl=1
                                break

                    if lbl==1:
                        print(E_u_jump(j,label_value))
                        x=E_u_jump(j,label_value)
                        lst.append(x)
                    else:
                        if found==1: 
                            print(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                elif j[0]=="jgt":
                    found=0
                    lbl=0
                    for ch in l:
                        if ch[0]=='var':
                            if ch[1]==j[1]:
                                found=1
                                break
                    for ch in l:
                        if ':' in ch[0]:
                            if j[1] in ch[0]:
                                lbl=1
                                break
                    if lbl==1:
                        print(E_u_jump(j,label_value))
                        x=E_u_jump(j,label_value)
                        lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variabel as label')
                        elif lbl==0:
                            print('Error: Label not found')
                elif j[0]=="je":
                    found=0
                    lbl=0
                    for ch in L:
                        if ch[0]=='var':
                            if ch[1]==j[1]:
                                found=1
                                break
                    for ch in l:
                        if ':' in ch[0]:
                            if j[1] in ch[0]:
                                lbl=1
                                break
                    if lbl==1:
                        print(E_u_jump(j,label_value))
                        x=E_u_jump(j,label_value)
                        lst.append(x)
                    else:
                        if found==1:
                            print(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
            elif j[0] in type_F:
                if j[0]=="hlt" and "hlt" in l[len(l)-1]:
                    print(F_hlt(j))
                    x=F_hlt(j)
                    lst.append(x)
                else:
                    print(f'HLT being used in line {c_op} instead of as final instruction')
            elif j[0][0]=="var":
                continue
            elif j[0] in label_value:
                print(label_value[j[0]])
                #print(label_value)
                #print("YES")
                
            elif j[0] in label_value:
                continue
            elif j[0] not in type_A+type_B+type_C+type_D+type_E+type_F and j[0] not in label_value and j[0]!="var" and j[0][0:lenght_of_list-1] not in label_value:
                print(f"Error Invalid Instruction: {j[0]} in line {c_op}")
        else:
            print(f'General Syntax Error at line {c_op}')

#print("KEYS",label_value.keys())
#print("fire",list_label_value)
for line in lst:
        #print(line)
        line=line+'\n'
        print(line) 