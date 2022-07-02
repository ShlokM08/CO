import DICT_VALUE as d
import Unused_bit as ub
inp=[i for i in input().split()]
s=''
if inp[0]=='not':
    s+=d.op_code['not']+ub.unused['C']+d.op_code[inp[1]]+d.op_code[inp[2]]
print(s)