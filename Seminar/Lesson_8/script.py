from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('\nВывожу данные для Вас из 1-ого файла:\n')
    with open('data_first_variant.csv', 'r+', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('\nВывожу данные для Вас из 2-ого файла:\n')
    with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
        # data_second = list(file.readlines())
        data_second = file.readlines()
        data_second_version_second = []
        j = 0
        for i in range(len(data_second)):
            if data_second[i] == '\n' or i == len(data_second) - 1:
                data_second_version_second.append(''.join(data_second[j:i + 1]))
                j = i
        data_second = data_second_version_second
        print(''.join(data_second))
        # print(*data_second, sep='')
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print('\nМеняем:\n', data_first[number_journal-1])
        
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
        
        if number_journal != 1:
            start_contact = (number_journal - 1) * 5
        else:
            start_contact = number_journal - 1
        print("Что именно Вы хотите изменить?\n\n"
          "1. Имя\n"
          "2. Фамилию\n"
          "3. Номер телефона\n"
          "4. Адрес\n")
        command = int(input("Введите номер из списка: "))
        
        while command < 1 or command > 4:
            print('Ты дурак?! Даю тебе последний шанс')
            command = int(input("Введите номер операции: "))
        
        if command == 1:
            data_first[start_contact] = name_data() + '\n'
        elif command == 2:
            data_first[start_contact + 1] = surname_data() + '\n'
        elif command == 3:
            data_first[start_contact + 2] = phone_data() + '\n'
        else:
            data_first[start_contact + 3] = address_data() + '\n'
            
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print('\nМеняем:\n', data_second[number_journal-1])
        contact = data_second[number_journal-1].split(';')
        print("Что именно Вы хотите изменить?\n\n"
          "1. Имя\n"
          "2. Фамилию\n"
          "3. Номер телефона\n"
          "4. Адрес\n")
        command = int(input("Введите номер из списка: "))
        
        while command < 1 or command > 4:
            print('Ты дурак?! Даю тебе последний шанс')
            command = int(input("Введите номер операции: "))
        
        if command == 1:
            contact[0] = '\n' + name_data()
        elif command == 2:
            contact[1] = surname_data()
        elif command == 3:
            contact[2] = phone_data()
        else:
            contact[3] = address_data() + '\n'
            
        data_second[number_journal-1] = ';'.join(contact)
            
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        print('\nУДАЛЯЕМ:\n', data_first[number_journal-1])
        
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
        
        if number_journal != 1:
            start_contact = (number_journal - 1) * 5
        else:
            start_contact = number_journal - 1
            
        
        
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
  