import json
import difflib as dl
dictionary = json.load(open("data.json"))

#find key was borrowed from a different project and works quite well in this situation. It does not return an error but an empty list if the input is not in the dictionary
def find_key(target_key, collection):
    '''Searches for all instances in the nested dictionary where a key matches the target key and returns a list of values with matching keys'''
    result_list = []
    if isinstance(collection, list):
        for item in collection:
            result_list += find_key(target_key, item)
    elif isinstance(collection, dict):
        for key, value in collection.items():
            if key == target_key:
                result_list += [value]
            else:
                result_list += find_key(target_key, value)
    return result_list

while True:
    word = str(input('Please enter word a word to use the dictionary. \nIf you would like to stop please type "\end". \nEnter word: '))
    if word == '\end':
        #this allows the user to end the program.
        break
    else:
        word = word.lower() #removes any non-capital letters
        while word not in dictionary: #check if misspelled.
            closest = dl.get_close_matches(word, dictionary.keys(), n = 3)
            if closest == []:
                break
            else:
                for i in range(len(closest)):
                    print('Did you mean', closest[i], '?')
                    answer = input('y/n? ')
                    if answer == 'y':
                        word = closest[i]
                        break
                break
        if word not in dictionary: #if not mispelled then restart
            print('\nThe word does not exist or is not in this dictionary. Please try again.\n')
            continue
        
        definition = find_key(word, dictionary)
        definition = definition[0] #find_key always returns a list of items    
        for i in range(len(definition)):
            print('\n', definition.index(definition[i])+1, '. ', definition[i], '\n')