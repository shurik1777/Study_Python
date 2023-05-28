phone_book = []
path = 'phones.txt'


def open_pb():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(new)


def get_pb():
    global phone_book
    return phone_book
