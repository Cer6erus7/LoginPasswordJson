import info
import utilities
from pprint import pprint


print(info.instruction)
global_point = True
menu_point = True
while global_point:
    profile_login = None

    while menu_point:
        print("\nYou are in main menu!\n")
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
                        print("\nRegistration was successful")
                        menu_point = False
                        profile_login = reg_login
                        print(info.logged_instruction)
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

                if utilities.check_log_pass(log_login, log_password) == 'success':
                    print("\nYou are successfully logged in!")
                    print(info.logged_instruction)
                    menu_point = False
                    profile_login = log_login
                    break
                elif utilities.check_log_pass(log_login, log_password) == 'deleted':
                    print("This profile has been deleted!")
                    break
                else:
                    print("Something is wrong! Try again!")

        elif get_request == '/help':
            print(info.instruction)

        elif get_request == "/clear":
            print(info.clear_area)

        elif get_request == '/return':
            print('You are in main menu, there no back!')

        elif get_request == '/end':
            print("GoodBye!")
            global_point = False
            break

        else:
            print("Write a correct request!")


    while utilities.chek_login(profile_login):
        deleted_point = True
        print(f'\nHello, {profile_login}! This is your page!\n')
        get_req_loggin = input("What do you want? - ")

        if get_req_loggin == "/info":
            pprint(utilities.chek_info_profile(profile_login))

        elif get_req_loggin == "/help":
            print(info.logged_instruction)

        elif get_req_loggin == "/clear":
            print(info.clear_area)

        elif get_req_loggin == "/get_post":
            while True:
                post_number = input("Print number of your post - ")
                if post_number == "/return":
                    break
                if post_number.isdigit():
                    if utilities.find_post(profile_login, post_number) is not False:
                        print(f"\n[{utilities.find_post(profile_login, post_number)}]")
                        break
                    else:
                        print(f"Post by '{post_number}' doesn't exist!")
                        break
                else:
                    print("Write a number!")

        elif get_req_loggin == '/all_posts':
            print()
            if utilities.get_all_posts(profile_login):
                for num, i in enumerate(utilities.get_all_posts(profile_login)):
                    print(f"   {num} - {i}")
            else:
                print("You don't have posts yet!")

        elif get_req_loggin == "/delete":

            while deleted_point:
                del_login = input("Write your login to delete - ")
                if del_login == "/return":
                    break
                del_password = input("Write your password to delete - ")
                if del_password == "/return":
                    break

                if utilities.check_log_pass(del_login, del_password) == "success":
                    while True:
                        verification = input('Are you sure?(Yes/No) - ')
                        if verification == "Yes":
                            utilities.del_acc(del_login)
                            profile_login = None
                            menu_point = True
                            deleted_point = False
                            print('\nYour profile was successfully deleted! Bye!')
                            break
                        elif verification == "No":
                            deleted_point = False
                            break
                        else:
                            print("Write correct answer!")
                else:
                    print("Something is wrong! Try again!")

        elif get_req_loggin == "/return":
            print('You are in profile menu, there are no back!')

        elif get_req_loggin == "/sing_out":
            print(f"Bye, {profile_login}! See you next time!")
            profile_login = None
            menu_point = True
            break

        elif get_req_loggin == "/end":
            print("GoodBye!")
            global_point = False
            break

        else:
            print("Write a correct request!")