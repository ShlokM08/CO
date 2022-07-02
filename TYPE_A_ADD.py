import DICT_VALUE as value
import Unused_bit as U
import STDIN as stdin
#add R1 R2 R3
#opcode=5bits unused=3bits reg1=3bits reg2=3bits reg3=3bits

def add():
    binary_encoding=""
    if stdin.to_read[0]=="add":
        binary_encoding=value.op_code["add"]
    binary_encoding+=U.unused["A"]+value.op_code[stdin.to_read[1]]+value.op_code[stdin.to_read[2]]+value.op_code[stdin.to_read[3]]
    print(binary_encoding)
add(stdin.to_read)