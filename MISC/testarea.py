def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
def permcalc(a,b):
    factt=factorial(a+b)/(factorial(a)*factorial(b))
    return factt
n=int(input())
out=0
for i in range(0,n+1):
    count2=i
    count1=n-2*i
    if(count2>count1+1):
        break
    factt=permcalc(count2,count1)
    j=1
    c=0
    val=0
    if (count2>1):
       if(count2%2==0):
           tempor=count2//2
           val=permcalc(tempor,count1)
       else:
           tempor=count2//2
           val=permcalc(tempor,count1)-permcalc(1,count1)
    out=out+factt-val
print(out)

