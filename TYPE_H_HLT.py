import DICT_VALUE as value

#opcode=5bits unused_bits=11bits

to_encode=[x for x in input().split()]
x=""
while len(x) < 8:
    x += '0'
def hlt(to_encode):
    x=""
    while len(x) < 11:
        x += '0'
    binary_encoding=""
    if to_encode[0]=="hlt":
        binary_encoding=value.op_code["hlt"]
    binary_encoding+=x
    print(binary_encoding)
hlt(to_encode)