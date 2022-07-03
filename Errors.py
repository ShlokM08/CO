
import DICT_VALUE as d

def keypresent(j):
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
    