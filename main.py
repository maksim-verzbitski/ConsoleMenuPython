import keyboard
actions_menu = {
    1: 'List all users - 1',
    2: 'Edit user/s - 2',
    3: 'Add  new user - 3',
    4: "Average(Medium) user's age - 4",
    5: "Delete user - 5",
    6: "Exit - 6"
}
def average_age(db):
    sum=0
    for i in range(0, len(db)):
        row= db[i]
        sum = sum + int(row[2])
        print(i, row[2])
    print(sum/i)

def deleting_user(db):
    print('Deliting user')
    print_out_database(db)
    delete_user = int(input("What user you want to delete user's index number: "))
    del db[delete_user]
    write_database(db)

def strip(string):
    return string.strip()

def read_database():
    file = open("C:/Users/akell/Desktop/Tick-tac-toe/contacts.txt",  encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

def write_database(db):
    file = open("C:/Users/akell/Desktop/Tick-tac-toe/contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db:
        rows.append(", ".join(row))
    file.write("\n".join(rows),)
    file.close()

def print_out_menu_options():
    for i in actions_menu:
        print(actions_menu[i])

def print_out_database(db):
    print("Index \t Name \t\t\t Phone \t\t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

def listing_users(db):
    print('Listing  users...')
    db = read_database()
    # i Have fixed None issue
    print_out_database(db)

def editing_users(db):
    print('Editing users...')
    # index name Phone Age Email
    db = read_database()
    listing_users(db)
    index_inpt = int(input("Enter which user' index(exp: 1,2,3...) you would like to improve: "))
    if index_inpt == 0:
        print(db[index_inpt])
        #print(i, "\t\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")
    elif index_inpt == 1:
        print(db[index_inpt])
    elif index_inpt == 2:
        print(db[index_inpt])
    #elif index_inpt == len(db[index_inpt-1]):
        #print(db[index_inpt-1])
    else:
        print("User's List is Out of range")

    inpt = input("What field you would like to change: ")

    if inpt.lower() == "Name":
        add_name = input("Enter your desired name: ")
        # db.write(db[0][0].replace())
        db[index_inpt][0] = add_name

        print(db[index_inpt][0])

    elif inpt == "Phone":
        add_number = input("Enter mobile number using only numbers and '+': ")
        db[index_inpt][1] = add_number
        print(db[index_inpt][1])
    elif inpt == "Age":
        add_age = input("Enter numeric value: ")
        db[index_inpt][2] = add_age
        print(db[index_inpt][2])
    elif inpt.lower == "Email" or input.lower() == "@":
        add_email = input("Enter email using letters numbers and @: ")
        db[index_inpt][3] = add_email
        print(db[index_inpt][3])
    else:
        print("Wrong input: => Try {Name, Phone, Age, Email}")
        editing_users(db)

    write_database(db)


def adding_user(db):
    print('Adding users...')
    db = read_database()
    add_name = input("Add name:")
    if add_name.isnumeric():
        print("Only string are allowed!")
        return
    add_number = input("Add Phone number:")
    if add_number.isalpha():
        print("Only string are allowed!")
        return
    add_age = input("Add Age:")
    if add_age.isalpha():
        print("Only string are allowed!")
        return
    add_email = input("Add Email:")

    db.append([add_name, add_number, add_age, add_email])
    write_database(db)

# Press the green button in the gutter to run the script.
# As im using Pycharm here is main method
if __name__ == '__main__':
    print("Welcome to main method"+"\nPress space to continue")
    while True:
        db = read_database()
        try:
            if keyboard.is_pressed('space'):
                print('*******************************')
                print_out_menu_options()
                print('*******************************')
                operation = int(input("Enter option you would like to choose:"))
                if operation == 1:
                    #print("Listing your users...")
                    listing_users(db)
                    print("Press space")
                elif operation == 2:

                    editing_users(db)
                    print("Press space")
                elif operation == 3:
                    print("Adding new user to your contacts.txt...")
                    adding_user(db)
                    print("Press space")
                elif operation == 4:
                    print("Calculating average user's age...")
                    average_age(db)
                    print("Press space")
                elif operation == 5:
                    print("Deliting excisting user...")
                    deleting_user(db)
                    print("Press space")
                elif operation == 6:
                    print("Exiting....")
                    break
                    exit()
                else:
                    print("Invalid action. Try(1,2,3,4,5")
        except:
            print("you have entered incorrect information")
            print("Press space")

def main():
    db=read_database()
    #print_out_database(db)
    #print_out_menu_options()

main()


