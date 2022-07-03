import DICT_VALUE as l
import Unused_bit as U

def B_leftshift(user):
    
    val=l.op_code["ls"]
    valueR1=l.op_code[user[1]]
    valueR2=user[2][1:]
    with open("TO_READ.txt") as f:
        file_read=f.read().split('\n')
        for i in range(len(file_read)):
            if valueR2 in file_read[i]:
                i+=1
                break
    num=len(file_read)-i
    mem_addr=''
    while num:
        r=num%2
        mem_addr+=str(r)
        num//=2
    mem_addr=mem_addr[::-1]
    if len(mem_addr)<8:
        mem_addr='0'*(8-len(mem_addr))+mem_addr

    return(val+valueR1+mem_addr)