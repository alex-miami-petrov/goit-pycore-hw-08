# from address_book import AddressBook, Record, Name, Phone, Birthday

# def validate_contact_args(args: list) -> str:
#     if len(args) != 2:
#         return "Invalid command. Usage: add [ім'я] [номер телефону] або change [ім'я] [старий номер] [новий номер]"
#     try:
#         name, phone = args
#         if not phone.isdigit():
#             return "Invalid phone number. Phone number must contain only 10 digits. Example: add John 1234567890"
#     except ValueError:
#         return "Invalid command. Usage: add [ім'я] [номер телефону] або change [ім'я] [старий номер] [новий номер]"
#     return None

# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError as e:
#             return str(e)
#         except KeyError:
#             return "Contact not found"
#         except IndexError:
#             return "Invalid command. Usage: [command] [ім'я] [номер телефону]"
#     return inner

# @input_error
# def add_contact(args: list, book: AddressBook) -> str:
#     name, phone, *_ = args
#     record = book.find(name)
#     message = "Contact updated."
#     if record is None:
#         record = Record(Name(name))
#         book.add_record(record)
#         message = "Contact added."
#     if phone:
#         record.add_phone(phone)
#     return message

# @input_error
# def change_contact(args: list, book: AddressBook) -> str:
#     name, old_phone, new_phone, *_ = args
#     record = book.find(name)
#     if record:
#         record.edit_phone(old_phone, new_phone)
#         return "Contact updated."
#     else:
#         raise KeyError

# @input_error
# def show_phone(args: list, book: AddressBook) -> str:
#     name, *_ = args
#     record = book.find(name)
#     if record:
#         return "; ".join(str(p.value) for p in record.phones)
#     else:
#         raise KeyError

# @input_error
# def show_all(book: AddressBook) -> str:
#     if not book.data:
#         return "No contacts saved."
#     else:
#         return "\n".join(str(record) for record in book.data.values())

# @input_error
# def add_birthday(args: list, book: AddressBook) -> str:
#     name, birthday, *_ = args
#     record = book.find(name)
#     if record:
#         record.add_birthday(birthday)
#         return "Birthday added."
#     else:
#         raise KeyError

# @input_error
# def show_birthday(args: list, book: AddressBook) -> str:
#     name, *_ = args
#     record = book.find(name)
#     if record and record.birthday:
#         return record.show_birthday()
#     else:
#         raise KeyError

# @input_error
# def birthdays(args: list, book: AddressBook) -> str:
#     return book.get_upcoming_birthdays()
    


from address_book import AddressBook, Record, Name, Phone, Birthday, Email, Address

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Invalid command. Usage: [command] [ім'я] [номер телефону] ..."
    return inner

@input_error
def add_contact(args: list, book: AddressBook) -> str:
    if len(args) < 2:
        return "Invalid command. Usage: add [ім'я] [номер телефону] [email (optional)] [адреса (optional)] [дата народження (DD.MM.YYYY) (optional)]"
    name, phone, *rest = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(Name(name))
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    if rest:
        if len(rest) > 0:
            try:
                record.add_email(rest[0])
                if len(rest) > 1:
                    record.add_address(" ".join(rest[1:-1]) if len(rest) > 2 else rest[1] if len(rest) == 2 else "")
                    if len(rest) > 1:
                        try:
                            record.add_birthday(rest[-1])
                        except ValueError as e:
                            return str(e)
                elif len(rest) == 1:
                    pass # Only email provided
            except ValueError as e:
                return str(e)
        elif len(args) == 3: # name, phone, birthday
            try:
                record.add_birthday(args[2])
            except ValueError as e:
                return str(e)
    return message

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    if len(args) < 3:
        return "Invalid command. Usage: change [ім'я] [старе поле: phone/email/address/birthday] [нове значення]"
    name, field_to_change, new_value, *rest = args
    record = book.find(name)
    if not record:
        raise KeyError
    field_to_change = field_to_change.lower()
    if field_to_change == "phone":
        if len(rest) != 1:
            return "Invalid command. Usage: change [ім'я] phone [старий номер] [новий номер]"
        old_phone = new_value
        new_phone = rest[0]
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    elif field_to_change == "email":
        record.add_email(new_value)
        return "Email updated."
    elif field_to_change == "address":
        record.add_address(new_value)
        return "Address updated."
    elif field_to_change == "birthday":
        try:
            record.add_birthday(new_value)
            return "Birthday updated."
        except ValueError as e:
            return str(e)
    else:
        return "Invalid field to change. Available fields: phone, email, address, birthday"

@input_error
def show_phone(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: phone [ім'я]"
    name, *_ = args
    record = book.find(name)
    if record and record.phones:
        return "; ".join(str(p.value) for p in record.phones)
    elif record:
        return f"Contact {name.capitalize()} has no phone numbers."
    else:
        raise KeyError

@input_error
def show_email(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: email [ім'я]"
    name, *_ = args
    record = book.find(name)
    if record and record.email:
        return record.show_email()
    elif record:
        return f"Contact {name.capitalize()} has no email."
    else:
        raise KeyError

@input_error
def show_address(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: address [ім'я]"
    name, *_ = args
    record = book.find(name)
    if record and record.address:
        return record.show_address()
    elif record:
        return f"Contact {name.capitalize()} has no address."
    else:
        raise KeyError

@input_error
def show_birthday_contact(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: show-birthday [ім'я]"
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return record.show_birthday()
    elif record:
        return f"Contact {name.capitalize()} has no birthday."
    else:
        raise KeyError

def show_all(book: AddressBook) -> str:
    if not book.data:
        return "No contacts saved."
    else:
        return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    if len(args) != 2:
        return "Invalid command. Usage: add-birthday [ім'я] [DD.MM.YYYY]"
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError

@input_error
def birthdays(args: list, book: AddressBook) -> str:
    days = 7
    if args:
        try:
            days = int(args[0])
            if days <= 0:
                return "Number of days must be positive."
        except ValueError:
            return "Invalid number of days."
    return book.get_upcoming_birthdays(days)

@input_error
def find_contact(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: find [ім'я]"
    name = args[0]
    record = book.find(name)
    if record:
        return str(record)
    else:
        return f"Contact '{name.capitalize()}' not found."

@input_error
def delete_contact(args: list, book: AddressBook) -> str:
    if not args:
        return "Invalid command. Usage: delete [ім'я]"
    name = args[0]
    book.delete(name)
    return f"Contact '{name.capitalize()}' deleted."





