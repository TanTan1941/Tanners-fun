import csv
import bcrypt
from getpass import getpass

def chkcred(struser, strpass):
    with open("userpass.csv", 'r') as file:

        reader = csv.reader(file)

        for row in reader:
            if len(row) != 2:
                continue
            stored_user, stored_hash = row
            if stored_user == struser:
                if bcrypt.checkpw(strpass.encode('utf-8'), stored_hash.encode('utf-8')):
                    return True

                else:
                    return False

    return False

username = input("please input your Username \n")

password = getpass("Please input your Password \n")

if chkcred(username, password):
    print(f"Logins match {username} \n")

else:
    print(f"Invald username or password {username}")
