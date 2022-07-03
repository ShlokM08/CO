import DICT_VALUE as l
import Unused_bit as U

def D_load(user,d):
    val=l.op_code["ld"]
    valueR1=l.op_code[user[1]]
    for i in d:
        if i==user[2]:
            s=d[i]
            break
    return(val+valueR1+s)