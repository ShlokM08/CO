import DICT_VALUE as d
import Unused_bit as U
def E_jump_less(inp,dict):
    for i in dict.keys():
        if i==inp[1]:
            mem_addr=dict[i]
            s=d.op_code[inp[0]]+U.unused['E']+mem_addr
            return s