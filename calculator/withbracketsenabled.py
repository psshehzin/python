def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def bracketrem(exp):
    temp2=[i for i in exp]
    i=0
    flag=0
    lind=[]
    done=False
    while not (done):
        if "(" not in temp2:
                done=True
        elif (temp2[i]=='('):
            flag+=1
            lind.append(i)
            i=i+1
        elif (temp2[i]==')'):
            result=[]
            flag-=1
            ind1=lind.pop()
            result.append(str(expcalc("".join(temp2[ind1+1:i]))))
            temp2=temp2[0:ind1]+result+temp2[i+1:]
            i=ind1
        else:
            i=i+1
            continue
        
    return("".join(temp2))

def calc(operator,ind,operands,values,calcfunc):
    result=[]
    #calcfunc here is a dictionary that has values as function names for operations and keys as operands
    result.append(calcfunc[operator](values[ind],values[ind+1]))
    operands=operands[:ind]+operands[ind+1:]
    values=values[:ind]+result+values[ind+2:]
    return operands,values
def expcalc(expression):
    temp1=[i for i in expression]
    numb=""
    operationfunc={
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    operands=[]
    values=[]
    if temp1[0] == '-':
        nflag=1
    else:
        nflag=0
    for j in temp1:
        if j not in operations or nflag==1:
            numb+=j
            nflag=0
        else:
            if nflag==0:
                nflag=1
            operands.append(j)
            values.append(float(numb))
            numb=""
        #to append the last number
    values.append(float(numb))
    while(len(operands)!=0):
        if "*" in operands:
            ind=operands.index("*")
            operands,values=calc("*",ind,operands,values,operationfunc)
        elif "/" in operands:
            ind=operands.index("/")
            operands,values=calc("/",ind,operands,values,operationfunc)
        elif "-" in operands:
            ind=operands.index("-")
            operands,values=calc("-",ind,operands,values,operationfunc)
        elif "+" in operands:
            ind=operands.index("+")
            operands,values=calc("+",ind,operands,values,operationfunc)
    return values[0]
res=[]
lind=[]
rind=[]
operations=['+','-','/','*']
expression=input("enter the expression example 2+3+5*3: ")
exp=expression
exp=bracketrem(expression)
result=expcalc(exp)
print(f"Result of the expression {expression} is : {result}")
