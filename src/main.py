import random
import requests
import sqlite3
## Imports ## 

def generate_username():
    with open(r'names.txt') as names:
        names = names.read().replace('\n', ' ')
        names = names.split(' ')
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


if __name__ == "__main__":
    username = generate_username()
    print(username)
    print(insert_username(username))
