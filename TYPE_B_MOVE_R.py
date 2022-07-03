import DICT_VALUE as value
import Unused_bit as U
#add R1 SImm
#mov R1 $10
#opcode=5bits reg1=3bits Immediate Valye=8bits 
#to_encode=[x for x in input().split()]


def C_move_R(to_read):
    binary_encoding=""
    if to_read[0]=="mov":
        binary_encoding=value.op_code["mov_R"]
    binary_encoding+=U.unused["C"]+value.op_code[to_read[1]]+value.op_code[to_read[2]]
    return binary_encoding