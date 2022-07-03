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
from Memory_Address import mem_add
from DICT_VALUE import *
from Errors import keypresent
file=open("TO_READ.txt","r")
asi=[]
L=[]
for line in file:
    asi.append(line.rstrip())
#print (asi)
asii=[]
for line in asi:
    if line!='':
        asii.append(line)
c=0
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
    if j[0]=="var":
        var_list.append(j[1])
    
        num_of_var+=1
for variable in var_list:
    dict[variable]=format(var_start,"08b")
    var_start+=1


    #print(var_list)

    #print(j[0])
if ["hlt"] not in l:
    print("Missing HLT insturction")
for j in l:
    if j[0]!="mov" and "FLAGS" in j[1:]: 
        print(f'ERROR:Illegal use of FLAG Register in line {l.index(j)+1}')
    
    else:
        if j[0] in type_A:
            if j[1] and j[2] and j[3] not in reg:
                print(f'ERROR:Incorrect value of register in line {l.index(j)+1}')
            else:
                if j[0]=="add":
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
        elif j[0] in type_B and '$' in j[2]:
            if j[1] not in reg:
                print(f'ERROR:Incorrect value of register in line {l.index(j)+1}')
            elif j[1]=="FLAGS":
                print(f'ERROR:Illegal use of FLAG Register in line {l.index(j)+1}')
            elif j[0]=="mov" :
                #print(keypresent(j))
                if '$' in j[2]:
                    num=''
                    for ch in j[2]:
                        if ch!='$':
                            num+=ch
                    num=int(num)
                    if num<256:
                        print(B_mov_i(j))
                        x=B_mov_i(j)
                        lst.append(x)
                    else: print('Error: Illegal Immediate Value')
            elif j[0]=="rs":
                    num=''
                    for ch in j[2]:
                        if ch!='$':
                            num+=ch
                    num=int(num)
                    if num<256:
                        print(B_rs(j))
                        x=B_rs(j)
                        lst.append(x)
                    else: print('Error: Illegal immediate Value')
            elif j[0]=="ls":
                num=''
                for ch in j[2]:
                    if ch!='$':
                        num+=ch
                num=int(num)
                if num<256:
                    print(B_leftshift(j))
                    x=B_leftshift(j)
                    lst.append(x)
                else: print('Error: Illegal Immediate Value')
        elif j[0] in type_C:
            if j[0]=="mov":
                if j[2] in reg and j[2]!="FLAGS" and j[1] in reg:
                #if j[2]=="R0"or j[2]=="R1" or j[2]=="R2" or j[2]=="R3" or j[2]=="R4" or j[2]=="R5" or j[2]=="R6" or j[1]=="R0"or j[1]=="R1" or j[1]=="R2" or j[1]=="R3" or j[1]=="R4" or j[1]=="R5" or j[1]=="R6" or j[1]=="FLAGS" and j[2]!="FLAGS":
                    print(C_move_R(j))
                    x=C_move_R(j)
                    lst.append(x)
                elif j[2]=="FLAGS":
                    print(f'Error: Illegal usage FLAG in line {l.index(j)+1}')
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
                    for ch in L:
                        if ch[0]=='var':
                            if ch[1]==j[2]:
                                found=1
                                break
                    if found:
                        print(D_load(j,dict))
                        x=D_load(j,dict)
                        lst.append(x)
                    else: 
                        print(f'Error: Variable {j[2]} not defined')
                elif j[0]=="st":
                        found=0
                        for ch in L:
                            if ch[0]=='var':
                                if ch[1]==j[2]:
                                    found=1
                                    break
                        if found:
                            print(D_store(j, dict))
                            x=D_store(j,dict)
                            lst.append(x)
                        else: print(f"Error: Variable {j[2]} not defined")
        elif j[0] in type_E:
            if j[0]=="jmp":
                found=0
                for ch in L:
                    if ch[0]=='var':
                        if ch[1]==j[1]:
                            found=1
                            break
                if found:
                    print(E_u_jump(j,dict))
                    x=E_u_jump(j,dict)
                    lst.append(x)
                else: print(f'Error: Variable {j[1]} not defined')
            elif j[0]=="jlt":
                found=0
                for ch in L:
                    if ch[0]=='var':
                        if ch[1]==j[1]:
                            found=1
                            break
                if found:
                    print(E_jump_less(j,dict))
                    x=E_jump_less(j,dict)
                    lst.append(x)
                else: print(f'Error: Variable {j[1]} is not defined')
            elif j[0]=="jgt":
                found=0
                for ch in L:
                    if ch[0]=='var':
                        if ch[1]==j[1]:
                            found=1
                            break
                if found:
                    print(E_jumpifg(j,dict))
                    x=E_jumpifg(j,dict)
                    lst.append(x)
                else: print(f'Error: Variable {j[1]} not defined')
            elif j[0]=="je":
                found=0
                for ch in L:
                    if ch[0]=='var':
                        if ch[1]==j[1]:
                            found=1
                            break
                if found:
                    print(E_jumpife(j,dict))
                    x=E_jumpife(j,dict)
                    lst.append(x)
                else:
                    print(f'Error; Variable {j[1]} not defined')
        elif j[0] in type_F:
            if j[0]=="hlt" and "hlt" in l[len(l)-1]:
                print(F_hlt(j))
                x=F_hlt(j)
                lst.append(x)
            else:
                print(f'HLT being used in line {l.index(j)+1} instead of as final instruction')
        else:
            print(f"Error Invalid Instruction:{j[0]}")


