from question_model import Question
from data import question_data
from random import randint
from quiz_brain import Brain

class QuestionGame:
    def __init__(self):
        self.brain = Brain()
        self.questions = question_data
        self.indexed = []
        self.is_on = True

    def Game(self):
        question_number = 1
        self.is_on = True
        while self.is_on:
            question = self.next_question()
            print(f"TRUE or FALSE! Q.{question_number}: {question['text']}")
            self.brain.Answer(question)
            question_number+=1
            print(f"Your score is: {self.brain.score}/{len(self.questions)} The hi-score is {self.brain.hi_score}")
            if len(self.indexed) >= len(self.questions):
                again = input("Play again? Y or N: ").lower()
                if again == "y":
                    if self.brain.score > self.brain.hi_score:
                        print(f"Your score of {self.brain.score} has set the hi-score!")
                        self.brain.hi_score = self.brain.score
                    self.indexed = []
                    self.brain.score = 0
                    continue
                else:
                    if self.brain.score > self.brain.hi_score:
                        self.brain.hi_score = self.brain.score
                    self.is_on = False
                    print("\n Thanks for playing!")
                    self.indexed = []
                    self.brain.score = 0
                    continue

    def next_question(self):
        index = randint(0, len(self.questions) - 1)
        while index in self.indexed:
            index = randint(0, len(self.questions) - 1)
        self.indexed.append(index)
        return self.questions[index]






questioner = QuestionGame()
# def all_questions():
#     for question in question_data:
#         print(f"Question: {question['text']} Answer: {question['answer']}")
# print(questioner.questions)

questioner.Game()

# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def report(self):
#         print(f"User: {self.name} | ID: {self.id}")
#
#
#
# user_1 = User("001", "Jake")
# user_1.report()
# print(user_1.id)
