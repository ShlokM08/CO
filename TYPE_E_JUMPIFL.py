import DICT_VALUE as d
import Unused_bit as U
inp=[i for i in input().split()]
with open("TO_READ.txt") as f:
    file_read=f.read().split('\n')
    for i in range(len(file_read)):
        if inp[1] in file_read[i]:
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
s=d.op_code[inp[0]]+U.unused['E']+mem_addr
print(s)