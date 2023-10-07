# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os

phonebook = []


def add_contact():  # добавление контакта в справочник
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    contact = {"Фамилия": surname, "Имя": name, "Отчество": patronymic, "Телефон": phone_number}
    phonebook.append(contact)
    print('Контакт добавлен')


def show_all_contacts(): # вывод данных из справочника
    if len(phonebook) == 0:
        print('контакты не добавлены')
    else:
        for contact in phonebook:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}\n")


def save_phonebook(): # сохранение контакта в справочник
    if len(phonebook) == 0:
        print('контакты не добавлены')
    else:
        filename = input('Введите имя файла: ')
        with open(filename + ".txt", "w", encoding="utf8") as f:
            for contact in phonebook:
                f.write(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}\n")
        print('Контакты сохранены')


def load_phonebook(): # загрузка из файла
    filename = input('Введите имя файла: ')
    if not os.path.exists(filename + ".txt"):
        print('Указанный файл не обнаружен')
    else:
        with open(filename + ".txt", "r", encoding="utf8") as f:
            for line in f:
                contact_data = line.strip().split(": ")
                surname, name, patronymic = contact_data[0].split(" ")
                phone_number = contact_data[1]
                contact = {"Фамилия": surname, "Имя": name, "Отчество": patronymic, "Телефон": phone_number}
                phonebook.append(contact)
        print('Контакты загружены')


def search_contact(): # поиск контакта
    if len(phonebook) == 0:
        print("контакты не добавлены")
    else:
        search_param = input("Введите параметр для поиска (Фамилия/Имя/Отчество/Телефон): ")
        search_value = input("Введите значение параметра: ")
        found_contacts = []
        for contact in phonebook:
            if contact[search_param] == search_value:
                found_contacts.append(contact)
        if len(found_contacts) == 0:
            print("Контакты не найдены!")
        else:
            for contact in found_contacts:
                print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")
                
def edit_contact(phonebook): # редактирование данных
    phone_number = input('Введите номер телефона контакта: ')
    for contact in phonebook:
        if contact['Телефон'] == phone_number:
            contact['Фамилия'] = input('Введите фамилию: ')
            contact['Имя'] = input('Ввелите имя: ')
            contact['Отчество'] = input('Ввелите отчество: ')
            contact['Телефон'] = input('Введите номер телефона: ')
            print('Спасибо, контакт изменен')
            return
    print('Контакт не найден')

def delete_contact(phonebook): # удаление данных
    phone_number = input('Введите номер контакта для удаления: ')
    for i, contact in enumerate(phonebook):
        del phonebook[i]
        print('Контакт удален')
        return
    print('Контакт не обнаружен')
    

while True:
    print("1. Добавить контакт")
    print("2. Показать контакты")
    print("3. Сохранить справочник в файл")
    print("4. Загрузить справочник из файла")
    print("5. Поиск контакта по параметру")
    print("6. Редактировать контакт")
    print("7. Удалить контакт")
    print("8. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_all_contacts()
    elif choice == "3":
        save_phonebook()
    elif choice == "4":
        load_phonebook()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        edit_contact(phonebook)
    elif choice == "7":
        delete_contact(phonebook)
    elif choice == "8":
        break
    else:
        print("Неверный выбор!")