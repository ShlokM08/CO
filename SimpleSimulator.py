import sys
#=====================================================================================================================
op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#=====================================================================================================================
reg_val={"R0":"0","R1":"0","R2":"0","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0000"}
#===============================================================================================================================
mem_addr={}
#=====================================================================================================================
#======================================================================================================================
#FUNCTIONS FOR SIMULATOR
def simulator_add(y):
    #if y[0:5] =="10000": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
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
        if new_dict_val>(2**16)-1:
            reg_val['FLAGS']='1000'
            return 'Overflow'
    #if y[0:5] =="10000": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")
#===============================================================================================================================
def simulator_and(y):
    if y[0:5] =="11100": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-7:-10:-1][::-1]:
        
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                if op_code[i]==y[-4:-7:-1][::-1]:
                
                    temp_sum_2=int(reg_val[i])
                
                def sim_and(temp_sum_1,temp_sum_2):
                    if temp_sum_1>temp_sum_2:
                        return temp_sum_1
                    elif temp_sum_2>temp_sum_1:
                        return temp_sum_2
    new_dict_val=sim_and(temp_sum_1,temp_sum_2)
    if y[0:5] =="11100": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")
#===============================================================================================================================
def simulator_div(y):
    r3_ad=y[10:13]
    r4_ad=y[13:16]
    for i in op_code:
        if op_code[i]==r3_ad:
            r3=i
        elif op_code[i]==r4_ad:
            r4=i
    r3=int(reg_val[r3])
    r4=int(reg_val[r4])
    reg_val['R0']=int(r3/r4)
    reg_val['R1']=r3-(int(r3/r4)*r4)
    return reg_val['R0'], reg_val['R1']

#===============================================================================================================================
def simulator_left_shift(y):
    if y[0:5] =="11001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-9:-12:-1][::-1]:
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                temp_sum_2=y[-1:-9:-1][::-1]

                def bin_to_dec(temp_sum_2):
                    binary = temp_sum_2
                    decimal = 0
                    for digit in binary:
                        decimal= decimal*2 + int(digit)
                    return decimal
    
            bin_val_temp2=bin_to_dec(temp_sum_2)                 
            def sim_left_shift(bin_val_temp2,temp_sum_1):
                print(bin_val_temp2,temp_sum_1)
                x=int(bin_val_temp2)<<temp_sum_1
                return x
                
        new_dict_val=sim_left_shift(bin_val_temp2,temp_sum_1)
        for i in op_code.keys():
            if op_code[i]==y[-9:-12:-1][::-1]:
                reg_val[i]=new_dict_val
#===============================================================================================================================
def simulator_ld(y, mem_addr):
    mem_add=y[8:16]
    r=y[5:8]
    for i in op_code:
        if op_code[i]==r:
            r=i
            break
    if mem_add in mem_addr:
        reg_val[r]=mem_addr[mem_add]
        return reg_val[r]
    else:
        return 'Error: Variable not found'
#===============================================================================================================================
def simulator_mov_r(y):
    if y[0:5] =="10011": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-7:-10:-1][::-1]:
        
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                if op_code[i]==y[-4:-7:-1][::-1]:
                
                    temp_sum_2=int(reg_val[i])
                
                def sim_mov_r(temp_sum_1,temp_sum_2):
                    temp_sum_1==temp_sum_2
                    return temp_sum_2
                   
    new_dict_val=sim_mov_r(temp_sum_1,temp_sum_2)
    if y[0:5] =="10011": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")
#===============================================================================================================================
def simulator_mul(y):
    r1=y[7:10]
    r2=y[10:13]
    r3=y[13:16]
    for i in op_code:
        if op_code[i]==r1:
            r1_val=int(reg_val[i])
        elif op_code[i]==r2:
            r2_val=int(reg_val[i])
        elif op_code[i]==r3:
            r3_val=int(reg_val[i])
            r3_k=i
    r3_val=r1_val*r2_val
    if r3_val>(2**16)-1:
        reg_val['FLAGS']='1000'
        return 'Overflow'
    reg_val[r3_k]=r3_val
    return r3_val
#===============================================================================================================================
def simulator_not(y):
    r1_ad=y[10:13]
    r2_ad=y[13:16]
    for i in op_code:
        if op_code[i]==r1_ad:
            r1=i
        elif op_code[i]==r2_ad:
            r2=i
    reg_val[r2]=~int(reg_val[r1])
    return reg_val[r2]
