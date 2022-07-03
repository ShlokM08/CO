import DICT_VALUE as d
import Unused_bit as ub
def B_mov_i(inp):
    s=d.op_code['mov_I']+d.op_code[inp[1]]
    num=''
    for ch in inp[2]:
        if ch!='$':
            num+=ch
    num=int(num)
    num_bin=''
    while num:
        r=num%2
        num_bin+=str(r)
        num=num//2
    num_bin=num_bin[::-1]
    if len(num_bin)<8:
        num_bin='0'*(8-len(num_bin))+num_bin
    s+=num_bin
    return s

