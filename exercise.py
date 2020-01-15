import mysql.connector
#establish connection
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cursor = con.cursor()# create cursor
#Dictionary contins the columns 'Expression' and 'Definition'
query = cursor.execute("SELECT * FROM Dictionary WHERE expression = 'inlay'") #execute query at database
results = cursor.fetchall() #fetch results

print(results)