#===============================================================================================================================
def simulator_str(y, mem_addr):
    mem_add=y[8:16]
    r=y[5:8]
    for i in op_code:
        if op_code[i]==r:
            r=i
            break
    mem_addr[mem_add]=reg_val[r]
    return mem_addr[mem_add]
#===============================================================================================================================
def simulator_sub(y):
    if y[0:5] =="10001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-7:-10:-1][::-1]:
        
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                if op_code[i]==y[-4:-7:-1][::-1]:
                    temp_sum_2=int(reg_val[i])
                
                def sim_sub(temp_sum_1,temp_sum_2):
                    return temp_sum_1-temp_sum_2
    new_dict_val=sim_sub(temp_sum_1,temp_sum_2)
    if len(bin(new_dict_val))>len(bin(65535)):
        reg_val['FLAGS']='1000'
        return 'Overflow'
    elif new_dict_val<0:
        reg_val['FLAGS']='1000'
        return 'Overflow'
    if y[0:5] =="10001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")
#===============================================================================================================================
def simulator_xor(y):
    r1=y[7:10]
    r2=y[10:13]
    r3=y[13:16]
    for i in op_code:
        if op_code[i]==r1:
            r1_val=int(reg_val[i])
        elif op_code[i]==r2:
            r2_val=int(reg_val[i])
        elif op_code[i]==r3:
            r3_val=int(reg_val[i])
            r3_k=i
    r3_val=r1_val^r2_val
    reg_val[r3_k]=r3_val
    return r3_val
def simulator_cmp(y):
    r1_ad=y[10:13]
    r2_ad=y[13:16]
    for i in op_code:
        if op_code[i]==r1_ad:
            r1=i
        elif op_code[i]==r2_ad:
            r2=i
    if int(reg_val[r1])<int(reg_val[r2]):
        reg_val['FLAGS']='0100'
    elif int(reg_val[r1])>int(reg_val[r2]):
        reg_val['FLAGS']='0010'
    elif int(reg_val[r1])==int(reg_val[r2]):
        reg_val['FLAGS']='0001'
def bin_to_dec(temp_sum_2):
                    binary = temp_sum_2
                    decimal = 0
                    for digit in binary:
                        decimal= digit*2**(len(binary)-1) + int(decimal)
                    return decimal

def simulator_mov_im(y):
    reg1=y[5:8:]
    value=y[8::]
    for i in op_code:
        if op_code[i]==reg1:
            reg1_val=int(reg_val[i])
            reg1_k=i

        def binarytodec(value):
            binary=value
            bin_to_dec=0
            for num in binary:
                bin_to_dec=bin_to_dec*2 +int(num)
            return bin_to_dec

    reg1_val=binarytodec(value)
    reg_val[reg1_k]=reg1_val
    return reg_val

def simulator_right_shift(y):
    if y[0:5] =="11001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-9:-12:-1][::-1]:
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                temp_sum_2=y[-1:-9:-1][::-1]

                def bin_to_dec(temp_sum_2):
                    binary = temp_sum_2
                    decimal = 0
                    for digit in binary:
                        decimal= decimal*2 + int(digit)
                    return decimal
    
            bin_val_temp2=bin_to_dec(temp_sum_2)                 
            def sim_right_shift(bin_val_temp2,temp_sum_1):
                print(bin_val_temp2,temp_sum_1)
                x=int(bin_val_temp2)>>temp_sum_1
                return x
                
        new_dict_val=sim_right_shift(bin_val_temp2,temp_sum_1)
        for i in op_code.keys():
            if op_code[i]==y[-9:-12:-1][::-1]:
                reg_val[i]=new_dict_val

def simulator_or(y):
    register1 = y[7:10]
    register2 = y[10:13]
    register3 = y[13:16]
    valR1 = 0
    valR2 = 0
    valR3 = 0
    for each in op_code :
        if(op_code[each] == register1):
            valR1 = int(reg_val[each])
        
        if(op_code[each] == register2):
            valR2 = int(reg_val[each])
        
        if (op_code[each]==register3):
            R3 = each

    valR3 = valR1 | valR2
    reg_val[R3]=valR3
    return valR3
#===============================================================================================================================
#===============================================================================================================================
#MASTER CODE

