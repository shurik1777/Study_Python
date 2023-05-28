import text
import view
import model

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_serch(text.input_search)
                result = model.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_serch(text.input_change)
                result = model.search_contact(key_word)
                if len(result) != 1:
                    pass
                else:
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change_contact()


            case 7:
                pass
            case 8:
                break