#from TYPE_A_ADD import A_add
'''from TYPE_A_MUL import A_mul
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
#from TYPE_F_HLT import *
from TYPE_D_LOAD import D_load
from TYPE_B_LEFTSHIFT import B_leftshift
from TYPE_E_UNCONDITIONALJUMP import E_u_jump
from TYPE_E_JUMPIFG import E_jumpifg
from TYPE_E_JUMPIFE import E_jumpife
#from Memory_Address import mem_add
from DICT_VALUE import *'''
import sys
#==============================================================================
op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

unused={"A":"00","C":"00000","E":"000","F":"00000000000"}
type_A=["add","sub","mul","div","xor","or","and"]
type_B=["mov","rs","ls"]
type_C=["mov","div","not","cmp"]
type_D=["ld","st"]
type_E=["jmp","jlt","jgt","je"]
type_F=["hlt"]

reg=["R0","R1","R2","R3","R4","R5","R6","FLAGS"]

def A_add(to_read):
        binary_encoding=""
        if to_read[0]=="add":
            binary_encoding=op_code["add"]
        binary_encoding+=unused["A"]+op_code[to_read[1]]+op_code[to_read[2]]+op_code[to_read[3]]
        return binary_encoding

def A_and(to_encode):
        binary_encoding=""
        if to_encode[0]=="and":
            binary_encoding=op_code["and"]
        binary_encoding+=unused["A"]+op_code[to_encode[1]]+op_code[to_encode[2]]+op_code[to_encode[3]]
        return binary_encoding

def A_mul(user):

    val=l.op_code["mul"]
    valueR1=op_code[user[1]]
    valueR2=op_code[user[2]]
    valueR3=op_code[user[3]]
    return (val+unused["A"]+valueR1+valueR2+valueR3)

def A_or(inp):
   
        s=op_code['or']+unused["A"]+op_code[inp[1]]+op_code[inp[2]]+op_code[inp[3]]
        return s

def A_sub(inp):
   
        s=op_code['sub']+unused["A"]+op_code[inp[1]]+op_code[inp[2]]+op_code[inp[3]]
        return s
   
def A_xor(to_encode):
    binary_encoding=""
    if to_encode[0]=="xor":
        binary_encoding=op_code["xor"]
    binary_encoding+=unused["A"]+op_code[to_encode[1]]+op_code[to_encode[2]]+op_code[to_encode[3]]
    return binary_encoding

def B_leftshift(user):
    val=op_code["ls"]
    valueR1=op_code[user[1]]
    num=int(user[2][1:])
    mem_addr=''
    while num:
        r=num%2
        mem_addr+=str(r)
        num//=2
    mem_addr=mem_addr[::-1]
    if len(mem_addr)<8:
        mem_addr='0'*(8-len(mem_addr))+mem_addr

    return(val+valueR1+mem_addr)

def B_mov_i(inp):
    s=op_code['mov_I']+op_code[inp[1]]
    num=''
    for ch in inp[2]:
        if ch!='$':
            num+=ch
    num=int(num)
    num_bin=''
    while num:
        r=num%2
        num_bin+=str(r)
        num=num//2
    num_bin=num_bin[::-1]
    if len(num_bin)<8:
        num_bin='0'*(8-len(num_bin))+num_bin
    s+=num_bin
    return s

def C_move_R(to_read):
    binary_encoding=""
    if to_read[0]=="mov":
        binary_encoding=op_code["mov_R"]
    binary_encoding+=unused["C"]+op_code[to_read[1]]+op_code[to_read[2]]
    return binary_encoding

def B_rs(to_encode):
    x=to_encode[2].split("$")
    for ch in range(1,len(x)):
        #print("Value",type(x[ch]))
        bnr = bin(int(x[ch])).replace('0b','')
        #print(bnr)
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        if to_encode[0]=="rs":
                binary_encoding=op_code["rs"]
        binary_encoding+=op_code[to_encode[1]]+bnr
        return binary_encoding

