#program takes user input for a paragraph and then seperates the sentences and counts them.
import re

#user input function, strictly used to take user input and then pass it along to other functions
def usrin():

    #user input for paragraph
    sen = input('Write a paragraph: ')
    #user input return
    return sen

#pattern check function, takes an arguement and then runs it through a pattern checker to make sure it has sentences.
#then recursively counts sentences as it lists them out
def patchck(s):
    #pattern
    pat = r'[A-Z1-9].*?[.!?](?= [A-Z1-9]|$)'

    #pattern check
    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)
    #initialized counter
    count = 0

    #loop recursively checks all elements in the m pattern of the user input while also counting
    for i in m:
        count +=1
        print('->', i)

    print(count)

patchck(usrin())