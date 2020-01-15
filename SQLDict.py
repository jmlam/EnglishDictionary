import mysql.connector
import re
from difflib import get_close_matches as gcm
#establish connection
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
#Dictionary contins the columns 'Expression' and 'Definition'
cursor = con.cursor()# create cursor
cursor.execute('SELECT expression FROM Dictionary')
expresslist = cursor.fetchall()
expresslist = [express[0] for express in expresslist] 

def sqldict(word):
    stripped = re.sub(r'\W+', "", word)
    wordtypes = [word, word.lower(), word.title(), word.upper(), stripped]
    for word in wordtypes:
        cursor.execute("SELECT * FROM Dictionary WHERE expression = '%s'" % word)  #execute query at database. return definition of word
        results = cursor.fetchall() #fetch results
        if results:
            return results
        
    #finding closest match
       
    for word in wordtypes: #find closest match                
        closest = gcm(word, expresslist, cutoff=.8) # attempting 3 words that seem similar at a 80% similarity. User checked.
        for i in range(len(closest)):
            while True:
                yn = input('Did you mean %s? y/n: ' % closest[i])
                if yn == 'y': #returning correct definition
                    word = closest[i]
                    return sqldict(word)
                elif yn not in 'yn' or yn == "": #checking for valid inputs
                    print('Please enter a valid input!')
                    continue
                else: #moving onto next closest when input is 'n'
                    break
    print('We did not understand your query or this word does not exist. Please double check.')
    return ""

word = str(input('Enter word: '))
definitions = (sqldict(word))
for definition in definitions:
    print(definition[1])

