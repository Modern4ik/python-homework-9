import view
import model
import text

main_phone_book = model.PhoneBook()

def search_module():
    search_word = view.input_data(text.search_word_string)
    search_result = model.PhoneBook(main_phone_book.search_contact(search_word))
    print(search_result)
    view.show_contacts(search_result, text.search_error(search_word))
    
    return search_result

def start():
    
    flag = True

    while flag:
        user_input = view.show_menu()

        match user_input:
            case 1:
                main_phone_book.open_file()
                view.print_msg(text.load_success)
            case 2:
                if len(main_phone_book.phone_book) != 0:
                    main_phone_book.save_file()
                    view.print_msg(text.save_success)
                else:
                    view.print_msg(text.save_error)
            case 3:
                view.show_contacts(main_phone_book, text.empty_book)
            case 4:
                contact = view.input_new_contact(text.fields_new_contact)
                main_phone_book.add_contact(contact)
                view.print_msg(text.new_contact_success(contact[0]))
            case 5:
                search_module()
            case 6:
                if search_module():
                    uid = view.input_number(text.input_change_uid)
                    change = view.input_new_contact(text.fields_change_contact)
                    name = main_phone_book.change_contact(uid, change)
                    view.print_msg(text.change_success(name))
            case 7:
                if search_module():
                    uid = view.input_number(text.input_del_uid)
                    name = main_phone_book.delete_contact(uid)
                    view.print_msg(text.delete_success(name))
            case 8:
                if main_phone_book.phone_book != main_phone_book.origin_phone_book:
                    flag = view.input_data(text.save_flag)

                    if flag.upper() == 'Y':
                        main_phone_book.save_file()
                        view.print_msg(text.save_success)

                view.print_msg(text.good_bye)
                break