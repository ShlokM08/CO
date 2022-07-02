import DICT_VALUE as l
import Unused_bit as U
import TYPE_A_ADD as add
import TYPE_B_MOVE_IM as move_im
with open("TO_READ.txt") as f:
    file_read=f.read().split('\n')
    for to_read in file_read:
        to_read=to_read.split()
        print(to_read)
        '''if to_read[0]=="mov" and to_read[2]=="R1" or to_read[2]=="R2" or to_read[2]=="R3":
            move_im.mov_I(to_read)'''
        '''if to_read[0]=="add":
            add.add(to_read)'''
            
            