# Quiz questions and answers
questions = [
    "Chandrayaan 3 is the space mission of which country? (a) India (b) China (c) Russia (d) none of the above: ",
    "Chandrayaan 3 is the successor to which previous Indian lunar mission? (a) Chandrayan1 (b) Chandrayan2 (c) Mangalyan (d) AstroSat: ",
    "Which celestial body is the primary target for Chandrayan 3? (a) mars (b) moon (c) venus (d) jupiter: "
]

answers = ["a", "b", "b"]

def run_quiz(questions, answers):
    score = 0
    for i, question in enumerate(questions):
        user_answer = input(question).lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions, answers)
