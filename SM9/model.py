phone_book: list[dict[str, str]] = []
path = 'phones.txt'


def open_pb():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    phone_book.append(new)
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def change_contact(new: dict, index: int) -> str:
    global phone_book
    name = phone_book.pop(index - 1).get('name')
    phone_book.insert(index - 1, new)
    return name
