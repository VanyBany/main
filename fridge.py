from datetime import *
from decimal import Decimal as dec

DATE_FORMAT = '%Y.%m.%d'
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': dec('0.5'), 'expiration_date': datetime.strptime("2023.7.15",DATE_FORMAT).date()},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': dec('2'), 'expiration_date': datetime.strptime("2023.8.1",DATE_FORMAT).date()},
    ],
    'Пельмени Уральские': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': dec('0.5'), 'expiration_date': datetime.strptime("2023.7.15",DATE_FORMAT).date()},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': dec('2'), 'expiration_date': datetime.strptime("2023.8.1",DATE_FORMAT).date()},
    ],
    'Вода': [
        {'amount': dec('1.5'), 'expiration_date': None}
    ],
}
print(goods)
def add(name, amount, expiration_date, DATE_FORMAT = '%Y.%m.%d'):

    #Проверка на наличие даты
    if expiration_date != None:
        expiration_date = datetime.strptime(expiration_date,DATE_FORMAT).date()
    
    description = {
            "amount": amount,
            "expiration_date": expiration_date
        }
    
    if name in goods:
        print("Добавил")
        goods[name].append(description)

    else:
        goods[name] = [description]
    
    print(goods)


    



def add_by_note(title,DATE_FORMAT = '%Y.%m.%d'):
    # Разбиение строки на имя, кол-во, дату
    title = title.split(" ")
    last_el = title.pop()
    # Проверка на последнего элемента, что он является датой
    try:
        datetime.strptime(last_el,DATE_FORMAT)
    except:
        title.append(last_el)
        expiration_date = None
    last_el = title.pop()
    try:
        amount = dec(last_el)
    except:
        title.append(last_el)
        amount = None
    name = " ".join(title)
   



    return add(name,amount,expiration_date)





def find(title):
    products = []
    for name in goods.keys():
        if title.lower() in name.lower():
            products.append(name)
    return products


def amount(title):
    products = find(title)
    summa = 0
    # Нахождение продукта в списке goods
    for product in products:
        # Перебор всех покупок этого продукта
        for amount in range(len(goods[product])):
            # Сложение amount из строки покупки
            summa += goods[product][amount]["amount"]
    return summa


def menu():
    print("Добро пожаловать в виртуальный холодильник!")

    while True:

        print("Добавить продукт - 1")
        print("Поиск продуктов по слову - 2")
        print("Кол-во запрошенного продукта - 3")
        print("Выход - 4")
        action = input("Введите желаемую операцию(1-4): ").strip()

        if action == "1":
            print("Примечание: дата вида: год,месяц, день")

            title = input("Введите название продукта, его кол-во, срок годности(через точку): ")
            add_by_note(title)

        elif action == "2":
             title = input("Введите название продукта: ")
             print(find(title))
        
        elif action == "3":
            title = input("Введите название продукта: ")
            print(f"Кол-во всех {title.lower()} = {amount(title)}")

        elif action == "4":
            title = input("До скорых встреч!")
            return

        else:
            print("Введите число от 1 до 4!")
            continue
menu()