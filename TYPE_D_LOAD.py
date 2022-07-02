import DICT_VALUE as l
import Unused_bit as U

def integertobinary(x):
    s = ""
    if(x == 0):
        s = "00000000"
        return s

    while(x > 0):

        if(x % 2 == 1):
            s = "1" + s
    
        else:
            s = "0" + s
    
        x //=  2  

    y = 8 - len(s)
    temp = ""
    while(y):
        temp += "0"
        y -=1

    s = temp + s
    return(s)



user=[x for x in input().split()]
def D_load(user):
 val=l.op_code["ld"]
 valueR1=l.op_code[user[1]]
 x = int(user[2])
 s = integertobinary(x)
 return(val+valueR1+s)