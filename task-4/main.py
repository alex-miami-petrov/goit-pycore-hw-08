from pharse_input import pharse_input as pharse
from contact_operations import *
from address_book import AddressBook, NoteBook, save_data, load_data
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