def sent_ch(stroka):
    counts = []

    alpgl = "АЕЁИОУЫЭЮЯAEIOUY"
    alpsogl = "БВГДЖЗЙКЛМНПРСТФХЦЧШBCDFGHJKLMNPQRSTVWXYZ"
    # Кол-во пробелов и слов
    space = stroka.count(" ")
    words = len(stroka.split())

    stroka = stroka.upper().replace(" ","")
    print(stroka)
    
    counts = {}
    for i in stroka:
        if i not in counts.keys():
            counts[i] = 1
        else:
            counts[i] += 1
    print(counts.items())            
    
        
    for i in alpgl:
        stroka = stroka.replace(i,"A")
    for i in alpsogl:
        stroka = stroka.replace(i,"Б")
    print(stroka)
    gl = stroka.count("A")
    sogl = stroka.count("Б")
    
    
    print(gl,sogl,space,words)


sent_ch(input("Введите предложение для анализа: "))


    