import DICT_VALUE as d
import Unused_bit as ub
inp=[i for i in input().split()]
s=''
if inp[0]=='sub':
    s+=d.op_code['sub']
elif inp[0]=='or':
    s+=d.op_code['or']
s+=ub.unused["A"]+d.op_code[inp[1]]+d.op_code[inp[2]]+d.op_code[inp[3]]
print(s)
