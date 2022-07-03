
from re import X
import DICT_VALUE as value
#rs R1 SImm
#rs R1 $10
#opcode=5bits reg1=3bits Immediate Valye=8bits 
'''to_encode=[x for x in input().split()]
x=to_encode[2].split("$")
a=int(x[1])
#print(a)
bnr = bin(a).replace('0b','')

x = bnr[::-1] #this reverses an array
while len(x) < 8:
    x += '0'
bnr = x[::-1]'''
#to_encode=[x for x in input().split()]
def B_rs(to_encode):
    x=to_encode[2].split("$")
    for ch in range(1,len(x)):
        #print("Value",type(x[ch]))
        bnr = bin(int(x[ch])).replace('0b','')
        #print(bnr)
        x = bnr[::-1] #this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        if to_encode[0]=="rs":
                binary_encoding=value.op_code["rs"]
        binary_encoding+=value.op_code[to_encode[1]]+bnr
        return binary_encoding
        '''s=""
        for ch in x:
            if ch !="$":
                    s+=ch
            print("Hello",ch)
            bnr = bin(int(ch[1])).replace('0b','')
            print("BIN",x)
            ch= bnr[::-1] #this reverses an array
            print("e",ch)
            while len(ch) < 8:
                ch += '0'
            #bnr = ch[::-1]
            binary_encoding=""
            if to_encode[0]=="rs":
                binary_encoding=value.op_code["rs"]
            binary_encoding+=value.op_code[to_encode[1]]+bnr
            print(binary_encoding)'''
#B_rs(to_encode)

