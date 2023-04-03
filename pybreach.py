import sys
import os

USERS_FILE = "users.txt"

def get_user(username):
    with open(USERS_FILE, "r") as f:
        for line in f:
            fields = line.strip().split(":")
            if fields[0] == username:
                return {"username": fields[0], "password": fields[1], "privilege": int(fields[2])}
    return None

def list_accounts():
    with open(USERS_FILE, "r") as f:
        print("Username  Privilege")
        print("--------------------")
        for line in f:
            fields = line.strip().split(":")
            print(f"{fields[0]:8}  {fields[2]:9}")
    print()

def execute_command():
    os.system(input("Enter command to execute: "))

def push_script():
    filename = input("Enter script filename: ")
    with open(filename, "r") as f:
        script = f.read()
    with open("script.py", "w") as f:
        f.write(script)
    print("Script saved as script.py")

def run_script():
    os.system("python script.py")

def create_account():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    privilege = input("Enter privilege level (1-3): ")
    with open(USERS_FILE, "a") as f:
        f.write(f"\n{username}:{password}:{privilege}")

def main():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write("admin:admin:3")

    username = input("Username: ")
    password = input("Password: ")

    user = get_user(username)

    if not user or user["password"] != password:
        print("Invalid username or password.")
        sys.exit(1)

    privilege = user["privilege"]

    if privilege == 3:
        while True:
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                create_account()
            elif choice == '2':
                list_accounts()
            elif choice == '3':
                execute_command()
            elif choice == '4':
                push_script()
            elif choice == '5':
                run_script()
            else:
                print("Invalid choice.")

    elif privilege == 2:
        while True:
            choice = input("Enter your choice (2-5): ")
            if choice == '2':
                list_accounts()
            elif choice == '3':
                execute_command()
            elif choice == '4':
                push_script()
            elif choice == '5':
                run_script()
            else:
                print("Invalid choice.")

    elif privilege == 1:
        while True:
            choice = input("Enter your choice (1, 2, 5): ")
            if choice == '1':
                create_account()
            elif choice == '2':
                list_accounts()
            elif choice == '5':
                run_script()
            else:
                print("Invalid choice.")

    else:
        print("Error: Invalid privilege level.")
        sys.exit(1)

if __name__ == "__main__":
    main()
