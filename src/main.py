import random
import requests
import sqlite3
## Imports ## 

def generate_username():
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain" ## great website :)

    raw_names = requests.get(url).text #-> gets the text(names) from the webiste. returns a string with names
    names = raw_names.split() # ---------> splits the string into different names. returns a list

    username = random.choice(names) + str(random.randint(1, 999)) ## finds a username from the list generated above
    return username


def insert_username(username):
    ## db config ######
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usernames (username TEXT)")
    #########################

    cursor.execute('SELECT * FROM usernames WHERE username=?', (username, )) # --> finds the username
    if cursor.fetchall() == []:
        cursor.execute("INSERT INTO usernames(username) VALUES (?)", (username, )) # --> inserts username if not exists. returns True if added in database.
        conn.commit()
        return True
    else:
        return False # --> returns false if username was found in the database. repitition detection :)



# username = generate_username()
# print(insert_username(username))

