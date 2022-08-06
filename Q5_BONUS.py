
import math
#-------------------------------------------------------------TYPE1------------------------------------------------------------------------------------------------
def type_1():
    instr_len=int(input("Enter Instruction Length:"))
    reg_len=int(input("Enter register Length:"))
    x=input("Enter input Memory:")
    inp_mem=x.split(" ")#inp_mem[1]gives kb mb or gb

    bit_conversion={"kb":2**10,"mb":2**20,"gb":2**30}                     

    for key,value in bit_conversion.items():
        if inp_mem[1]=="kb":
            value=bit_conversion["kb"]
            #print(bit_conversion["kb"])returns value of kb in dict
            break
        elif inp_mem[1]=="mb":
            value=bit_conversion["mb"]
            #print(bit_conversion["kb"])returns value of kb in dict
            break
        elif inp_mem[1]=="gb":
            value=bit_conversion["gb"]
            #print(bit_conversion["kb"])returns value of kb in dict
            break

    inp_final=int(inp_mem[0])*value
    #print(inp_final)
    val_inp= math.log(int(inp_final)) / math.log(2)#2^x
    print("1. Bit Addressable Memory - Cell Size = 1 bit")
    print("2. Nibble Addressable Memory - Cell Size = 4 bit")
    print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
    print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

    addr_type=int(input("Enter your choice:"))
    if addr_type==1:
        addr_pins=val_inp
        print(f"We need minimum {addr_pins} bits to represent an address in this architecture")
        opcode=instr_len-addr_pins-reg_len
        print(f"{opcode} bits will be needed by the opcode")
        filler_bits=instr_len-opcode-reg_len #25-2-5
        print(f"We will need {filler_bits} in Instruction type")
        n_instr=2**opcode
        print(f"It can support a maximum of {n_instr} instructions")
        n_reg=2**reg_len
        print(f"It can support a maximum of {n_reg} instructions")
        addr_type=int(input("Enter your choice:"))
    if addr_type==2:
        nibble= math.log(int(4)) / math.log(2)
        addr_pins=val_inp-nibble
        print(f"We need minimum {addr_pins} bits to represent an address in this architecture")
        opcode=instr_len-addr_pins-reg_len
        print(f"{opcode} bits will be needed by the opcode")
        filler_bits=instr_len-opcode-reg_len #25-2-5
        print(f"We will need {filler_bits} in Instruction type")
        n_instr=2**opcode
        print(f"It can support a maximum of {n_instr} instructions")
        n_reg=2**reg_len
        print(f"It can support a maximum of {n_reg} instructions")
        addr_type=int(input("Enter your choice:"))
    if addr_type==3:
        nibble= math.log(int(8)) / math.log(2)
        addr_pins=val_inp-nibble
        print(f"We need minimum {addr_pins} bits to represent an address in this architecture")
        opcode=instr_len-addr_pins-reg_len
        print(f"{opcode} bits will be needed by the opcode")
        filler_bits=instr_len-opcode-reg_len #25-2-5
        print(f"We will need {filler_bits} in Instruction type")
        n_instr=2**opcode
        print(f"It can support a maximum of {n_instr} instructions")
        n_reg=2**reg_len
        print(f"It can support a maximum of {n_reg} instructions")
        addr_type=int(input("Enter your choice:"))
    if addr_type==4:
        cpu_size=int(input("Enter cpu_size size:"))
        cpu= math.log(int(cpu_size)) / math.log(2)
        addr_pins=val_inp-cpu
        print(f"We need minimum {addr_pins} bits to represent an address in this architecture")
        opcode=instr_len-addr_pins-reg_len
        print(f"{opcode} bits will be needed by the opcode")
        filler_bits=instr_len-opcode-reg_len #25-2-5
        print(f"We will need {filler_bits} in Instruction type")
        n_instr=2**opcode
        print(f"It can support a maximum of {n_instr} instructions")
        n_reg=2**reg_len
        print(f"It can support a maximum of {n_reg} instructions")
        addr_type=int(input("Enter your choice:"))

    if addr_type>4:
        print("Thank You")
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------TYPE2------------------------------------------------------------------------------------------
def type_2():
    #bit_conversion={"kb":2**10,"mb":2**20,"gb":2**30} 
    cpu_size=int(input("Enter CPU size:"))
    addr_pins=int(input("Enter number of address pins:"))
    print("1. Bit Addressable Memory - Cell Size = 1 bit")
    print("2. Nibble Addressable Memory - Cell Size = 4 bit")
    print("3. Byte Addressable Memory - Cell Size = 8 bits(standard)")
    print("4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")

    addr_type=int(input("Enter your choice:"))
    def expo(x):
        p=0
        while(x!=1):
            x=x/2
            p+=1
        return p

    if addr_type ==1:
        if addr_pins>=30:
            reg_num=addr_pins-30
            reg_num=reg_num-3
            print(2**reg_num,"GB")
        if addr_pins>=20 and addr_pins<30:
            reg_num=addr_pins-20
            reg_num=reg_num-3
            print(2**reg_num,"MB")
        if addr_pins>=10 and addr_pins<20:
            reg_num=addr_pins-10
            reg_num=reg_num-3
            print(2**reg_num,"B")
        #addr_type = int(input("Enter your choice: "))
    if addr_type==2:
        if addr_pins>=30:
            addr_pins+=2
            reg_num=addr_pins-30
            reg_num=reg_num-3
            print(2**reg_num,"GB")
        if addr_pins>=20 and addr_pins<30:
            addr_pins+=2
            reg_num=addr_pins-20
            reg_num=reg_num-3
            print(2**reg_num,"MB")
        if addr_pins>=10 and addr_pins<20:
            addr_pins+=2
            reg_num=addr_pins-10
            reg_num=reg_num-3
            print(2**reg_num,"B")
        #addr_type = int(input("Enter your choice: "))
    if addr_type==3:
        if addr_pins>=30:
            addr_pins+=3
            reg_num=addr_pins-30
            reg_num=reg_num-3
            print(2**reg_num,"GB")
        if addr_pins>=20 and addr_pins<30:
            addr_pins+=3
            reg_num=addr_pins-20
            reg_num=reg_num-3
            print(2**reg_num,"MB")
        if addr_pins>=10 and addr_pins<20:
            addr_pins+=3
            reg_num=addr_pins-10
            reg_num=reg_num-3
            print(2**reg_num,"B")
        #addr_type = int(input("Enter your choice: "))
    if addr_type==4:
        if addr_pins>=30:
            addr_pins+=expo(cpu_size)
            reg_num=addr_pins-30
            reg_num=reg_num-3
            print(2**reg_num,"GB")
        if addr_pins>=20 and addr_pins<30:
            addr_pins+=expo(cpu_size)
            reg_num=addr_pins-20
            reg_num=reg_num-3
            print(2**reg_num,"MB")
        if addr_pins>=10 and addr_pins<20:
            addr_pins+=expo(cpu_size)
            reg_num=addr_pins-10
            reg_num=reg_num-3
            print(2**reg_num,"B")
        #addr_type = int(input("Enter your choice: "))

    if addr_type>4:
        print("Thank You")

#--------------------------------------------------------------------------------------------------------------------------------------------------------

Type=int(input("Input the type you want:"))
if Type==1:
    type_1()
elif Type==2:
    type_2()
else:
    print("Enter valid type")


    
    
