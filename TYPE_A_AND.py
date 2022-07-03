import DICT_VALUE as value
import Unused_bit as U
#and R1 R2 R3
#opcode=5bits unused=3bits reg1=3bits reg2=3bits reg3=3bits
#to_encode=[x for x in input().split()]
def A_and(to_encode):
    binary_encoding=""
    if to_encode[0]=="and":
        binary_encoding=value.op_code["and"]
    binary_encoding+=U.unused["A"]+value.op_code[to_encode[1]]+value.op_code[to_encode[2]]+value.op_code[to_encode[3]]
    return binary_encoding
#and_(to_encode)