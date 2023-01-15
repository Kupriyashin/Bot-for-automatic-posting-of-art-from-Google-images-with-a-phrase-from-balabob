def otvet_and_art():
    try:

        slova_generate = ['кодомо', 'сенэн', 'седзе', 'анимеха', 'анимешник', 'анимешница', 'анимашка', 'Манга',
                          'Мангака',
                          'Гэкига', 'Токусацу', 'Сэйю', 'Танкобон', 'Меха', 'Хэнсин', 'опенинг', 'эндинг', 'Омакэ',
                          'Сэнтай',
                          'Махо - сёдзё',
                          'Спокон', 'Киберпанк', 'Добуцу', 'Кавайи', 'Хентай', 'Яой', 'Юри', 'Отаку', 'Хентайщик',
                          'Отака',
                          'Анимессианство', 'Додзинси', 'Фанфик',
                          'Косплей', 'Кавайи', 'Каккойи', 'Чиби', 'Бака', 'Гайдзин', 'Бисёнэн']

        import random
        from otvet_balabola import otvet_balabob
        from poluchenie_random_art import random_art

        slova_generate = slova_generate[random.randint(0, len(slova_generate) - 1)]
        path_image = random_art()
        otvet = f"{slova_generate} {otvet_balabob(slova_generate)}"

        if otvet != 'error' and path_image[0] != 'error':
            name_anime = path_image[1]
            return otvet, path_image[0], name_anime

    except Exception as err_otvet_and_art:
        print(f"Произошла ошибка в функции otvet_and_art: {err_otvet_and_art}")
