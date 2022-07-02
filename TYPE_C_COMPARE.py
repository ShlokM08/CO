import DICT_VALUE as d
import Unused_bit as ub
def C_compare(inp):
    s=d.op_code['cmp']+ub.unused['C']+d.op_code[inp[1]]+d.op_code[inp[2]]
    return s