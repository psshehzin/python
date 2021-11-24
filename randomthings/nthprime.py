n = int(input())
b=1
i=2
while b<=n:
    flag=0
    for j in range(2,i):
        if (i%j==0) and i!=j:
            flag=1
            break
    if flag==0:
        if(b==n):
            print(f"{i} is the {n}th prime")
            break
        else:
           b=b+1
           i=i+1
    else:
        i=i+1