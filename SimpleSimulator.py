import sys

#=====================================================================================================================
op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#=====================================================================================================================
reg_val={"R0":"0","R1":"6","R2":"2","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0"}
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
print(simulator_div('1011100000011100'))
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

for elements in input_elements:
    if elements[0:5]=="10000":
        simulator_add(elements)#
    elif elements[0:5]=="11100":
        simulator_and(elements)#
    elif elements[0:5]=="10111":
        simulator_div(elements)#
    elif elements[0:5]=="11001":
        simulator_left_shift(elements)#
    elif elements[0:5]=="10011":
        simulator_mov_r(elements)#
    elif elements[0:5]=="10110":
        simulator_mul(elements)#
    elif elements[0:5]=="11101":
        simulator_not(elements)#
    elif elements[0:5]=="10101":
        simulator_str(elements,mem_addr)#
    elif elements[0:5]=="10001":
        simulator_sub(elements)#
    elif elements[0:5]=="11010":
        simulator_xor(elements)#
    elif elements[0:5]=="10100":
        simulator_ld(elements)#
    else:
        print("Invalid Instruction")
        break