from pharse_input import pharse_input as pharse
from contact_operations import *
from address_book import AddressBook, NoteBook
from address_book import save_data, load_data
from note import add_note_cmd, find_note_cmd, edit_note_cmd, delete_note_cmd, search_note_by_tag_cmd, sort_notes_by_tag_cmd

def main():
    book, notes = load_data() 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = pharse(user_input)

        if command in ["close", "exit"]:
            save_data(book, notes)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "email":
            print(show_email(args, book))

        elif command == "address":
            print(show_address(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday_contact(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        elif command == "find":
            print(find_contact(args, book))

        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "add-note":
            print(add_note_cmd(args, notes))

        elif command == "find-note":
            print(find_note_cmd(args, notes))

        elif command == "edit-note":
            print(edit_note_cmd(args, notes))

        elif command == "delete-note":
            print(delete_note_cmd(args, notes))

        elif command == "search-tag":
            print(search_note_by_tag_cmd(args, notes))

        elif command == "sort-tag":
            print(sort_notes_by_tag_cmd(args, notes))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


# Виконайте команду python main.py.
# Взаємодійте з ботом:

# Після запуску ви побачите повідомлення "Welcome to the assistant bot!". Тепер ви можете вводити команди для перевірки його функціональності. Ось кілька команд, які ви можете спробувати:

# hello: Бот повинен відповісти "How can I help you?".
# add John 1234567890: Додасть контакт з ім'ям John та номером телефону 1234567890.
# phone John: Покаже номер телефону для John.
# change John 1234567890 0987654321: Змінить номер телефону John на 0987654321.
# add-birthday John 01.01.2000: Додасть день народження для John.
# show-birthday John: Покаже день народження John.
# all: Покаже список усіх збережених контактів.
# birthdays: Покаже список контактів, у яких день народження протягом наступних 7 днів (якщо такі є).
# birthdays 3: Покаже список контактів, у яких день народження протягом наступних 3 днів.
# find John: Знайде та покаже інформацію про контакт John.
# delete John: Видалить контакт John.
# add-note My important note: Додасть нотатку "My important note".
# add-note Another note --tag work --tag idea: Додасть нотатку "Another note" з тегами "work" та "idea".
# find-note important: Знайде нотатки, що містять слово "important".
# find-note --tag work: Знайде нотатки з тегом "work".
# edit-note 1 New content: (Після додавання нотатки ви можете спробувати редагувати її, використовуючи її ID, який може бути виведено при знаходженні).
# delete-note 1: (Видалить нотатку з ID 1).
# close або exit: Завершить роботу бота та збереже дані.