#This code creates a list of common spam phrases and then takes user input for an email.
#It then checks the user input for spam phrases defined in the created list, and then
#outputs: the number of phrases found, which phrases were found, the spam score of the email
#and the probability that the email is spam.

def aidstest():

    #initial list of spam test phrases
    spam_words = [
        "free",
        "winner",
        "congratulations",
        "click here",
        "limited time",
        "avoid bankruptcy",
        "be your own boss",
        "big bucks",
        "you are a winner",
        "act now",
        "cures baldness",
        "eliminate bad credit",
        "fast viagra delivery",
        "cents on the dollar",
        "earn extra cash",
        "earn money",
        "fast cash",
        "free investment",
        "free trial",
        "get paid",
        "increase sales",
        "make money",
        "money back",
        "potential earnings",
        "prize",
        "risk-free",
        "satisfaction guaranteed",
        "special promotion",
        "become a member",
        "click here",
        "exclusive deal",
    ]

    #takes user input
    message = input("Enter an email message: ")

    #converts email into all lower case
    message_lower = message.lower()

    #spam words and spam score accumulators
    spam_score = 0
    words_found = []

    #spam word check
    for word in spam_words:
        if word.lower() in message_lower:
            spam_score += 1
            words_found.append(word)

    #return values for function
    return spam_score, words_found



def testoutput(spam_score, words_found):
    #checks spam score and prints appropriate output
    if spam_score == 0:
        chance = "Safe."
    elif spam_score <= 2:
        chance = "Probably spam."
    else:
        chance = "Computer aids."

    #prints test result
    print("Spam score:", spam_score)
    print("chance:", chance)

    if len(words_found) > 0:
        print("Words/phrases that triggered the spam score:")
        for word in words_found:
            print(word)
    else:
        print("No spam words or phrases were found.")


testoutput(*aidstest())