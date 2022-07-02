import DICT_VALUE as value

#opcode=5bits unused_bits=11bits


def F_hlt(to_encode):
    x=""
    while len(x) < 11:
        x += '0'
    binary_encoding=""
    if to_encode[0]=="hlt":
        binary_encoding=value.op_code["hlt"]
    binary_encoding+=x
    print(binary_encoding)
#\hlt(to_encode)