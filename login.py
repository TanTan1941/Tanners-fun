import bcrypt

FilePath = "userpass.csv"


StrUser = input("Please enter your username \n")

StrPass = input("Please enter your password \n")
StrPassHash = bcrypt.hashpw(StrPass.encode('utf-8'), bcrypt.gensalt())

with open(FilePath, "a") as file:
    file.write(f"User:{StrUser} \t Pass:{StrPassHash} \n")