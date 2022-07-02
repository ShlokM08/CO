import DICT_VALUE as l
import Unused_bit as U

def mul():
  
  user=[x for x in input().split()]
  val=l.op_code["mul"]
  valueR1=l.op_code[user[1]]
  valueR2=l.op_code[user[2]]
  valueR3=l.op_code[user[3]]
  return (val+U.unused["A"]+valueR1+valueR2+valueR3)
