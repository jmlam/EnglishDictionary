import json
from difflib import get_close_matches as gcm
deflist = json.load(open("data.json"))

def dictionary(word):
    '''takes a word as an input and returns a list of definitions'''
    if word in deflist:
        return deflist[word]
    else:
        closest = gcm(word, deflist.keys()) # 60% cutoff
        for i in range(len(closest)):
            while True:
                yn = input('Did you mean %s ? y/n: ' % closest[i])
                if yn == 'y': #returning correct definition
                    word = closest[i]
                    return dictionary(word)
                elif yn not in 'yn' or yn == "": #checking for valid inputs
                    print('Please enter a valid input!')
                    continue
                else: #moving onto next closest when input is 'n'
                    break
        
        return ['We did not understand your query or this word does not exist. Please double check.']


definition = dictionary(input("Please enter a word: "))
[print('\n', definition.index(definition[i])+1, '. ', definition[i], '\n') for i in range(len(definition))]