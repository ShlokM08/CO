import DICT_VALUE as value
#add R1 SImm
#mov R1 $10
#opcode=5bits reg1=3bits Immediate Valye=8bits 
to_encode=[x for x in input().split()]


def C_move_R(to_encode):
    x=to_encode[2].split("$")
    a=int(x[1])
    #print(a)
    bnr = bin(a).replace('0b','')

    x = bnr[::-1] #this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    binary_encoding=""
    if to_encode[0]=="mov":
        binary_encoding=value.op_code["mov_R"]
    binary_encoding+=value.op_code[to_encode[1]]+bnr
    print(binary_encoding)
#move_R(to_encode)
#opcode=5bits reg1=3bits Immediate Valye=8bits