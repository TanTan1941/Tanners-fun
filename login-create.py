import bcrypt

FilePath = "userpass.csv"
StrUser = input("Please enter your username \n")
StrPass = input("Please enter your password \n")
StrPassHash = bcrypt.hashpw(StrPass.encode('utf-8'), bcrypt.gensalt())
DecHash = StrPassHash.decode('utf-8')

with open(FilePath, "a") as file:
    file.write(f"{StrUser},{DecHash}\n")
