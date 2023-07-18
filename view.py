import text
from model import Contact
from model import PhoneBook


def show_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print('\t' + f'{i}. {item}')
        else:
            print('\t' + item)
    
    select_option = input('Выберите пункт меню: ')

    flag = True

    while flag:
        if select_option.isdigit() and 0 < int(select_option) <= len(text.main_menu) - 1:
            return int(select_option)
        else:
            select_option = input(text.main_menu_input_error)

def show_contacts(book: PhoneBook, msg: str):
    if book:
        max_n, max_p, max_c = book.get_max_field()

        print('\n' + '=' * (7 + max_n + max_p + max_c))
        for uid, contact in book.phone_book.items():
            print(f'{uid: >3}. {contact.to_show(max_n, max_p, max_c)}')
        print('=' * (7 + max_n + max_p + max_c) + '\n')
    else:
        print_msg(msg)
   

def input_new_contact(new_contact_lst: list[str]):
    new_contact = []

    for item in new_contact_lst:
        new_contact.append(input(item))
    
    return new_contact

def input_data(msg: str):
    return input(msg)

def input_number(msg: str):
    numb = input(msg)
    flag = True

    while flag:
        if numb.isdigit():
            flag = False
        else:
            numb = input(text.number_error)
    
    return int(numb)

def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')