import DICT_VALUE as l
import Unused_bit as U

def E_u_jump(user, d): 
    val=l.op_code["jmp"]
    for i in d.keys():
        if i==user[1]:
            s=d[i]
            break
    return (val+U.unused["E"]+s)