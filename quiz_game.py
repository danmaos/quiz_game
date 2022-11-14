questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():
    question_num = 1
    guesses = []
    correct_answers = 0

    for key in questions.keys():
        print(key)
        print('_______________')
        for el in options[question_num - 1]:
            print(el)
        print('_______________')
        while True:
            guess = input("Please enter answer (A, B, C, D): ").upper()
            if guess not in questions.values():
                print('Try again')
                print('_______________')
            else:
                break
        guesses.append(guess)
        correct_answers += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_answers, len(guesses))


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(correct_ans, guesses):
    total = (correct_ans / guesses) * 100
    print("Your total score is", total, "%")


def play_again():
    while True:
        response = input("Do you want to play again? (yes or no): ").upper()
        if response not in ["YES", 'NO']:
            print("Enter only Yes or No")
        else:
            break
    if response == "YES":
        return True
    elif response == "NO":
        return False

new_game()


def main():
    while play_again():
        new_game()
    print("Bye bye")

main()
