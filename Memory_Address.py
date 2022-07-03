#var_list=['abc', 'yoo', 'tyi']
'''def mem_add(total_lines,number_of_var,var_list):
    for i in range(0,len(var_list)):
        var_mem_address=var_list[i]
        #print(var_mem_address)
        var_mem_address=total_lines-number_of_var
        
        total_lines+=7
        return var_mem_address 
    #

#print(mem_add(7,4,var_list))'''

L=["hlt","var x","mov R1 R2 R3"]
l1=[]
for i in L:
    x=i.split(" ")
    l1.append(x)
print(l1)
for i in l1:
    if "var" not in l1[0]:
        print("ERROR")
        break
    

'''for i in L:
    if "var" in L[i].split(" "):
        print("yes")
    elif 'var' not in L:
        print("NO")'''