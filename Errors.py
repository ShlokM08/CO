
from re import X
import DICT_VALUE as d

'''def keypresent(j):
    if 'mov' in j[0]:
        if j[0]!='mov':
            print("Typos in instruction name or register name")
            return False
    for each in j:
        if each!='mov':
            if each not in d.op_code.keys():
                print("Typos in instruction name or register name")
                return False
    return True
    '''
'''l=["label:","mov r1,r2","mov r1,#10","mov r1,r2,r3"]
Lo=[]
for i in l:
    x=i.split(":")
    Lo.append(x)

if Lo[0][0]=="label":
    print(f"label in line{l.index(j)+1}")'''

j=['label:', 'add', 'R1', 'R2', 'R3']
j1=[]
for v in j:
    x=v.split(":")
    j1.append(x)
for t in j1:
    if len(t)>1:
        print(t[0])
    #print(len(t))
    '''if j1[t][0]=="label":
        #print(f"label in line{j1.index(t)+1}")
        print("YES")'''
#print(j1[0][0])