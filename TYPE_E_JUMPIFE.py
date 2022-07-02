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
def E_jumpife(user):
 val=l.op_code["jgt"]
 x = int(user[1])
 s = integertobinary(x)
 return (val+U.unused["E"]+s)