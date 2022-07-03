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

def E_u_jump(user): 
 val=l.op_code["jgt"]
 with open("TO_READ.txt") as f:
        file_read=f.read().split('\n')
        for i in range(len(file_read)):
            if user[2] in file_read[i]:
                i+=1
                break
        num=len(file_read)-i
 s = integertobinary(num)
 return (val+U.unused["E"]+s)