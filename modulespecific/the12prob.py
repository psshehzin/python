from itertools import permutations
n=int(input())
a=['2']
b=['1']
fperm=[]
for i in range(0,n+1):
    temp1=b*(n-2*i)
    temp2=a*i
    ctemp=temp1+temp2
    if i>len(ctemp)+1:
        break
    tperm=set(permutations(ctemp,len(ctemp)))
    tperm=list(tperm)
    valueh=[]
    for i in tperm:
        if not '22' in ("".join(list(i))):
            valueh.append(i)
    fperm.extend(valueh)
print(fperm)
count=len(fperm)    
print(f"ways = {count}")