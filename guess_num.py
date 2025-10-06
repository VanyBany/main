from random import randint


def guess_game():
    num = randint(1,101)
    status = "чётным" if num % 2 == 0 else "нёчетным"
    attempts = 3
    while attempts != 0:
        
        
        try:
            # Проверка ввода (не пустит дальше пока не будет введено корректное значение)
            guess = int(input("Угадайте число в диапазоне от 1 до 100: ").strip())
            if guess in range(1,101):
            # Проверка числа
                if guess == num:
                    return "Вы угадали число!"
                elif guess > num:
                    attempts-=1
                    print("Загаданное число меньше")
                else:
                    attempts-=1
                    print("Загаданное число больше")
                if attempts == 1:
                    print(f"Число является {status}")

        except ValueError:
            continue
    return "Вы потратили все попытки"

print(guess_game())