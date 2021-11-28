from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
#hex color value
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK="#000000"
WHITE="#FFFFFF"
FONT_NAME = "Courier"
TICK="✓"
text2=""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=NONE
REP=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global text2,timer,REP
    text2=""
    window.after_cancel(timer)
    REP=0
    label.config(text=" TIMER   ",fg=PINK)
    label2.config(text=text2)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REP
    global text2
    if REP in range(0,8,2):
        label2.config(text=text2)
        label.config(text=" Work Time",fg=GREEN)
        count_down(WORK_MIN*60)
    elif REP in range(1,8,2):
        text2=text2+TICK
        label2.config(text=text2)
        label.config(text="Break Time",fg=BLACK)
        count_down(SHORT_BREAK_MIN*60)
        
    else:
        label.config(text="Break Time",fg=BLACK)
        text2=""
        count_down(LONG_BREAK_MIN*60)
        
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REP
    global timer
    min=0
    sec=0
    if count>=0:
        min=count//60
        sec=count%60
        if min in range(0,10):
            min="0"+str(min)
        if sec in range(0,10):
            sec="0"+str(sec)
        canvas.itemconfig(canvastext,text=f"{min}:{sec}")
        timer=window.after(1000,count_down,count-1)
    else:
        if REP!=7:
            REP=REP+1
        else:
            reset_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
label=Label(text="Timer",fg=BLACK,font=(FONT_NAME,30,"bold"),bg=YELLOW)
label.grid(row=1,column=2)
#got width and height from pixel size
tomatoimage=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomatoimage)
canvastext=canvas.create_text(102,135,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=2,column=2)
button1=Button(text="start",bg=WHITE,font=(FONT_NAME,10,"bold"),highlightthickness=0,command=start_timer)
button1.grid(row=3,column=1)
button2=Button(text="reset",bg=WHITE,font=(FONT_NAME,10,"bold"),highlightthickness=0,command=reset_timer)
button2.grid(row=3,column=3)
label2=Label(text=text2,fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
label2.grid(row=4,column=2)
window.mainloop()