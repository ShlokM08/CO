import DICT_VALUE as l
import Unused_bit as U

user=[x for x in input().split()]

def b_leftshift(user):
    
    val=l.op_code["ls"]
    valueR1=l.op_code[user[1]]
    valueR2=user[2][1:]
    x = int(valueR2)
    s = ""
    if(x == 0):
        s = "00000000"
    while(x > 0):
        if(x % 2 == 1):
            s = "1" + s
    
        else:   
            s = "0" + s
    
        x //= 2

    y = 8 - len(s)
    temp = ""
    while(y):
        temp += "0"
        y -=1

    s = temp + s

    return(val+valueR1+s)