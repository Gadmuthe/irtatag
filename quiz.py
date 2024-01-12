class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, answer):
        user_answer = input(f"{question} ").lower()
        if user_answer == answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    def start_quiz(self):
        print("Welcome to the Quiz Game!")
        for q, a in self.questions.items():
            self.ask_question(q, a)

        print(f"\nQuiz complete! Your score is: {self.score}/{len(self.questions)}")


quiz_questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "What is the largest mammal in the world?": "blue whale",
    "In what year was Python first released?": "1991"
}

my_quiz = Quiz(quiz_questions)
my_quiz.start_quiz()