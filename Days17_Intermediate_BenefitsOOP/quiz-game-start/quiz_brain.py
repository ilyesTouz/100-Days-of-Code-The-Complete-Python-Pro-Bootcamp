# TODO : asking the questions
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz

class QuizBrain:
    # Initialize attributes
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Go to the next question quiz
    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("Q{}: {} (True/False)?:".format(self.question_number,current_question.text))
        self.check_answer(user_answer, current_question.answer)
    
    # Still has question 
    def still_has_question(self) -> bool:
        return self.question_number < len(self.question_list)
    
    # Check the answer
    def check_answer(self, user_answer, correct_answer) -> None:
        if user_answer.lower() == correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print('You got it wrong')
        print('The correct answer was: {}'.format(correct_answer))
        print('The current Score is {}/{}'.format(self.score, self.question_number))
        print('\n')
        



