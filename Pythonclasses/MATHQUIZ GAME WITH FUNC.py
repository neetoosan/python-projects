import random
# declear my question function
def generateQuestion():
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    cal_Operation = random.choice(['+', '-', '*']) # pick random operation to work with
    if cal_Operation == '+':
        ans = num1 + num2
    elif cal_Operation == "-":
        ans = num1 - num2
    else:
        ans = num1*num2
    return num1, num2, cal_Operation, ans # to store all the values
# create a function to ask questions

def askQuestions():
    num1,num2, cal_Operation, correctAns = generateQuestion() # using the stored values here
    userAns = input(f'what is {num1} {cal_Operation} {num2} ?: ')
    try: # using this to prevent erros of input when i input strings instead of a number
        userAns = int(userAns)
        return userAns == correctAns
    except ValueError:
        print('Invalid input! please enter a number')
        return False
# rounds and score section in the quiz game
def mathQuiz():# main function for the game
    score = 0
    rounds = 10 # how many times it gonna ask questions
    print('\n-- Welcome to the Math Quiz game ---\n')
    for i in range(rounds):
        if askQuestions():
            print("correct!!\n")
            score += 1
        else:
            print("Wrong answer\n")
    print(f'Quiz is over! final score is {score} / {rounds}')
mathQuiz()


