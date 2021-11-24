ab=[0,1,1,0,1,1,1]
a=0
c=0
for i in ab:
    if i==1:
        a+=1
    elif i==0:
        if(a>c):
            c=a
            a=1
print(c)    


