a=[3,4,7,9,10,11,20,27]
b=[5,6,7,15,17,21,23,24,25,26,28]
l1=len(a)
l2=len(b)
i=0
j=0
c=[]
while(i!=l1 and j!=l2):
   if a[i]>b[j]:
      c.append(b[j])
      j=j+1
   elif b[j]>a[i]:
      c.append(a[i])
      i=i+1
   else:
      c=c+[a[i]]*2
      i=i+1
      j=j+1
   if j==l2:
      c=c+a[i:]
      break
   elif i==l1:
      c=c+b[j:]
      break
print(c)

