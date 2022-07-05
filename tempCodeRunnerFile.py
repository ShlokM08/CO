    if j[0] in type_A:
                    try:
                        if j[0]=="add":
                            found=0
                            print(A_add(j))
                            x=A_add(j)
                            lst.append(x)
                        elif j[0]=="sub":
                            print(A_sub(j))
                            x=A_sub(j)
                            lst.append(x)
                        elif j[0]=="mul":
                            print(A_mul(j))
                            x=A_mul(j)
                            lst.append(x)
                        elif j[0]=="xor":
                            print(A_xor(j))
                            x=A_xor(j)
                            lst.append(x)
                        elif j[0]=="and":
                            print(A_and(j))
                            x=A_and(j)
                            lst.append(x)
                        elif j[0]=="or":
                            print(A_or(j))
                            x=A_or(j)
                            lst.append(x)
                    except:
                        print(f'ERROR:Undefined Register in line {l.index(j)+1}')