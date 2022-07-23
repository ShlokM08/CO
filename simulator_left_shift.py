#=====================================================================================================================
op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#=====================================================================================================================
reg_val={"R0":"0","R1":"6","R2":"2","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0"}
'''x=["mov","R1","10"]
z=["mov","R2","20"]'''
#=====================================================================================================================
y="1100100100000101"
#=====================================================================================================================
def simulator_left_shift(y):
    if y[0:5] =="11001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-7:-10:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-9:-12:-1][::-1]:
                    print(i)
                    print(reg_val[i])
                    temp_sum_1=int(reg_val[i])
                    #print(reg_val[i]) #value stored in  register in dict reg_value
                if op_code[i]==y[-4:-7:-1][::-1]:
                    print(i)
                    print(reg_val[i])
                    #print(reg_val[i])

                
                    temp_sum_2=int(reg_val[i])
                
                def sim_left_shift(temp_sum_1,temp_sum_2):
                    #import numpy as np
                    x=temp_sum_1<<temp_sum_2
                    return x
    new_dict_val=sim_left_shift(temp_sum_1,temp_sum_2)
    if y[0:5] =="11001": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
        if y[-1:-4:-1][::-1] in op_code.values():
            for i in op_code.keys():
                if op_code[i]==y[-1:-4:-1][::-1]:
                    reg_val[i]=new_dict_val                   #format(new_dict_val,"016b")

simulator_left_shift(y)
print(reg_val)