'''
    if j[0]=="add":
        print(A_add(j))
        x=A_add(j)
        lst.append(x)
    elif j[0]=="sub":
        print(A_sub(j))
        x=A_sub(j)
        lst.append(x)
    elif j[0]=="not":
        print(C_not(j))
        x=C_not(j)
        lst.append(x)
    elif j[0]=="and":
        print(A_and(j))
        x=A_and(j)
        lst.append(x)
    elif j[0]=="or":
        print(A_or(j))
        x=A_or(j)
        lst.append(x)
    elif j[0]=="xor":
        print(A_xor(j))
        x=A_xor(j)
        lst.append(x)
    elif j[0]=="div":
        print(C_div(j))
        x=C_div(j)
        lst.append(x)
    elif j[0]=="hlt":
        print(F_hlt(j))
        x=F_hlt(j)
        lst.append(x)
    elif j[0]=="rs":
        num=''
        for ch in j[2]:
            if ch!='$':
                num+=ch
        num=int(num)
        if num<256:
            print(B_rs(j))
            x=B_rs(j)
            lst.append(x)
        else: print('Error: Illegal immediate Value')
    elif j[0]=="mov":
        if j[2]=="R0"or j[2]=="R1" or j[2]=="R2" or j[2]=="R3" or j[2]=="R4" or j[2]=="R5" or j[2]=="R6" or j[2]=="FLAGS":
            print(C_move_R(j))
            x=C_move_R(j)
            lst.append(x)
        elif '$' in j[2]:
            num=''
            for ch in j[2]:
                if ch!='$':
                    num+=ch
            num=int(num)
            if num<256:
                print(B_mov_i(j))
                x=B_mov_i(j)
                lst.append(x)
            else: print('Error: Illegal Immediate Value')
        
    elif j[0]=='st':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[2]:
                    found=1
                    break
        if found:
            print(D_store(j, dict))
            x=D_store(j,dict)
            lst.append(x)
        else: print(f"Error: Variable {j[2]} not defined")
    elif j[0]=='mul':
        print(A_mul(j))
        x=A_mul(j)
        lst.append(x)
    elif j[0]=='cmp':
        print(C_compare(j))
        x=C_compare(j)
        lst.append(x)
    elif j[0]=='jlt':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[1]:
                    found=1
                    break
        if found:
            print(E_jump_less(j,dict))
            x=E_jump_less(j,dict)
            lst.append(x)
        else: print(f'Error: Variable {j[1]} is not defined')
    elif j[0]=='ls':
        num=''
        for ch in j[2]:
            if ch!='$':
                num+=ch
        num=int(num)
        if num<256:
            print(B_leftshift(j))
            x=B_leftshift(j)
            lst.append(x)
        else: print('Error: Illegal Immediate Value')
    elif j[0]=='ld':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[2]:
                    found=1
                    break
        if found:
            print(D_load(j,dict))
            x=D_load(j,dict)
            lst.append(x)
        else: print(f'Error: Variable {j[2]} not defined')
    elif j[0]=='jmp':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[1]:
                    found=1
                    break
        if found:
            print(E_u_jump(j,dict))
            x=E_u_jump(j,dict)
            lst.append(x)
        else: print(f'Error: Variable {j[1]} not defined')
    elif j[0]=='jgt':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[1]:
                    found=1
                    break
        if found:
            print(E_jumpifg(j,dict))
            x=E_jumpifg(j,dict)
            lst.append(x)
        else: print(f'Error: Variable {j[1]} not defined')
    elif j[0]=='je':
        found=0
        for ch in L:
            if ch[0]=='var':
                if ch[1]==j[1]:
                    found=1
                    break
        if found:
            print(E_jumpife(j,dict))
            x=E_jumpife(j,dict)
            lst.append(x)
        else:
            print(f'Error; Variable {j[1]} not defined')
    #if j[0]=="var":
        #print(i)
        
        #print(j[1])
print("VAR",num_of_var)
print("VAR LIST",var_list)
print("Lenght of asii",len(asii))
    
    #print(f'Memory address of {j[1]}',mem_add(int(len(asii)),num_of_var,var_list))
'''
with open('OUTPUT.TXT', 'w') as f:
    for line in lst:
        line=line+'\n'
        f.write(line)  
#print(var_list)
#var_list.reverse()
#print(var_list)