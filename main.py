import info
import utilities


print(info.instruction)
while True:
    get_request = input('What do you want? - ')
    if get_request == '/register':
        while True:
            reg_login = input('Write your login - ')
            reg_password = input('Write your password - ')
            reg_password_1 = input('Write your password again - ')
            if not utilities.chek_login(reg_login):
                if reg_password == reg_password_1:
                    utilities.user_registration(reg_login, reg_password)
                    print("Registration was successful")
                    break
                else:
                    print("Invalid passwords! Try again!")
            else:
                print("This login is already exist! Try again!")

    elif get_request == '/help':
        print(info.instruction)

    elif get_request == '/end':
        print("GoodBye")
        break

    else:
        print("Write a correct request!")