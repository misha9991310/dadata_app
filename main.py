from dadata import Dadata
from SQL_func import create_db, parameters, exit
from prettytable import PrettyTable

token = input("Введите API-ключ : ")
secret = input("Введите Секретный ключ : ")
language = input('Введите язык ответ ru или en : ')

if language != "ru" and language != "en":
    language = "ru"

print("Для выхода введите exit!!!")

create_db(token, secret, language)


def dadata_api():
    param = parameters()
    token, secret, lan = param[0][0], param[0][1], param[0][2]
    try:
        while True:
            value = input("Введите адрес : ")
            variants = []
            t = PrettyTable(['Номер', 'Адрес'])
            otv = PrettyTable(['Адрес', 'Широта', "Долгота"])
            if value == 'exit':
                exit()
                break
            else:
                dadata = Dadata(token, secret)
                result = dadata.suggest(name="address", query=value, language=lan, count=15)
                x = 0

                for i in result:
                    x = x + 1
                    variants.append(i['value'])
                    t.add_row([f"№{x}", i['value']])


                if len(variants) == 0:
                    print("Совподений не найдено")

                else:
                    while True:
                        t.align = "l"
                        print(t)
                        y = input("Введите номер подходящего адреса : ")
                        if y == "exit":
                            exit()
                            break

                        elif 0 <= int(y) <= x:
                            result = dadata.clean("address", variants[int(y) - 1])
                            otv.add_row([result["result"], str(result['geo_lat']), str(result['geo_lon'])])
                            print(otv)
                            break
                        else:
                            print("Такого номера не существует\nВыбирите другой:")

    except Exception as e:
        print(f"Произошла ошибка : {e}")


if __name__ == '__main__':
    dadata_api()
