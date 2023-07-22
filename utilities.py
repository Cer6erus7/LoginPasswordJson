import json
import datetime
import pprint


def chek_login(login):
    """
    Функция пригимает аргумент логин и проверяет его на наличие в базе данных
    :param login:
    :return: boolean
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        for i in data["users"]:
            if i["login"] == login:
                return True
    return False


def user_registration(login, password):
    """
    Принимает в качестве аргументов логин и пароль пользователя. Создаем уникоальное айди пользователя, а также
    время создания акаунта. Считываем все данные с файла, и в список ключа "users" добавялем новый аккаунт, и наконец
    перезаписываем полностью файл с этими новыми данными.
    :param login:
    :param password:
    :return:
    """
    with open('db.json', 'r') as f:
        id = len(json.load(f)["users"]) + 1
    time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    account = {"login": login,
               "password": password,
               "id": id,
               "date_of_create": time,
               "status": True,
               "amount_of_posts": 0,
               "posts": []}

    with open('db.json', 'r') as f:
        data = json.load(f)
    data["users"].append(account)

    with open('db.json', 'w') as f:
        json.dump(data, f, indent=3)


def check_log_pass(login, password):
    """
    Принимает в качестве аргументов логин и пароль. Сверяет их с базой данных ноходящиеся в json файле и если аккаунт,
    не удален возвращает строку "success", если же аккаунт удалён возвращает "delete". Но если же логин и пароль не
    верны, возвращает значение False
    :param login:
    :param password:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        for users in data["users"]:
            if users["login"] == login and users["password"] == password and users["status"] is True:
                return 'success'
            elif users["login"] == login and users["password"] == password and users["status"] is False:
                return 'deleted'
    return False


def chek_info_profile(login):
    """
    Принимает логин пользователя, и возвращает полную информацию о нём
    :param login:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        for users in data["users"]:
            if users["login"] == login:
                return {'login': users["login"],
                        "password": users["password"],
                        "id": users["id"],
                        "date_of_create": users["date_of_create"],
                        "status": users["status"],
                        "amount_of_posts": users["amount_of_posts"],
                        }
    return "Not found"


def del_acc(login):
    """
    Принимает логин пользователя. Проходит через список и ищёт пользователя которого хотим удалить. Те кто не является
    желаемыми пользователями отправляются в список, наш пользователь также отправляется в список, но перед этим меняем
    ему статус на False. Потом этому же списку даем ключ "users" и перезаписываем польностью наш json файл.
    :param login:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        lst = []
        for user in data['users']:
            if user["login"] == login:
                user["status"] = False
                lst.append(user)
            else:
                lst.append(user)

    with open("db.json", 'w') as f:
        json.dump({"users": lst}, f, indent=3)


def find_post(login, number):
    """
    Принимает логин и номер поста пользователя. Возвращает пост под введеным номером, если же нет
    такого поста, выведет False.
    :param login:
    :param number:
    :return:
    """
    try:
        with open('db.json', 'r') as f:
            data = json.load(f)
            for user in data["users"]:
                if user["login"] == login:
                    return user['posts'][int(number)]
    except:
        return False


def get_all_posts(login):
    """
    Принимает логин пользователя и возвращает полный список всех постов
    :param login:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        for user in data["users"]:
            if user["login"] == login:
                return user["posts"]


def add_post(login, post):
    """
    Принимает логин и пост пользователя, а затем добавляет его в базу данных
    :param login:
    :param post:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        lst = []
        for user in data["users"]:
            if user["login"] == login:
                user["amount_of_posts"] += 1
                user["posts"].append(post)
                lst.append(user)
            else:
                lst.append(user)

    with open('db.json', 'w') as f:
        json.dump({"users": lst}, f, indent=3)


def delete_post(login, number):
    """
    Принимает лонин и номер посата, и удаляет пост под номером полученым от пользователя
    :param login:
    :param number:
    :return:
    """
    with open('db.json', 'r') as f:
        data = json.load(f)
        lst = []
        try:
            for user in data["users"]:
                if user["login"] == login:
                    user["amount_of_posts"] -= 1
                    user["posts"].pop(int(number))
                    lst.append(user)
                else:
                    lst.append(user)
        except:
            return False

    with open('db.json', 'w') as f:
        json.dump({"users": lst}, f, indent=3)


if __name__ == "__main__":
    # print("hello")
    # user_registration("da", "pizpa")
    print(check_log_pass(login='Matvey', password='12345'))
    pprint.pprint(chek_info_profile("Matvey"))
    # del_acc('Kolya')
    print(get_all_posts("Matvey"))
    # add_post("Ernest", "I'm bezdelnik!!!!")