input_elements=[]
asii=[]
for line in sys.stdin:
    asii.append(line.rstrip())
for line in asii:
    if line!='':
        input_elements.append(line)
total_line=len(input_elements)
def simulator_jgt(y):
    mem=y[8:16]
    if reg_val['FLAGS']=='0010':
        c=bin_to_dec(mem)
        #line_num=input_elements[c-1]
        return c
def simulator_jmp(y):
    c=0
    mem=y[8:16]
    c=bin_to_dec(mem)
    #line_num=input_elements[c-1]
    return c
def simulator_jlt(y):
    c=0
    mem=y[8:16]
    if reg_val['FLAGS']=='0100':
        c=bin_to_dec(mem)
        #line_num=input_elements[c-1]
        return c
def simulator_je(y):
    mem=y[8:16]
    c=0
    if reg_val['FLAGS']=='0001':
        c=bin_to_dec(mem)
        #line_num=input_elements[c-1]
        return c
current=0
PC=0 #current cycle number
simulator=[]
s=''
while True:
    found=0
    s=''
    if input_elements[current][0:5]=="10000":
        simulator_add(input_elements[current])#
    elif input_elements[current][0:5]=="11100":
        simulator_and(input_elements[current])#
    elif input_elements[current][0:5]=="10111":
        simulator_div(input_elements[current])#
    elif input_elements[current][0:5]=="11001":
        simulator_left_shift(input_elements[current])#
    elif input_elements[current][0:5]=="10011":
        simulator_mov_r(input_elements[current])#
        if input_elements[current][10:13]=='111':
            reg_val['FLAGS']='0000'
            found=1
    elif input_elements[current][0:5]=="10110":
        simulator_mul(input_elements[current])#
    elif input_elements[current][0:5]=="11101":
        simulator_not(input_elements[current])#
    elif input_elements[current][0:5]=="10101":
        simulator_str(input_elements[current],mem_addr)#
    elif input_elements[current][0:5]=="10001":
        simulator_sub(input_elements[current])#
    elif input_elements[current][0:5]=="11010":
        simulator_xor(input_elements[current])#
    elif input_elements[current][0:5]=="10100":
        simulator_ld(input_elements[current], mem_addr)#
    elif input_elements[current][0:5]=="10010":
        simulator_mov_im(input_elements[current])#
    elif input_elements[current][0:5]=="11000":
        simulator_right_shift(input_elements[current])#
    elif input_elements[current][0:5]=="11011":
        simulator_or(input_elements[current])#
    elif input_elements[current][0:5]=="11110":
        simulator_cmp(input_elements[current])#
        found=1
    elif input_elements[current][0:5]=="01101":
        simulator_jgt(input_elements[current])#
        try:
            current=print(int(simulator_jgt(input_elements[current])))-2
        except:
            continue
        
    elif input_elements[current][0:5]=="01111":
        simulator_je(input_elements[current])#
        try:
            current=print(int(simulator_je(input_elements[current])))-2
            found=1
        except:
            continue
    elif input_elements[current][0:5]=="01100":
        simulator_jlt(input_elements[current])#
        try:
            current=print(int(simulator_jlt(input_elements[current])))-2
        except:
            continue
    elif input_elements[current][0:5]=="11111":
        simulator_jmp(input_elements[current])#
        try:
            current=print(int(simulator_jmp(input_elements[current])))-2
        except:
            continue
    
    flg='0'*(12)+reg_val['FLAGS']
    s+=format(int(PC),'08b')+' '+format(int(reg_val['R0']),'016b')+' '+format(int(reg_val['R1']),'016b')+' '+format(int(reg_val['R2']),'016b')+' '+format(int(reg_val['R3']),'016b')+' '+format(int(reg_val['R4']),'016b')+' '+format(int(reg_val['R5']),'016b')+' '+format(int(reg_val['R6']),'016b')+' '+flg
    simulator.append(s)
    reg_val['FLAGS']='0000'
    if input_elements[current][0:5]=='01010':
        break
    current+=1
    PC+=1
for line in simulator:
    print(line)
for line in input_elements:
    print(line)
c=0
for line in mem_addr:
    if mem_addr[line]!='0':
        print(format(int(mem_addr[line]),'016b'))
        c+=1
for i in range(256-len(input_elements)-c):
    print("0"*16)
