#!/home/shehzin/python/anaconda/bin/python
def display(a,b,c,d,q):
    clear()
    for i in range(0,11):
        if(i==3 or i==7):
            print(q)
        elif(i==1):
             print("".join(a))
        elif(i==5):
            print("".join(b))
        elif(i==9):
            print("".join(c))
        else:
            print(d)
            
def clear():
     system('clear')    
    
from os import system 

print("va va thamara penne")   
def xokalikka():        
       
       l=("   |   |   ")
       q=("---|---|---")
       p='y'                  
       g=1
       
       while p=='y':
            fin=1
            
            clear()
            ze=[]
            
            a=[" "," "," ","|"," "," "," ","|"," "," "," "]
            b=[" "," "," ","|"," "," "," ","|"," "," "," "]
            d=[" "," "," ","|"," "," "," ","|"," "," "," "]
            
            while(fin<10):
                 cd=0
                 qa=1
                 if(g==1):
                      z='x'
                      g=2
                 else:
                      z='o'
                      g=1
                 
                 while(qa==1):
                      
                      try:
                           m=int(input('player {} select column 1 to 9 :'.format(g)))
                      except:
                           print("Aala kaliyakkunnoo 0-9 selecteyyada koope")
                           continue
                           
                      clear()
                      for i in ze:
                           
                           if(i==m):
                               cd=1
                               break
                      
                      if (cd==1):
                           display(a,b,d,l,q)
                           print("ath edthathaalo vere number para")
                           cd=0          
                      elif(m==1 or m==4 or m==7):
                           i=1
                           qa=0
                      elif(m==2 or m==5 or m==8):
                           i=5
                           qa=0
                      elif(m==3 or m==6 or m==9):
                           i=9
                           qa=0
                      
                      else :
                           
                           continue
                      ze.append(m)
                 print(fin)
                 if(m==1 or m==2 or m==3):
                      a[i]=z
                 elif(m==4 or m==5 or m==6):
                      b[i]=z
                 elif(m==7 or m==8 or m==9):
                      d[i]=z
                 display(a,b,d,l,q)
                 fin=fin+1
                 print(fin)
                 if(a[1]==a[5]==a[9]==z or b[1]==b[5]==b[9]==z or d[1]==d[5]==d[9]==z or a[1]==b[1]==d[1]==z or a[5]==b[5]==d[5]==z or a[9]==b[9]==d[9]==z or a[1]==b[5]==d[9]==z or a[9]==b[5]==d[1]==z ):
                      if(z=='x'):
                           print("player 1 won")
                           p=input('do yo wanna paly again: y 0r n ')
                           fin=10
                      
                      else:     
                           print('player 2 won')
                           p=input('do yo wanna paly again: y or N')
                           fin=10
                 
                 elif(fin==10):
                      p=input('its a draawwww wanna playyy y or n:')

                 
                 else:
                      continue
xokalikka()

  
