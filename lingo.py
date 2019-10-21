import random

secret_list = ['benin', 'egypt', 'gabon', 'ghana', 'kenya', 'libya', 'niger', 'sudan', 'chile', 
               'china', 'haiti', 'india', 'italy', 'japan', 'malta', 'nauru', 'nepal', 'palau', 
               'qatar', 'samoa', 'spain', 'syria', 'tonga', 'yemen']

secret = random.choice(secret_list)


def fullMatch(guess, position):
    if guess[position] == secret[position]:
        return True
    
def partialMatch(guess, position):
    if guess[position] != secret[position]:
        return True

def checkInput(guess):
    hint = 'Clue: '
    for n in range(0, 5):
        if guess[n] in secret:
            if fullMatch(guess, n) == True:
                hint = hint + '[' + guess[n] + ']'
            elif partialMatch(guess, n) == True:
                hint = hint + '(' + guess[n] + ')'
        else:
            hint += guess[n]
    return hint

print('''
      Welcome to Lingo! Your task is to guess the secret name of a country consisting of exactly five characters. 
      Each attempt generates a clue with respect to the matched characters. Characters found in the secret name but 
      at incorrect positions are marked with round parentheses. Characters fully matched at correct positions are 
      marked with square brackets. E.g., the following clue would be given for the secret country 'italy':
      
      Input: spain
      Clue: sp[a](i)n
      
      To exit the game, press Enter at any time.''')

while True:
    guess = input('Please enter the name of a country consisting of 5 characters: ').lower()
    try:
        if guess == '':
            print('You quit the game. Thank you for playing Lingo!')
            break
        elif checkInput(guess).count('[') == 5:
            print('Correct, the secret country was ' + secret + '. Thank you for playing Lingo!')
            retry = input('Would you like to play again (y/n)?')
            if retry == 'y':
                secret = random.choice(secret_list)
            elif retry == 'n':
                break
        else:
            print(checkInput(guess))
    except IndexError:
        print('Please ensure your guess consists of exactly 5 characters.')