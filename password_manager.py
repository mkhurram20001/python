from cryptography.fernet import Fernet

master_pwd = input("Enter your master password: ")

def add():
    name=input("Enter your name: ")
    pwd=input("Enter your password: ")

    with open("pwd.txt","a") as f:
        f.write(name +"|"+ pwd + "\n")
    print("Password added successfully.")
def view():
    with open("pwd.txt", "r") as f:
        for line in f.readlines():
            data=(line.strip())
            user, pswd = data.split("|")
            print(f"User: {user}, Password: {pswd}")
         

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view): ").lower()
    if mode =="add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid input. Please try again.")
        continue

