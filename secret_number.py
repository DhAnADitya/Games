import random
number = random.randint(1,10)

print('''Welcome to Guess The Number. Please enter an integer between 1 and 10 (inclusive) to begin. Each attempt 
         generates a clue if the entered number is too low or too high. Exit the game at any time by pressing Enter.''')

attempts = 0
while True:
    guess = input('Please enter a number: ')
    attempts+=1
    stop = guess
    try:
        if stop == '':
            print('You quit the game. Thank you for playing!')
            break
        elif int(guess) == number:
            print('Correct! The secret number was', number)
            print('The number of attempts was', attempts)
            break
        elif int(guess) != number and int(guess) < number:
            print('Incorrect.')
            print('Your guess is too low.')
        elif int(guess) != number and int(guess) > number:
            print('Incorrect.')
            print('Your guess is too high.')
    except ValueError:
        print('Invalid input. Please ensure your guess is an integer.')
