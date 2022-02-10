from question_model import Question
from data import question_data_trivia
from quiz_brain import QuizBrain

# Create a question bank that contains all the question's objects
question_bank = [
    Question(question["question"], question["correct_answer"]) for question in question_data_trivia['results']
]

# Initialize quizz
quiz = QuizBrain(question_bank)

# Show questions
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print('Quiz Finished')
print('\n')
print('Your final score is {}/{}'.format(quiz.score, quiz.question_number))
