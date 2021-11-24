class QuizBrain:
    def __init__(self,qbank):
        self.qno=0
        self.questions=qbank
        self.score=0
    def nextq(self):
        currentquestion=self.questions[self.qno]
        self.qno+=1
        answer=input(f"Q{self.qno}: {currentquestion.text} (True/False): ")
        self.check_answer(answer,currentquestion.ans)
    def check_answer(self, answer,correctans):
        if answer==correctans:
            self.score=self.score+1
            print(f"correct answer score is {self.score}/{self.qno}")
        else:
           print(f"wrong answer score is {self.score}/{self.qno}")
        print(f" correct ans was {correctans}")
        print("\n")
    def stillhasq(self,len):
        if self.qno<len:
            return True
        else: 
            return False