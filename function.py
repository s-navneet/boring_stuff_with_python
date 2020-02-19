import random
def getAnswer(r):
    if(r == 1):
        return 'it is certain'
    elif(r == 2):
        return 'it is decidly so'
    elif(r == 3):
        return 'yes'
    elif(r == 4):
        return 'reply hazy try again'
    elif(r == 5):
        return 'ask again later'
    elif(r == 6):
        return 'concrete and ask again'
    elif(r == 7):
        return 'my rply is no'
    elif(r == 8):
        return 'outlook is not so good'
    elif(r == 9):
        return 'very doubtfull'


fortune = getAnswer(random.randint(1,9))
print(fortune)
