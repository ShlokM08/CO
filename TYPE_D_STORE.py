import DICT_VALUE as l
import Unused_bit as U
with open("TO_READ.txt") as f:
    file_read=f.read().split('\n')
    for inst in file_read:
        inst=inst.split()