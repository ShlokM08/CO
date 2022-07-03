import DICT_VALUE as d
import Unused_bit as U
def D_store(inp,dict):
    for i in dict.keys():
        if i==inp[2]:
            mem_addr=dict[i]
            break
    s=d.op_code[inp[0]]+d.op_code[inp[1]]+mem_addr
    return s