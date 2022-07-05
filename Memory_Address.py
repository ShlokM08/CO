j=["label:","alt"]
l=[]
for i in j:
    if i=="alt":
        l.append(i)
        j.pop()
        
print(j)
print(l)