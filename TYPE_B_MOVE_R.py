import DICT_VALUE as value
import Unused_bit as U
#add R1 SImm
#opcode=5bits reg1=3bits Immediate Valye=8bits 
to_encode=[x for x in input().split()]
x=to_encode[2].split("$")
'''def xor(to_encode):
    binary_encoding=""
    if to_encode[0]=="and":
        binary_encoding=value.op_code["and"]
    binary_encoding+=U.unused["A"]+value.op_code[to_encode[1]]+value.op_code[to_encode[2]]+value.op_code[to_encode[3]]
    print(binary_encoding)
xor(to_encode)'''
print(bin(int(x[1])))