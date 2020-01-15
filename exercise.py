import mysql.connector
#establish connection
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

#Testing multiple queries
while True:
    word = str(input('Enter word: '))
    if word == '/end':
        break
    else:
        cursor = con.cursor()# create cursor
        #Dictionary contins the columns 'Expression' and 'Definition'
        query = cursor.execute("SELECT definition FROM Dictionary WHERE expression = '%s'" % word)  #execute query at database. return definition of word
        results = cursor.fetchall() #fetch results
        if results:
            for result in results:
                print(result[0])
        else:
            print('There is no word! Please double check.')