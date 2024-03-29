import sys

#==============================================================================
#DICTIONARIES AND LISTS
op_code={"add":"10000","addf": "00000","sub":"10001","subf": "00001","mov_I":"10010","movf": "00010","mov_R":"10011","ld":"10100"
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

reg_val={"R0":"0","R1":"6","R2":"2","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0"}
#=========================================================================================================================
#FUNCTIONS FOR ASSEMBLY CODE
def A_addf(inst):
    s=op_code['fadd']+unused['A']+op_code[inst[1]]+op_code[inst[2]]+op_code[inst[3]]
    return s

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

    val=op_code["mul"]
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
def A_subf(inp):
    s=op_code['subf']+unused["A"]+op_code[inp[1]]+op_code[inp[2]]+op_code[inp[3]]
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

def B_movf_i(inp):
    s=op_code['movf']+op_code[inp[1]]
    num=''
    for ch in inp[2]:
        if ch!='$':
            num+=ch
    num=float(num)
    q=int(num)
    fr=num-q
    num_bin=''
    while q:
        r=q%2
        num_bin+=str(r)
        q=q//2
    num_bin=num_bin[::-1]+'.'
    while int(fr)!=1:
        num_bin+=str(int(fr*2))
        fr=fr*2
    s+=num_bin
    i=s.index('.')
    if len(s[1:i])<=3:
        expo=format(int(len(s[1:i])), '03b')
        mantissa=s[i+1:]
        if len(mantissa)>3:
            mantissa=mantissa[-1:-4]
        elif len(mantissa)<3:
            mantissa='0'*(3-len(mantissa))+mantissa
        s=''
        s=expo+mantissa
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

#====================================================================================================================================
#FUNCTIONS FOR SIMULATOR

def simulator_add(y):
    if y[0:5] =="10000": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-7:-10:-1][::-1]:
        
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                if op_code[i]==y[-4:-7:-1][::-1]:
                
                    temp_sum_2=int(reg_val[i])
                
                def sim_sum(temp_sum_1,temp_sum_2):
                    return temp_sum_1+temp_sum_2
    new_dict_val=sim_sum(temp_sum_1,temp_sum_2)
    if y[0:5] =="10000": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")
    #print(reg_val)


#====================================================================================================================================
asi=[]
L=[]

for line in sys.stdin:
    asi.append(line.rstrip())

asii=[]
for line in asi:
    if line!='':
        asii.append(line)
c=0
for i in asii:
    i=i.split()
    c+=1
    L.append(i)

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
    dict[variable]=format(var_start-1,"08b")
    var_start+=1

found_error=0
l_err=[]
label_value={}
if ["hlt"] not in l and 'hlt' not in l[len(l)-1]:
    print(f"Missing HLT insturction in final line")
    found_error=1
    l_err.append(f"Missing HLT insturction in final line")
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
                label_num=int(c_op)-num_of_var+1
                label_value[t[0]]=format(label_num,"08b")
