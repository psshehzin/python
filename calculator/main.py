def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def calc(operator,ind,operands,values,calcfunc):
    result=[]
    #calcfunc here is a dictionary that has values as function names for operations and keys as operands
    result.append(calcfunc[operator](values[ind],values[ind+1]))
    operands=operands[:ind]+operands[ind+1:]
    values=values[:ind]+result+values[ind+2:]
    return operands,values
operations=['+','-','/','*']
expression=input("enter the expression example 2+3+5*3: ")
#to separate numbers and operations
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
for j in temp1:
   if j not in operations:
       numb+=j
   else:
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
print(f"The result of the expresion {expression} is = {values[0]}")