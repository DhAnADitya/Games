'''A word game in which the user enters a word or sentence and the program checks whether 
it is a palindrome or not. An example palindrome is "Amore, Roma." '''

def isPalindrome(phrase): 
    chars=[".", ",", "'", "?", "!", " ", ":", ";"]
    phrase=phrase.lower()
    for x in chars:
        phrase=phrase.replace(x, '')
    phrase_list=list(phrase)
    phrase_list.reverse()
    rev=''.join(phrase_list)
    if phrase==rev:
        output="This is a palindrome."
        return output
    else:
        output="This is not a palindrome."
        return output

phrase=input("Please enter a word or phrase to check if it is a palindrome or not:>> ")
outcome=isPalindrome(phrase)
print(outcome)
