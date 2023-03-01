import random as rd
import re

class Paradoxes:
    def __init__(self):
        pass

    @staticmethod
    def monti_holl(iter=10000):
        win_ved = 0
        win_self = 0
        mas = [1, 0, 0]
        for i in range(iter):
            choise = rd.randint(0, 2)
            if mas[choise] == 1:
                win_self += 1
            else:
                win_ved += 1
        print((win_ved / iter) * 100, "%", sep="")

    @staticmethod
    def birthday(iter=10000):
        n = 23
        match_count = 0
        for i in range(iter):
            birthdays = []
            for j in range(n):
                birthdays.append(rd.randint(1, 336))
            for k in birthdays:
                if birthdays.count(k) >= 2:
                    match_count += 1
                    break
        print((match_count / iter) * 100, "%", sep="")

    @staticmethod
    def field_of_wonders():
        words = ["книга", "месяц", "река", "компьютер", "питон", "еж", "сифилис"]
        while len(words) != 0:
            word_num = rd.randint(0, len(words) - 1)
            secret_word_str = words[word_num]
            secret_word_lst = list(words[word_num])
            win_word = secret_word_lst

            # Выбор сложности
            level = input("Выберите уровень сложности (легкий, средний, сложный): ")
            if level == "легкий":
                print(f"Вы выбрали {level} уровень сложности")
                life_count = 7
            elif level == "средний":
                print(f"Вы выбрали {level} уровень сложности")
                life_count = 5
            else:
                print(f"Вы выбрали {level} уровень сложности")
                life_count = 3

            print(secret_word_str)
            secret_w = []
            for i in range(len(secret_word_str)):
                secret_w.append("*")
            game = True

            # Начало игры
            while game:
                if len(words) != 0:
                    print("Секретное слово: ", secret_w, " | ❤x", life_count, sep="")
                    print(secret_w, win_word)
                    if secret_w.count("*") == 0:
                        print("Вы выиграли! Поздравляем!")
                        words.remove(secret_word_str)
                        if len(words) != 0:
                            EoC = int(input("Сыграть еще раз? Да - 1 Нет - 2 \n"))
                            if EoC == 1:
                                game = False
                            elif EoC == 2:
                                game = False
                                words.clear()
                                break
                    else:
                        i = int(input("1 - ввести букву \n2 - ввести слово \n"))
                        # Пользователь ввел букву
                        if i == 1:
                            letter = input("Введите букву ")
                            if letter in secret_word_lst:
                                for i in range(len(win_word)):
                                    if win_word[i] == letter:
                                        win_word[i] = "*"
                                        secret_w[i] = letter
                            else:
                                if life_count > 1:
                                    life_count -= 1
                                    print("Вы потеряли 1 жизнь! Осталось", life_count)
                                else:
                                    print("Вы проиграли! Повезет в следующий раз!")
                                    words.remove(secret_word_str)
                                    if len(words) != 0:
                                        EoC = int(input("Сыграть еще раз? Да - 1 Нет - 2 \n"))
                                        if EoC == 1:
                                            game = False
                                        elif EoC == 2:
                                            game = False
                                            words.clear()
                                            break
                        if i == 2:
                            word = input("Введите слово ")
                            if word == secret_word_str:
                                print("Вы выиграли! Поздравляем!")
                                words.remove(secret_word_str)
                                if len(words) != 0:
                                    EoC = int(input("Сыграть еще раз? Да - 1 Нет - 2 \n"))
                                    if EoC == 1:
                                        game = False
                                    elif EoC == 2:
                                        game = False
                                        words.clear()
                                        break
                            else:
                                print("Вы проиграли! Повезет в следующий раз!")
                                words.remove(secret_word_str)
                                if len(words) != 0:
                                    EoC = int(input("Сыграть еще раз? Да - 1 Нет - 2 \n"))
                                    if EoC == 1:
                                        game = False
                                    elif EoC == 2:
                                        game = False
                                        words.clear()
                                        break

    @staticmethod
    def read_file(name):
        with open(f"files/{name}", 'r') as file:
            rf = file.read()
        rf = rf.lower()
        uniq_words = set(rf.split())
        uniq_words_lst = []
        for i in uniq_words:
            uniq_words_lst.append(i)
        return uniq_words_lst

    @staticmethod
    def save_file(name, uw_lst):
        words = len(uw_lst)
        uw_lst = sorted(uw_lst)
        with open(f"files/{name}", "w") as file:
            file.write(f"Всего уникальных слов: {words} \n")
            for i in uw_lst:
                file.write(f"{i} \n")

    @staticmethod
    def prak5():
        name = input("Введите имя файла из папки files ")
        try:
            f = open(f"files/{name}", "r")
            nums = []
            for line in f:
                line1 = ''.join(filter(str.isalnum, line))
                nums.append(line1)
            del nums[0]
            print(nums)
        except:
            print("Ошибка: такого файла нет в папке files!")

    @staticmethod
    def prak6():
        new_file = open("files/new_trains.txt", "w+")
        with open("files/trains.txt", "r") as file1:
            for line in file1:
                try:
                    tnum = re.search(r'\d{3}', line)[0]
                    ttime = re.search(r'\d\d:\d\d:\d\d', line)[0]
                    in_out = line.split()[3]
                    city = line.split()[4]
                    record = f"[{ttime}] - Поезд № {tnum} {in_out} {city} \n"
                    new_file.write(record)
                except:
                    continue
        file1.close()

    #Создание файла и получение списка списков
    @staticmethod
    def prak7():
        #Создание таблицы с книгами
        # columns = ['isbn', 'title', 'author', 'quantity', 'price']
        # data = [
        #     ['978-1-43545-500-9', 'Python Programming for the Absolute Beginner', 'Michael Dawson', '10', '18.90'],
        #     ['978-0-59600-372-2', 'XSLT Cookbook', 'Sal Mangano', '15', '34.60'],
        #     ['978-0-32168-056-3', 'Programming in Python 3', 'Mark Summerfield', '8', '27.28'],
        #     ['978-1-44935-573-9', 'Learning Python', 'Mark Lutz', '21', '34.20'],
        #     ['978-0-47178-597-2', 'Ajax For Dummies', 'Steve Holzner', '32', '11.80'],
        #     ['978-1-78439-700-5', 'Mastering Python Networking', 'Eric Chou', '23', '31.49'],
        #     ['978-8-59037-986-7', 'Programming in Lua', 'Roberto lerusalimschy', '12', '37.10'],
        #     ['978-1-78439-658-9', 'Machine Learning in Java', 'Bostjan Kaluza', '45', '34.99']
        # ]
        # df = pd.DataFrame(data, columns=columns)
        # df.to_csv(r'files/books.csv')
        file_lst = []
        with open("files/books.csv", "r") as file:
            for line in file:
                file_lst.append(line.split(","))
        return file_lst

    @staticmethod
    def get_books(books_lst, name):
        list = []
        for i in books_lst:
            if name in i[2].lower():
                list.append(i)
        return list

    @staticmethod
    def get_totals(lst):
        list_k = []
        for i in lst:
            if int(i[4])*float(i[5]) < 500:
                kor = (i[1], int(i[4])*float(i[5])+100)
                list_k.append(kor)
            else:
                kor = (i[1], int(i[4]) * float(i[5]))
                list_k.append(kor)
        print(list_k)