def C_compare(inp):
    s=op_code['cmp']+unused['C']+op_code[inp[1]]+op_code[inp[2]]
    return s

def C_div(to_encode):
    binary_encoding=""
    if to_encode[0]=="div":
        binary_encoding=op_code["div"]
    binary_encoding+=unused["C"]+op_code[to_encode[1]]+op_code[to_encode[2]]
    return binary_encoding

def C_not(inp):
    s=""
    if inp[0]=="not":
        s=op_code["not"]
    s+=unused['C']+op_code[inp[1]]+op_code[inp[2]]
    return s 

def D_load(user,d):
    val=op_code["ld"]
    valueR1=op_code[user[1]]
    for i in d:
        if i==user[2]:
            s=d[i]
            break
    return(val+valueR1+s)

def D_store(inp,dict):
    for i in dict.keys():
        if i==inp[2]:
            mem_addr=dict[i]
            break
    s=op_code[inp[0]]+op_code[inp[1]]+mem_addr
    return s

def E_jumpife(user, d):
    val=op_code["je"]
    s=''
    for i in d.keys():
        if i==user[1]:
            s=d[i]
            break
    return (val+unused["E"]+s)

def E_jumpifg(user,d):
    val=op_code["jgt"]
    s=''
    for i in d.keys():
        if i==user[1]:
            s=d[i]
            break
    return (val+unused["E"]+s)

def E_jump_less(inp,dict):
    for i in dict.keys():
        if i==inp[1]:
            mem_addr=dict[i]
            break
    s=op_code[inp[0]]+unused['E']+mem_addr
    return s

def E_u_jump(user, d): 
    val=op_code["jmp"]
    for i in d.keys():
        if i==user[1]:
            s=d[i]
            break
    return (val+unused["E"]+s)

def F_hlt(to_encode):
    x=""
    while len(x) < 11:
        x += '0'
    binary_encoding=""
    if to_encode[0]=="hlt":
        binary_encoding=op_code["hlt"]
    binary_encoding+=x
    return binary_encoding

#===============================================
file=open("TO_READ.txt","r")
asi=[]
L=[]
'''for ch in file:
    asi.append(ch.rstrip())'''
for line in sys.stdin:
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
    if len(j)==2:
        if j[0]=="var":
            var_list.append(j[1])
    
        num_of_var+=1
for variable in var_list:
    dict[variable]=format(var_start,"08b")
    var_start+=1
#print(dict)
found_error=0
l_err=[]
label_value={}
if ["hlt"] not in l and 'hlt' not in l[len(l)-1]:
    print("Missing HLT insturction")
    found_error=1
    l_err.append("Missing HLT insturction")
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
    j1=[]
    for v in j:
        x=v.split(":")
        j1.append(x)
    for t in j1:
        if len(t)>1:
            if t[1]=="":
                label_num=int(c_op)-num_of_var
                label_value[t[0]]=format(label_num,"08b")
