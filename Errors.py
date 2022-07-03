
import DICT_VALUE as d

def keypresent(j):
    for each in j:
        if each not in d.op_code.keys():
            print("Typos in instruction name or register name")
            return False
    
    
    return True

    