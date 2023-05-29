#  Пример реализации телефонного справочника:
import os


def read_file():
    if not os.path.exists('phonebook.txt'):
        print('Файл не существует.')
        return {}

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read()

    if not data:
        return {}

    phonebook = eval(data)
    return phonebook


def save_file(phonebook):
    with open('phonebook.txt', 'w', encoding='UTF-8') as f:
        f.write(str(phonebook))


def add_contact(phonebook):
    print('Добавление нового контакта:')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    email = input('Введите электронную почту: ')
    address = input('Введите адрес: ')
    phonebook[name] = {'phone': phone, 'email': email, 'address': address}
    print(f'Контакт {name} добавлен в справочник.')


def find_contact(phonebook):
    name = input('Введите имя контакта: ')
    if name in phonebook:
        contact = phonebook[name]
        print(f'Телефон: {contact["phone"]}')
        print(f'Электронная почта: {contact["email"]}')
        print(f'Адрес: {contact["address"]}')
    else:
        print(f'Контакт {name} не найден в справочнике.')


def modify_contact(phonebook):
    name = input('Введите имя контакта: ')
    if name in phonebook:
        contact = phonebook[name]
        print('Редактирование контакта:')
        phone = input(f'Введите новый телефон (было {contact["phone"]}): ')
        email = input(f'Введите новую электронную почту (было {contact["email"]}): ')
        address = input(f'Введите новый адрес (был {contact["address"]}): ')
        contact.update({'phone': phone, 'email': email, 'address': address})
        print(f'Контакт {name} изменен.')
    else:
        print(f'Контакт {name} не найден в справочнике.')


def delete_contact(phonebook):
    name = input('Введите имя контакта для удаления: ')
    if name in phonebook:
        del phonebook[name]
        print(f'Контакт {name} удален.')
    else:
        print(f'Контакт {name} не найден в справочнике.')


def menu():
    phonebook = read_file()
    while True:
        print('\nСправочник телефонов')
        print(f'1. Просмотр всех контактов 2. Добавление нового контакта 3. Поиск контакта '
              f'4. Редактирование контакта 5. Удаление контакта 6. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            if not phonebook:
                print('Справочник пуст.')
            else:
                for name, contact in phonebook.items():
                    print(f'Имя: {name} Телефон: {contact["phone"]} '
                          f'Электронная почта: {contact["email"]} Адрес: {contact["address"]}')                    
                    print()

        elif choice == '2':
            add_contact(phonebook)

        elif choice == '3':
            find_contact(phonebook)

        elif choice == '4':
            modify_contact(phonebook)

        elif choice == '5':
            delete_contact(phonebook)

        elif choice == '6':
            save = input('Сохранить изменения перед выходом? ( да / нет ) -> ')
            if save.lower() == 'да':
                save_file(phonebook)
            break

        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    menu()
