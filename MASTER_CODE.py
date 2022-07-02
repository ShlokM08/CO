import TYPE_B_MOVE_IM as mov_i
with open('STDIN.txt', 'w') as f:
    while True:
        instr=input()
        instr+='\n'
        f.write(instr)
        if 'hlt' in instr:
            break
l=[]
with open("STDIN.txt") as f:
    file_read=f.read().split('\n')
    for to_read in file_read:
        to_read=to_read.split()
        if to_read[0]=='mov':
            if '$' in to_read[2]:
                l.append(mov_i)