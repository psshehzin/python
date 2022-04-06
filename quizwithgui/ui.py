from tkinter import *
from question_model import Question
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class Ui():
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        question=self.quiz.next_question()
        self.window=Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=400,height=350)
        self.questiontext=self.canvas.create_text(200,175,text=f"Q.{self.quiz.question_number}: {question} (True/False): ",font=["Arial",20,"italic"],fill=THEME_COLOR,width=380)
        self.canvas.grid(row=1,column=1,columnspan=3,pady=50)
        self.score=Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,fg="White")
        self.score.grid(row=0,column=3)
        imagetrue=PhotoImage(file="./images/true.png")
        imagefalse=PhotoImage(file="./images/false.png")
        self.buttontr=Button(image=imagetrue,command=self.opttrue)
        self.buttontr.grid(row=2,column=1)
        self.buttonfals=Button(image=imagefalse,command=self.optfalse)
        self.buttonfals.grid(row=2,column=3)
        self.window.mainloop()
    def opttrue(self):
        self.quiz.check_answer("True")
        self.update()
    def optfalse(self):
        self.quiz.check_answer("False")
        self.update()
    def update(self):
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            question=self.quiz.next_question()
            self.canvas.itemconfig(self.questiontext,text=f"Q.{self.quiz.question_number}: {question} (True/False): ")
        else:
            self.canvas.itemconfig(self.questiontext,text=f"Quiz over your sore{self.quiz.score}/{self.quiz.question_number}\nDo you wanna play again")
            self.buttonfals.destroy()
            self.buttontr.destroy()
   
            


