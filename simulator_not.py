op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
reg_val={"R0":"0","R1":"10","R2":"4","R3":"5","R4":"2","R5":"0","R6":"0","FLAGS":"0"}

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
print(simulator_not('1110100000001010'))