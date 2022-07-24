op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
reg_val={"R0":"0","R1":"6","R2":"2","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0"}

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

print(simulator_mul('1011000001010011'))