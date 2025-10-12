accounts = {}
# Cоздание аккаунта
def create_acc(name):
    if name not in accounts:
        accounts[name] = 0
        print(f"Аккаун {name} был успешно создан!")
    else:
        print("Такой аккаунт уже существует!")

# Пополнение счёта
def deposit(name,amount):
    if name in accounts:

        if amount > 0:
            accounts[name]+=amount
            print(f"Баланс счёта был пополнен на сумму {amount} руб.")
        else:
            print("Сумма пополнения должна быть положительной!")



    else:
        print("Такой аккаунт не существует!")
# Списание со счёта

def withdraw(name,amount):

    if amount > 0 and amount <= accounts[name]:
            accounts[name] -= amount
            print(f"C баланса счёта было списано {amount} руб.")

    else:
        print("Сумма списания должна быть положительной и не больше баланса счета!")


# Перевод
def transfer(name_sender,name_receiver,amount):
    if name_sender in accounts and name_receiver in accounts:


        if amount > 0 and amount <= accounts[name_sender]:
            accounts[name_receiver] +=amount
            accounts[name_sender] -= amount
            print(f"Перевод на сумму {amount} руб. был отправлен на имя {name_receiver}")

        else:
            print("Сумма пополнения должна быть положительной и не больше баланса счета!")



    else:
        print("Аккаунт отправителя или получателя нет в базе данных!")
# Проверка баланса счёта
def check_acc(name):
    if name in accounts:
        print(f"Баланс счёта: {accounts[name]}")
    else:
        print("Такой аккаунт не существует!")

def menu():
    print("Добро пожаловать в симулятор банковских операций!")
    print("Создание счёта - 1")
    print("Проверка баланса счета - 2")
    print("Пополнение счета - 3")
    print("Списание со счета - 4")
    print("Перевод - 5")


    while True:

        try:

            operation = int(input("Введите операцию(1-6): ".strip()))

            if operation == 1:
                name = input("Введите имя: ")
                create_acc(name)

            elif operation == 2:
                name = input("Введите имя: ")
                check_acc(name)

            elif operation == 3:
                name = input("Введите имя: ")
                amount = int(input("Введите сумму: ").strip())
                deposit(name,amount)

            elif operation == 4:
                name = input("Введите имя: ")
                amount = int(input("Введите сумму: ").strip())
                withdraw(name,amount)

            elif operation == 5:
                name_sender = input("Введите имя отправителя: ")
                name_receiver = input("Введите имя получателя: ")
                amount = int(input("Введите сумму: ").strip())
                transfer(name_sender,name_receiver,amount)

            elif operation == 6:
                print("Спасибо, что пользовались нами!")
                return



            else:
                print("Введите корректное значение!")


        except:
            print("Введите корректное значение!")
            continue

menu()