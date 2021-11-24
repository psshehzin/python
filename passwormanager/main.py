from tkinter import *
#the above lines only import calsses and constatns below is kind of a module
from tkinter import messagebox
import random
import pyperclip
import json
UPPERCASESNO=3
LOWERCASENO=6
DIGITNO=4
SPECIALCHARNO=2
# Get creds
def get_credentials():
    web=entry_website.get()
    try:
        with open("password.json",mode='r') as datajson:
            data=json.load(datajson)
    except FileNotFoundError:
        messagebox.askokcancel(message=f"The entry for {web} not found please add an entry or check the spelling ")
    else:
        try: 
            credpwd=data[web]["password"]
            credmail=data[web]["email"]
            entry_password.delete(0,END)
            entry_password.insert(0,credpwd)
            entry_mail.delete(0,END)
            entry_mail.insert(0,credmail)
        except KeyError:
            messagebox.askokcancel(message=f"The entry for {web} not found please add an entry or check the spelling ")

    
        
              

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    upper=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    upper.insert(0,UPPERCASESNO)
    lower=[chr(i) for i in range(ord('a'),ord('z')+1)]
    lower.insert(0,LOWERCASENO)
    spchar=["!","@","#"]
    spchar.insert(0,SPECIALCHARNO)
    digit=[str(i) for i in range(0,10)]
    digit.insert(0,DIGITNO)
    opt=[upper,lower,digit,spchar]
    password=""
    for i in range(0,11):
        optselected=random.choice(opt)
        while(optselected[0]==0):
            optselected=random.choice(opt)
        optselected[0]-=1
        char=random.choice(optselected[1:])
        password+=char
    pyperclip.copy(password)
    entry_password.delete(0,END)
    entry_password.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_details():
#    global entry_mail,entry_password,entry_website
    email=entry_mail.get()
    website=entry_website.get()
    password=entry_password.get()
    if website=="" or password=="" or email=="":
        messagebox.showinfo(message="one or more fields are empty add value and retry")
    else:
        updateyn=messagebox.askyesno(title="update details",message=f"Hi do you want to update the following details \n website: {website}\n email: {email}\n password: {password}")
        if updateyn:
            newdata={website: {
                "email": email,
                "password": password
            }}
            try:
                with open("password.json",mode='r') as datafile:
                    data=json.load(datafile)
            except FileNotFoundError:
                with open("password.json",mode='w') as datafile:
                    json.dump(newdata,datafile,indent=4)
            else:
                data.update(newdata)
                with open("password.json",mode='w') as datafile:
                    json.dump(data,datafile,indent=4)
            finally:
                entry_website.delete(0,END)
                entry_password.delete(0,END)
        

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("password Manager")
window.config(padx=40,pady=40)
logo=PhotoImage(file="logo.png")
canvas=Canvas(height=200,width=200)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=0,rowspan=3,columnspan=3)
label_website=Label(text="website",font=("arial",8,"bold"))
label_website.grid(row=3,column=0)
entry_website=Entry(width=22)
entry_website.grid(row=3,column=1)
#to place cursor inside the box
entry_website.focus()
label_email=Label(text="Email",font=("arial",8,"bold"))
label_email.grid(row=4,column=0)
entry_mail=Entry(width=36)
entry_mail.grid(row=4,column=1,columnspan=2)
entry_mail.insert(0,"shehzinps@gmail.com")
label_password=Label(text="Password",font=("arial",8,"bold"))
label_password.grid(row=5,column=0)
entry_password=Entry(width=22)
entry_password.grid(row=5,column=1)
button_genpassword=Button(text="Gen Passwd",width=12,font=("arial",8,"bold"),command=gen_password)
button_genpassword.grid(row=5,column=2)
button_update=Button(text="Add",width=31,font=("arial",8,"bold"),command=update_details)
button_update.grid(row=6,column=1,columnspan=2)
button_get=Button(text="search",width=12,font=("arial",8,"bold"),command=get_credentials)
button_get.grid(row=3,column=2)
window.mainloop()
