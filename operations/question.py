def askQuestion(problem_generator, scale):
    generator = problem_generator(scale)
    answer, sentence = generator.create_problem()
    ops = {"+": "Add", "-": "Subtract", "*": "Multiply", "/": "Divide"}

    if isinstance(answer, str):
        q_type = ops.get(answer)
        print(sentence)
        guess = str(input())
        return guess == q_type
    else:
        print(sentence)
        guess = float(input())
        return guess == answer


def quiz(chances=3):
    score = 0
    chances = 3
    print(f"Welcome. Good luck, you have {chances} chances!\n")
    while chances > 0:
        correct = askQuestion(add_problem, 1)
        if correct:
            score += 1
            print("Correct!\n")
        else:
            chances -= 1
            if chances > 0:
                print(f"Incorrect, you have {chances} chances left.")
            else:
                print(f"Sorry, Game Over!")
    return print(f"Your score was {score}.")
