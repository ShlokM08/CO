
import DICT_VALUE as d 
import STDIN1


def keypresent(j):
   
    for each in j:

        if each not in d:
            print("Typos in instruction name or register name")
            return False
    
    
    return True

    