'''A word game in which the user enters a sentence and the program checks whether 
the sentence is a pangram or not. An example pangram: "The quick brown fox jumps over the lazy dog." '''

def isPangram(words):
    
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
             
    chars=[".", ",", " ", "!", "?", "'", ":", ";"]
    pangram=False
    words=words.lower()
    for x in chars:
            words=words.replace(x, '')
    for x in letters:
        if x not in words:
            pangram=False
            break
        elif x in words:
            pangram=True
    if pangram==True:
        outcome='This is a pangram.'
        return outcome
    else:
        outcome="This is not a pangram."
        return outcome

phrase=input("Please enter a sentence to check if it is a pangram or not:>> ")
output=isPangram(phrase)
print(output)
