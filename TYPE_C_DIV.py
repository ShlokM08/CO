import DICT_VALUE as value
import Unused_bit as U
#add R1 R2 R3
#opcode=5bits unused=3bits reg1=3bits reg2=3bits reg3=3bits
to_encode=[x for x in input().split()]
def div(to_encode):
    binary_encoding=""
    if to_encode[0]=="div":
        binary_encoding=value.op_code["div"]
    binary_encoding+=U.unused["C"]+value.op_code[to_encode[1]]+value.op_code[to_encode[2]]
    print(binary_encoding)
div(to_encode)