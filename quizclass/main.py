from question_model import Question
from data import question_data,results
from quiz_brain import QuizBrain
questionobjects=[]
for i in results:
    questionobjects.append(Question(i["question"],i["correct_answer"]))
quiz=QuizBrain(questionobjects)
tques=len(questionobjects)
stillhasq=True
while(stillhasq):
    quiz.nextq()
    stillhasq=quiz.stillhasq(tques)

print(f"quiz has ended your score {quiz.score}/{tques}")