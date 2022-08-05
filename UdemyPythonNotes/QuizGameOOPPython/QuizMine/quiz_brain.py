class Brain:
    def __init__(self):
         self.score = 0
         self.hi_score = 0

    def Answer(self, question):
        answer = input("Answer: ").lower()
        while answer != "t" and answer != "f":
            answer = input("Wrong input try typing T or F: ").lower()

        if answer == "t":
            answer = "True"
        elif answer == "f":
            answer = "False"
        if answer == question['answer']:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
