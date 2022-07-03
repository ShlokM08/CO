import DICT_VALUE as d
import Unused_bit as ub
def A_sub(inp):
    try:
        s=d.op_code['sub']+ub.unused["A"]+d.op_code[inp[1]]+d.op_code[inp[2]]+d.op_code[inp[3]]
        return s
    except:
        return "Error: Undefined Register"

