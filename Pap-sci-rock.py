from random import randint


def game():
    # Счетчик побед
    user_score = 0
    comp_score = 0
    print("Добро пожаловать в игру камень-ножницы-бумага!")
    print("Камень - 1")
    print("Бумага - 2")
    print("Ножницы - 3")

    # Выбор действия
    actions = {"1":"Камень","2":"Бумага","3":"Ножницы"}

    results = {(1, 2): "comp", (2, 1): "user",
               (3, 1): "comp", (1, 3): "user",
               (2, 3): "comp", (3, 2): "user"}

    while True:

        user_turn = input("Введите ваш выбор(1-3): ").strip()
        comp_turn = randint(1,3)

        if user_turn.isalpha() or int(user_turn) not in range(1,4):
                continue
        # Всевозможные игровые сценарии

        elif results.get((int(user_turn),comp_turn),"draw") == "draw":
            print(f"Игрок выбрал {actions[user_turn]}; Comp выбрал {actions[str(comp_turn)]}")
            print("Ничья")

        elif results.get((int(user_turn),comp_turn),"draw") == "comp":
            print(f"Игрок выбрал {actions[user_turn]}; Comp выбрал {actions[str(comp_turn)]}")
            print("В раунде выиграл Comp")
            comp_score+=1

        else:
            print(f"Игрок выбрал {actions[user_turn]}; Comp выбрал {actions[str(comp_turn)]}")
            print("В раунде выиграл User")
            user_score+=1
        # Итоги
        if comp_score == 3:
            return "Comp"
        elif user_score == 3:
            return "User"





Winner = game()
print(f"Победителем стал {Winner}")








