import random

def quiz_game():
    questions = [
        ("What is the capital of India?", "Delhi"),
        ("What is 70 + 30?", "100"),
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
        ("What is the square root of 64?", "8"),
        ("Which country is known as the Land of the Rising Sun?", "Japan"),
        ("What is the tallest mountain in the world?", "Mount Everest"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the currency of the United Kingdom?", "Pound Sterling")
    ]

    while True:
        random.shuffle(questions)

        while True:
            try:
                num_questions = int(input(f"How many questions would you like to answer (1-{len(questions)})? "))
                if 1 <= num_questions <= len(questions):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(questions)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        selected_questions = questions[:num_questions]

        score = 0
        for question, answer in selected_questions:
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Wrong!!")

        percentage = (score / num_questions) * 100
        print(f"\nYour final score is: {score} out of {num_questions}!")
        print(f"You got {percentage:.2f}% of the questions correct!\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

quiz_game()
