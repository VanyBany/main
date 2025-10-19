def hg_game(word):
    Used_letters = []
    length = len(word)
    Right_letters = list("_"*length)
    print(f"Длина загаданного слова {length}")




    attempts = 10
    #Цикл пока остались попытки
    while attempts != 0:
        print(" ".join(Right_letters))
        guess_letter = input("Введите предполагаемую букву: ").strip().upper()
    # Проверка на слово и правильный ввод
        if guess_letter == word:
            return "Вы победили!"

        elif len(guess_letter) > 1 or not(guess_letter.isalpha()):
            print("Введите 1 букву!")

        elif guess_letter in Used_letters:
            print("Буква была использована!")
    # Проверка буквы в слове
        else:
            Used_letters.append(guess_letter)
            if guess_letter in word:

                for i in range(len(word)):
                    if word[i] == guess_letter:
                        Right_letters[i] = guess_letter

                if "".join(Right_letters) == word:
                    print(" ".join(Right_letters))
                    return "Вы победили!"
            else:
                attempts -= 1
                print(f"Буквы нет в слове, осталось {attempts}")


    return "Вы проиграли!"

# Ввод слова
word = input("Введите слово для игры: ").strip().upper()
print(hg_game(word))

