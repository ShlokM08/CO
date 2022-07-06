'''import DICT_VALUE as value
import Unused_bit as U
#import TYPE_A_ADD as add
#import package.TYPE_A_ADD
from TYPE_A_ADD import *
#import TYPE_A       # (3) Alternate absolute import
L=[]
import TYPE_B_MOVE_IM as move_im
with open("TO_READ.txt") as f:
    file_read=f.read().split('\n')
    #print(file_read)
    for to_read in file_read:
        #print(to_read[0])
        to_read=to_read.split()
        print(type(to_read))
        print(to_read[0])
        #vL.append(to_read)
        def add(to_read):
            binary_encoding=""
            if to_read[0]=="add":
                binary_encoding=value.op_code["add"]
            binary_encoding+=U.unused["A"]+value.op_code[to_read[1]]+value.op_code[to_read[2]]+value.op_code[to_read[3]]
            print(binary_encoding)
        #add(to_read)'''
  