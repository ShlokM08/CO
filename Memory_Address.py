#var_list=['abc', 'yoo', 'tyi']
def mem_add(total_lines,number_of_var,var_list):
    for i in range(0,len(var_list)):
        var_mem_address=var_list[i]
        #print(var_mem_address)
        var_mem_address=total_lines-number_of_var
        
        total_lines+=7
        return var_mem_address 
    #

#print(mem_add(7,4,var_list))