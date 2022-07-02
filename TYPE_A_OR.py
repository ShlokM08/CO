import DICT_VALUE as d
import Unused_bit as ub
inp=[i for i in input().split()]
def a_or(inp):
    s=d.op_code['or']+ub.unused["A"]+d.op_code[inp[1]]+d.op_code[inp[2]]+d.op_code[inp[3]]
    return s