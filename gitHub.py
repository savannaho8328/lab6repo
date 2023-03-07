def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    n_password = ""
    for num in password:
        num = int(num)
        n_password += str(num + 3)
    return n_password




if __name__ == "__main__":
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored")
        elif option == 2:
            decode(n_password)
            print("The encoded password is", n_password, ", and the original password is", decode(n_password))
        else:
            break