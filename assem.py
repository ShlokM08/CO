
import re


op_code={"add":"10000","sub":"10001","mov_I":"10010","mov_R":"10011","ld":"10100"
,"st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011"
,"and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010",
"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}



#=====================================================================================================================
def temp_add(s):
    x=bin(int(s[-7:-10:-1][::-1],2)+int(s[-4:-7:-1][::-1],2))
    return x[2:]

#=====================================================================================================================

'''new_reg={}

s="1000000001010011"

st_value=s[0:5]
#print(s[-7:-10:-1][::-1])
#print(s[-4:-7:-1][::-1])
if st_value in op_code.values():
    if st_value=="10000":
        new_val=temp_add(s)
        print(new_val)
else:
    print("no")'''

#R1=0
reg_val={"R1":"0","R2":"0","R3":"0","R4":"0","R5":"0","R6":"0"}
x=["mov","R1","10"]
z=["mov","R2","20"]
#y=["add","R1","R2","R3"]
y="1000000001010011"
if x[0]=="mov" and  x[1] in reg_val.keys():
    reg_val[x[1]]=x[2]

if z[0]=="mov" and  z[1] in reg_val.keys():
    reg_val[z[1]]=z[2]
print(reg_val)
'''if y[0]=="add" and y[1] in reg_val.keys() and y[2] in reg_val.keys() and y[3] in reg_val.keys():
    reg_val[y[3]]=int(reg_val[y[1]])+int(reg_val[y[2]])'''
if y[0:5]=="10000": #and int(y[-7:-10:-1][::-1],2) in op_code.values() and int(y[-4:-7:-1][::-1],2) in op_code.values():
    print(bin(int(y[-7:-10:-1][::-1])))
    print(bin(int(y[-4:-7:-1][::-1])))
    print("Hey")
else:
    print("crash")
#print(n)
print("update",reg_val)


















'''L=["10000","00","001","010","011"]
def temp_add(L):
    x=0
    #for i in L:
    if L[0]=="10000":
        #return int(L[-2])
        x=bin(int(L[-1],2)+int(L[-2],2))
        return x[2:]
print(temp_add(L))'''