c_op=0
for j in l:
    c_op+=1
    if j[0]!="mov" and "FLAGS" in j[1:]: 
        print(f'ERROR:Illegal use of FLAG Register in line {c_op}')
        found_error=1
        l_err.append(f'ERROR:Illegal use of FLAG Register in line {c_op}')
    
    #if j[0] in list(op_code.keys())[:20]:
        #print(j[0])
    for i in j:
        if i not in op_code.keys() and j.count(i)>1:
            print(f'Error: Syntax Error at line {c_op}!')
            found_error=1
            l_err.append(f'Error: Syntax Error at line {c_op}!')
            break

        '''if j.count(j[0])>1:
            print(f'Error: Syntax Error in line {c_op}')'''

    if j[0]=='var' and c_op>c_var:
        print(f'Error: Variable at line {c_op} not defined in the beginning')
        found_error=1
        l_err.append(f'Error: Variable at line {c_op} not defined in the beginning')

    else:
        #print(j)
        lenght_of_list=len(j[0])          
        if j[0][0:lenght_of_list-1]  in label_value:
            #print("check",j[0][0:lenght_of_list-1])
            j.pop(0)
        if j!=[]:
            if j[0] in type_A:
                    try:
                        if j[0]=="add" and found_error==0:
                            found=0
                            #print(A_add(j))
                            x=A_add(j)
                            lst.append(x)
                        elif j[0]=="sub" and found_error==0:
                            #print(A_sub(j))
                            x=A_sub(j)
                            lst.append(x)
                        elif j[0]=="mul" and found_error==0:
                            #print(A_mul(j))
                            x=A_mul(j)
                            lst.append(x)
                        elif j[0]=="xor" and found_error==0:
                            #print(A_xor(j))
                            x=A_xor(j)
                            lst.append(x)
                        elif j[0]=="and" and found_error==0:
                            #print(A_and(j))
                            x=A_and(j)
                            lst.append(x)
                        elif j[0]=="or" and found_error==0:
                            #print(A_or(j))
                            x=A_or(j)
                            lst.append(x)
                    except:
                        print(f'ERROR:Undefined Register in line {c_op}')
                        found_error=1
                        l_err.append(f'ERROR:Undefined Register in line {c_op}')
            elif j[0] in type_B and '$' in j[2]:
                if j[1] not in reg:
                    print(f'ERROR:Incorrect value of register in line {c_op}')
                    found_error=1
                    l_err.append(f'ERROR:Incorrect value of register in line {c_op}')
                elif j[1]=="FLAGS":
                    print(f'ERROR:Illegal use of FLAG Register in line {c_op}')
                    found_error=1
                    l_err.append(f'ERROR:Illegal use of FLAG Register in line {c_op}')
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
                                if found_error==0:
                                    #print(B_mov_i(j))
                                    x=B_mov_i(j)
                                    lst.append(x)
                            else: 
                                print('Error: Illegal Immediate Value')
                                found_error=1
                                l_err.append('Error: Illegal Immediate Value')
                        except: 
                            print('Error: Illegal Immediate Value')
                            found_error=1
                            l_err.append('Error: Illegal Immediate Value')
                elif j[0]=="rs":
                        num=''
                        for ch in j[2]:
                            if ch!='$':
                                num+=ch
                        try:
                            num=int(num)
                            if num<256:
                                if found_error==0:
                                    #print(B_rs(j))
                                    x=B_rs(j)
                                    lst.append(x)
                            else: 
                                print('Error: Illegal immediate Value')
                                found_error=1
                                l_err.append('Error: Illegal Immediate Value')
                        except:
                            print('Error: Illegal Immediate Value')
                            found_error=1
                            l_err.append('Error: Illegal Immediate Value')
                elif j[0]=="ls":
                    num=''
                    for ch in j[2]:
                        if ch!='$':
                            num+=ch
                    try:
                        num=int(num)
                        if num<256:
                            if found_error==0:
                                #print(B_leftshift(j))
                                x=B_leftshift(j)
                                lst.append(x)
                        else: 
                            print('Error: Illegal Immediate Value')
                            found_error=1
                            l_err.append('Error: Illegal Immediate Value')
                    except:
                        print('Error: Illegal Immediate Value')
                        found_error=1
                        l_err.append('Error: Illegal Immediate Value')
            elif j[0] in type_C:
                if j[0]=="mov":
                    if j[2] in reg and j[2]!="FLAGS" and j[1] in reg:
                        if found_error==0:
                            #print(C_move_R(j))
                            x=C_move_R(j)
                            lst.append(x)
                    elif j[2]=="FLAGS":
                        print(f'Error: Illegal usage FLAG in line {c_op}')
                        found_error=1
                        l_err.append(f'Error: Illegal usage FLAG in line {c_op}')
                elif j[0]=="div" and found_error==0:
                    #print(C_div(j))
                    x=C_div(j)
                    lst.append(x)
                elif j[0]=="not" and found_error==0:
                    #print(C_not(j))
                    x=C_not(j)
                    lst.append(x)
                elif j[0]=="cmp" and found_error==0:
                    #print(C_compare(j))
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
                        l_error=1
                        for ch in l:
                            if ':' in ch[0]:
                                if j[1] in ch[0]:
                                    l_error=0
                                    break

                        
                        if found==1 and l_err==1:
                            if found_error==0:
                                #print(D_load(j,dict))
                                x=D_load(j,dict)
                                lst.append(x)
                        else:
                            if found==0:
                                #print(f'Error: Variable {j[2]} not defined')
                                found_error=1
                                l_err.append()
                                l_err.append(f"Error: Variable {j[2]} not defined")
                            elif l_error==0:
                                print('Error: Misuse of label as variable')
                                found_error=1
                                l_err.append('Error: Misuse of label as variable')
                    elif j[0]=="st":
                            found=0
                            for ch in l:
                                if ch[0]=='var':
                                    if ch[1]==j[2]:
                                        found=1
                                        break
                            l_error=1
                            for ch in l:
                                if ':' in ch[0]:
                                    if j[1] in ch[0]:
                                        l_error=0
                                        break
                            if found==1 and l_error==1:
                                if found_error==0:
                                    #print(D_store(j, dict))
                                    x=D_store(j,dict)
                                    lst.append(x)
                            else: 
                                if found==0:
                                    print(f"Error: Variable {j[2]} not defined")
                                    found_error=1
                                    l_err.append(f"Error: Variable {j[2]} not defined")
                                elif l_error==0:
                                    print('Error: Misuse of label as variable')
                                    found_error=1
                                    l_err.append('Error: Misuse of label as variable')
                                
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
                        if found_error==0:
                            #print(E_u_jump(j,label_value))
                            x=E_u_jump(j,label_value)
                            lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variable as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                            found_error=1
                            l_err.append('Error: Label not found')
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
                        if found_error==0:
                            #print(E_u_jump(j,label_value))
                            
                            x=E_u_jump(j,label_value)
                            lst.append(x)
                    else:
                        if found==1: 
                            print(f'Error: Misuse of variable as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                            found_error=1
                            l_err.append('Error: Label not found')
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
                        if found_error==0:
                            #print(E_u_jump(j,label_value))
                            x=E_jumpifg(j,label_value)
                            lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variabel as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                            l_err.append('Error: Label not found')
                            found_error=1
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
                        if found_error==0:
                            x=E_jumpife(j, label_value)
                            #print(E_u_jump(j,label_value))
                            #x=E_u_jump(j,label_value)
                            lst.append(x)
                    else:
                        if found==1:
                            print(f'Error: Misuse of variable as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print('Error: Label not found')
                            found_error=1
                            l_err.append('Error: Label not found')
            elif j[0] in type_F:
                if j[0]=="hlt" and "hlt" in l[len(l)-1]:
                    if found_error==0:
                        #print(F_hlt(j))
                        x=F_hlt(j)
                        lst.append(x)
                else:
                    print(f'HLT being used in line {c_op} instead of as final instruction')
                    found_error=1
                    l_err.append(f'HLT being used in line {c_op} instead of as final instruction')
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
                l_err.append(f"Error Invalid Instruction: {j[0]} in line {c_op}")
                found_error=1
        else:
            print(f'General Syntax Error ')
            found_error=1
            l_err.append(f'General Syntax Error ')

#print("KEYS",label_value.keys())
#print("fire",list_label_value)
#with open('OUTPUT.TXT', 'w') as f:
if l_err==[]:
    for line in lst:
            #print(lst)
            #line=line
            print(line)  
    else:
        for i in l_err:
            print(line)