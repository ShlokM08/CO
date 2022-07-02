import DICT_VALUE as d
import Unused_bit as ub
#inp=[i for i in input().split()]
def C_not(inp):
    s=""
    if inp[0]=="not":
        s=d.op_code["not"]
    s+=ub.unused['C']+d.op_code[inp[1]]+d.op_code[inp[2]]
    print(s)
#C_not(inp)

'''binary_encoding=""
    if to_encode[0]=="and":
        binary_encoding=value.op_code["and"]'''