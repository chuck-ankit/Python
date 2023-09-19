L = ["life", "answer", 42, 0]
for thing in L:
 if thing == 0:
    L[thing] = "universe"
 elif thing == 42:
     L[1] = "everything"
     
print(L)


L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.extend(L4)
L3.sort()
del(L3[0])
L3.append(['fa','la'])


print(L3)