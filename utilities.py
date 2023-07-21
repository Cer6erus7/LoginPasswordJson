import json
import datetime


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
        id = len(json.load(f)["users"])+1
    time = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    account = {"login": login, "password": password, "id": id, "date_of_create": time}

    with open('db.json', 'r') as f:
        data = json.load(f)
    data["users"].append(account)

    with open('db.json', 'w') as f:
        json.dump(data, f, indent=3)


if __name__ == "__main__":
    print("hello")
    user_registration("da", "pizpa")