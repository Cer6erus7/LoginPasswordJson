import info
import utilities


print(info.instruction)
point = True
while point:
    print("\nYou are in main menu!")
    get_request = input('What do you want? - ')

    if get_request == '/register':
        while True:
            reg_login = input('Write your login - ')
            if reg_login == '/return':
                break
            reg_password = input('Write your password - ')
            if reg_password == '/return':
                break
            reg_password_1 = input('Write your password again - ')
            if reg_password_1 == '/return':
                break

            if not utilities.chek_login(reg_login):
                if reg_password == reg_password_1:
                    utilities.user_registration(reg_login, reg_password)
                    print("Registration was successful")
                    break
                else:
                    print("Invalid passwords! Try again!")
            else:
                print("This login is already exist! Try again!")

    elif get_request == "/login":
        while True:
            log_login = input("Write login - ")
            if log_login == '/return':
                break
            log_password = input("Write password - ")
            if log_password == '/return':
                break

            if utilities.check_log_pass(log_login, log_password):
                print("You are successfully logged in!")
                point = False
                break
            else:
                print("Something is wrong! Try again!")

    elif get_request == '/help':
        print(info.instruction)

    elif get_request == '/return':
        print('You are in main menu, you cannot return back!')

    elif get_request == '/end':
        print("GoodBye!")
        break

    else:
        print("Write a correct request!")