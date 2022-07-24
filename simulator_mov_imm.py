op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#=====================================================================================================================
reg_val={"R0":"0","R1":"6","R2":"2","R3":"0","R4":"0","R5":"0","R6":"0","FLAGS":"0"}


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