c_op=0
hlt_count=0
for j in l:
    if hlt_count>0:
        print(f"hlt instruction used more than once;used at line {c_op}")
        l_err.append(f"hlt instruction used more than once;used at line {c_op}")
    c_op+=1
    if j[0]!="mov" and "FLAGS" in j[1:]: 
        print(f'ERROR:Illegal use of FLAG Register in line {c_op}')
        found_error=1
        l_err.append(f'ERROR:Illegal use of FLAG Register in line {c_op}')
    
    
    for i in j:
        if i not in op_code.keys() and j.count(i)>1:
            print(f'Error: Syntax Error at line {c_op}!')
            found_error=1
            l_err.append(f'Error: Syntax Error at line {c_op}!')
            break

        

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
                        elif j[0]=='addf' and found_error==0:
                            x=A_addf(j)
                            lst.append(x)
                        elif j[0]=="sub" and found_error==0:
                            #print(A_sub(j))
                            x=A_sub(j)
                            lst.append(x)
                        elif j[0]=='subf' and found_error==0:
                            x=A_subf(j)
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
                                print(f'Error: Illegal Immediate Value in line {c_op}')
                                found_error=1
                                l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
                        except: 
                            print(f'Error: Illegal Immediate Value in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Illegal Immediate Value  in line {c_op}')
                elif j[0]=="movf" :
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
                                    x=B_movf_i(j)
                                    lst.append(x)
                            else: 
                                print(f'Error: Illegal Immediate Value in line {c_op}')
                                found_error=1
                                l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
                        except: 
                            print(f'Error: Illegal Immediate Value in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Illegal Immediate Value  in line {c_op}')
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
                                print(f'Error: Illegal Immediate Value in line {c_op}')
                                found_error=1
                                l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
                        except:
                            print(f'Error: Illegal Immediate Value in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
                elif j[0]=="ls":
                    num=''
                    for ch in j[2]:
                        if ch!='$':
                            num+=ch
                    try:
                        num=int(num)
                        if num<256:
                            if found_error==0:
                                
                                x=B_leftshift(j)
                                lst.append(x)
                        else: 
                            print(f'Error: Illegal Immediate Value in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
                    except:
                        print(f'Error: Illegal Immediate Value in line {c_op}')
                        found_error=1
                        l_err.append(f'Error: Illegal Immediate Value in line {c_op}')
            elif j[0] in type_C:
                if j[0]=="mov":
                    if j[2] in reg and j[2]!="FLAGS" and j[1] in reg:
                        if found_error==0:
                            
                            x=C_move_R(j)
                            lst.append(x)
                    elif j[2]=="FLAGS":
                        print(f'Error: Illegal usage FLAG in line {c_op}')
                        found_error=1
                        l_err.append(f'Error: Illegal usage FLAG in line {c_op}')
                elif j[0]=="div" and found_error==0:
                    x=C_div(j)
                    lst.append(x)
                elif j[0]=="not" and found_error==0:
                    x=C_not(j)
                    lst.append(x)
                elif j[0]=="cmp" and found_error==0:
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
                                if found==1 and l_error==1:
                                    if found_error==0:
                                        x=D_load(j,dict)
                                        lst.append(x)
                                else: 
                                    if found==0:
                                        print(f"Error: Variable {j[2]} not defined in line {c_op} in line {c_op} in line {c_op}")
                                        found_error=1
                                        l_err.append(f"Error: Variable {j[2]} not defined in line {c_op} in line {c_op} in line {c_op}")
                                    elif l_error==0:
                                        print(f'Error: Misuse of label as variable in line {c_op}')
                                        found_error=1
                                        l_err.append(f'Error: Misuse of label as variable in line {c_op}')
                    
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
                                    x=D_store(j,dict)
                                    lst.append(x)
                            else: 
                                if found==0:
                                    print(f"Error: Variable {j[2]} not defined in line {c_op} in line {c_op} in line {c_op}")
                                    found_error=1
                                    l_err.append(f"Error: Variable {j[2]} not defined in line {c_op} in line {c_op} in line {c_op}")
                                elif l_error==0:
                                    print(f'Error: Misuse of label as variable in line {c_op}')
                                    found_error=1
                                    l_err.append(f'Error: Misuse of label as variable in line {c_op}')
                                
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
                            x=E_u_jump(j,label_value)
                            lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variable as label in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label in line {c_op}')
                        elif lbl==0:
                            print(f'Error: Label not found in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Label not found in line {c_op}')
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
                            
                            x=E_u_jump(j,label_value)
                            lst.append(x)
                    else:
                        if found==1: 
                            print(f'Error: Misuse of variable as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print(f'Error: Label not found in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Label not found in line {c_op}')
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
                            x=E_jumpifg(j,label_value)
                            lst.append(x)
                    else: 
                        if found==1:
                            print(f'Error: Misuse of variabel as label')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label')
                        elif lbl==0:
                            print(f'Error: Label not found in line {c_op}')
                            l_err.append(f'Error: Label not found in line {c_op}')
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
                            
                            lst.append(x)
                    else:
                        if found==1:
                            print(f'Error: Misuse of variable as label in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Misuse of variable as label in line {c_op}')
                        elif lbl==0:
                            print(f'Error: Label not found in line {c_op}')
                            found_error=1
                            l_err.append(f'Error: Label not found in line {c_op}')
            elif j[0] in type_F:
                if j[0]=="hlt" and "hlt" in l[len(l)-1]:
                    hlt_count+=1
                    if found_error==0:
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
                
                
            elif j[0] in label_value:
                continue
            elif j[0] not in type_A+type_B+type_C+type_D+type_E+type_F and j[0] not in label_value and j[0]!="var" and j[0][0:lenght_of_list-1] not in label_value:
                print(f"Error Invalid Instruction: {j[0]} in line {c_op}")
                l_err.append(f"Error Invalid Instruction: {j[0]} in line {c_op}")
                found_error=1
        else:
            print(f'General Syntax Error at line {c_op} ')
            found_error=1
            l_err.append(f'General Syntax Error at line {c_op} ')


if l_err==[]:
    for line in lst:
            
            print(line)  
    else:
        for i in l_err:
            print(i)