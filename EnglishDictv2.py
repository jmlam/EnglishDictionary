import json
from difflib import get_close_matches as gcm
deflist = json.load(open("data.json"))

def dictionary(word):
    '''takes a word as an input and looks up the definition in a definition list'''
    if word in deflist:
        return deflist[word]
    else:
        closest = gcm(word, deflist.keys()) # 60% cutoff
        for i in range(len(closest)):
            yn = input('Did you mean %s ? y/n: ' % closest[i])
            if yn == 'y':
                word = closest[i]
                return dictionary(word)
        
        return 'This word does not exist. Please double check.'


definition = dictionary(input("Please enter a word: "))
[print('\n', definition.index(definition[i])+1, '. ', definition[i], '\n') for i in range(len(definition))]