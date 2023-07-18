from copy import deepcopy

class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment
    
    def to_iter(self):
        return [self.name, self.phone, self.comment]
    
    def to_show(self, name: int, phone: int, comment: int):
        return f'{self.name: <{name}} {self.phone: <{phone}} {self.comment: <{comment}}'

class PhoneBook:

    def __init__(self, path: str = 'phonebook.txt') -> None:
        self.phone_book: dict[int, Contact] = {}
        self.path = path
        self.origin_phone_book = {}

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()

        for contact in data:
            uid, name, phone, comment = contact.strip().split(';')
            self.phone_book[int(uid)] = Contact(name, phone, comment)
        
        self.origin_phone_book = deepcopy(self.phone_book)

        return self.origin_phone_book

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            all_contacts = []

            for uid, contact in self.phone_book.items():
                all_contacts.append(';'.join([str(uid), contact[0], contact[1], contact[2]]))
            
            all_contacts = '\n'.join(all_contacts)
            file.write(all_contacts)

    def add_contact(self, new: list[str]):
        uid = max(self.phone_book) + 1

        self.phone_book[uid] = Contact(*new)

    def search_contact(self, word: str):
        

        for uid, cur_contact in self.phone_book.items():
            for field in cur_contact.to_iter():
                if word.lower() in field.lower():
                    result = PhoneBook

        return result
        
        

    def delete_contact(self, id):
        return self.phone_book.pop(id)[0]

    def change_contact(self, uid: int, change: list[str]) -> str:
        contact = self.phone_book.get(uid)

        for i in range(3):
            if change[i]:
                contact[i] = change[i]

        return contact.name
    
    def get_max_field(self):
        max_name = []
        max_phone = []
        max_comment = []

        for contact in self.phone_book.values():
            max_name.append(contact.name)
            max_phone.append(contact.phone)
            max_comment.append(contact.comment)
        
        return len(max(max_name, key=len)), len(max(max_phone, key=len)), len(max(max_comment, key=len))