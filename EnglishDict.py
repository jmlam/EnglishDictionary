import json

dictionary = json.load(open("data.json"))
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
    word = str(input('Enter word: '))
    if word != '/end':
        definition = find_key(word, dictionary)
        print(definition)
    else:
        break