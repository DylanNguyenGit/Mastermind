import random


def game():
    answer=[random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    print("Welcome to Mastermind!")
    for x in range(15):
        print("please enter a guess:")
        while True:
            try:
                guess = int(input())
                if guess > 9999 or guess < 0:
                    print("Your guess has to be a 4 digit positive number...")
                    print("or any number smaller than 1000 because of how I coded it")
                else:
                    break
            except:
                print("Your guess has to be a 4 digit positive number...")
                print("or any number smaller than 1000 because of how I coded it")
        hint = check(answer, guess)
        if(hint == "2222"):
            print("Your guess " + str(guess) + " was correct! Congratulations!")
            break
        elif x == 14:
            print("You lost! Haha! Noob!")
            print("The answer was: " + str(answer[0])+str(answer[1])+str(answer[2])+str(answer[3]) + " all along!")
        else:
            print("Here is your hint: " + hint)

def check(ans, gue):
    result=""
    checked = [0, 0, 0, 0]
    gue2 = gue
    for y in range(4):
        digit = gue2 % 10
        gue2 //= 10
        if digit == ans[3-y]:
            checked[3-y] = 2
            result = "2" + result
    gue2 = gue
    result = result + check_more(gue2, checked, ans, 3)
    gue2 //= 10
    result = result + check_more(gue2, checked, ans, 2)
    gue2 //= 10
    result = result + check_more(gue2, checked, ans, 1)
    gue2 //= 10
    result = result + check_more(gue2, checked, ans, 0)
    return result


def check_more(guess, checked, answer, num):
    if checked[num] != 2:
        digit = guess % 10
        cont = True
        index = 0
        while cont and index < 4:
            if checked[index] == 0 and answer[index] == digit:
                checked[index] = 1
                return "1"
                cont = False
            else:
                index += 1
    return ""


play = "play again"
while play.lower() == "play again":
    game()
    print("Thank you for playing! Enter 'play again' to play again or anything else otherwise.")
    play = input()
print("Bye Bye!")
