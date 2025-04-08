# from collections import UserDict
# import re
# from datetime import datetime, timedelta
# from dataclasses import dataclass, field

# @dataclass
# class Field:
#     value: str

#     def __str__(self):
#         return self.value

# @dataclass
# class Name(Field):
#     pass

# @dataclass
# class Phone(Field):
#     def __post_init__(self):
#         if not re.match(r"^\d{10}$", self.value):
#             raise ValueError("Invalid phone number format. Must be 10 digits")

# @dataclass
# class Birthday(Field):
#     def __post_init__(self):
#         try:
#             datetime.strptime(self.value, "%d.%m.%Y")
#         except ValueError:
#             raise ValueError("Invalid date format. Use DD.MM.YYYY")

# @dataclass
# class Record:
#     name: Name
#     phones: list[Phone] = field(default_factory=list)
#     birthday: Birthday = None

#     def add_phone(self, phone_str: str):
#         self.phones.append(Phone(phone_str))

#     def remove_phone(self, phone):
#         if self.phones:
#             self.phones = [p for p in self.phones if p.value != phone]

#     def edit_phone(self, old_phone, new_phone):
#         if self.phones:
#             for p in self.phones:
#                 if p.value == old_phone:
#                     p.value = new_phone
#                     return
#             raise ValueError("Phone number not found")
#         else:
#             raise ValueError("No phone numbers to edit.")

#     def find_phone(self, phone):
#         if self.phones:
#             for p in self.phones:
#                 if p.value == phone:
#                     return p.value
#         return None

#     def add_birthday(self, birthday_str: str):
#         self.birthday = Birthday(birthday_str)

#     def show_birthday(self):
#         if self.birthday:
#             return self.birthday.value
#         return None

#     def __str__(self):
#         phones_str = ";".join(p.value for p in self.phones)
#         birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
#         return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

# class AddressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.value] = record

#     def find(self, name):
#         for record_name, record in self.data.items():
#             if record_name.lower() == name.lower():
#                 return record
#         return None

#     def delete(self, name):
#         for record_name, record in self.data.items():
#             if record_name.lower() == name.lower():
#                 del self.data[record_name]
#                 return
#         raise KeyError("Record not found")

#     def get_upcoming_birthdays(self) -> str:
#         today = datetime.today().date()
#         next_week = today + timedelta(days=7)
#         birthdays_per_week = {i: [] for i in range(5)}

#         for record in self.data.values():
#             if record.birthday:
#                 birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
#                 birthday_this_year = birthday_date.replace(year=today.year)

#                 if today <= birthday_this_year <= next_week:
#                     day_of_week = birthday_this_year.weekday()
#                     if day_of_week >= 5:
#                         day_of_week = 0
#                     birthdays_per_week[day_of_week].append(record.name.value.capitalize()) # зміна

#                 elif birthday_this_year.year == today.year - 1 and today.month == 1 and today.day <= birthday_date.day and birthday_this_year <= next_week:
#                     day_of_week = birthday_this_year.weekday()
#                     if day_of_week >= 5:
#                         day_of_week = 0
#                     birthdays_per_week[day_of_week].append(record.name.value.capitalize()) # зміна

#         days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#         return "\n".join(f"{days_of_week[i]}: {', '.join(names)}"
#                         for i, names in birthdays_per_week.items() if names)





from collections import UserDict
import re
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import os
import pickle

@dataclass
class Field:
    value: str

    def __str__(self):
        return self.value

@dataclass
class Name(Field):
    pass

@dataclass
class Phone(Field):
    def __post_init__(self):
        if not re.match(r"^\d{10}$", self.value):
            raise ValueError("Invalid phone number format. Must be 10 digits")

@dataclass
class Email(Field):
    def __post_init__(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.value):
            raise ValueError("Invalid email format.")

@dataclass
class Address(Field):
    pass

@dataclass
class Birthday(Field):
    def __post_init__(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

@dataclass
class Record:
    name: Name
    phones: list[Phone] = field(default_factory=list)
    email: Email = None
    address: Address = None
    birthday: Birthday = None

    def add_phone(self, phone_str: str):
        self.phones.append(Phone(phone_str))

    def remove_phone(self, phone):
        if self.phones:
            self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if self.phones:
            for p in self.phones:
                if p.value == old_phone:
                    p.value = new_phone
                    return
            raise ValueError("Phone number not found")
        else:
            raise ValueError("No phone numbers to edit.")

    def find_phone(self, phone):
        if self.phones:
            for p in self.phones:
                if p.value == phone:
                    return p.value
        return None

    def add_birthday(self, birthday_str: str):
        self.birthday = Birthday(birthday_str)

    def show_birthday(self):
        if self.birthday:
            return self.birthday.value
        return None

    def add_email(self, email_str: str):
        self.email = Email(email_str)

    def show_email(self):
        if self.email:
            return self.email.value
        return None

    def add_address(self, address_str: str):
        self.address = Address(address_str)

    def show_address(self):
        if self.address:
            return self.address.value
        return None

    def __str__(self):
        phones_str = ";".join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        email_str = f", email: {self.email.value}" if self.email else ""
        address_str = f", address: {self.address.value}" if self.address else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{email_str}{address_str}{birthday_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for record_name, record in self.data.items():
            if record_name.lower() == name.lower():
                return record
        return None

    def delete(self, name):
        for record_name, record in self.data.items():
            if record_name.lower() == name.lower():
                del self.data[record_name]
                return
        raise KeyError("Record not found")

    def get_upcoming_birthdays(self, days: int = 7) -> str:
        today = datetime.today().date()
        future_date = today + timedelta(days=days)
        birthdays_list = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday_date.replace(year=today.year)

                if today <= birthday_this_year <= future_date:
                    birthdays_list.append(f"{record.name.value.capitalize()}: {birthday_this_year.strftime('%d.%m.%Y')}")
                elif birthday_this_year.year == today.year - 1 and today.month == 1 and today.day <= birthday_date.day and birthday_this_year.replace(year=today.year) <= future_date:
                    birthdays_list.append(f"{record.name.value.capitalize()}: {birthday_this_year.replace(year=today.year).strftime('%d.%m.%Y')}")

        if birthdays_list:
            return "Upcoming birthdays:\n" + "\n".join(birthdays_list)
        else:
            return "No upcoming birthdays in the next {} days.".format(days)

class Note:
    def __init__(self, content, tags=None):
        self.content = content
        self.tags = set(tags) if tags else set()

    def add_tag(self, tag):
        self.tags.add(tag.lower())

    def remove_tag(self, tag):
        self.tags.discard(tag.lower())

    def __str__(self):
        tags_str = f" (Tags: {', '.join(sorted(self.tags))})" if self.tags else ""
        return f"{self.content}{tags_str}"

class NoteBook(UserDict):
    def add_note(self, note):
        self.data[id(note)] = note

    def find_note(self, keyword):
        results = []
        keyword_lower = keyword.lower()
        for note in self.data.values():
            if keyword_lower in note.content.lower() or any(keyword_lower == tag for tag in note.tags):
                results.append(note)
        return results

    def edit_note(self, note_id, new_content):
        if note_id in self.data:
            self.data[note_id].content = new_content
            return True
        return False

    def delete_note(self, note_id):
        if note_id in self.data:
            del self.data[note_id]
            return True
        return False

    def search_by_tag(self, tag):
        results = []
        tag_lower = tag.lower()
        for note in self.data.values():
            if tag_lower in note.tags:
                results.append(note)
        return results

    def sort_by_tag(self):
        return sorted(self.data.values(), key=lambda note: sorted(list(note.tags)))

def save_data(address_book, note_book, filename="addressbook.pkl", notes_filename="notebook.pkl"):
    user_dir = os.path.expanduser("~")
    addressbook_path = os.path.join(user_dir, filename)
    notebook_path = os.path.join(user_dir, notes_filename)
    try:
        with open(addressbook_path, "wb") as f:
            pickle.dump(address_book, f)
        with open(notebook_path, "wb") as f:
            pickle.dump(note_book, f)
        print("Дані збережено.")
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")

def load_data(filename="addressbook.pkl", notes_filename="notebook.pkl"):
    user_dir = os.path.expanduser("~")
    addressbook_path = os.path.join(user_dir, filename)
    notebook_path = os.path.join(user_dir, notes_filename)
    book = AddressBook()
    notes = NoteBook()
    try:
        with open(addressbook_path, "rb") as f:
            book = pickle.load(f)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Помилка при завантаженні адресної книги: {e}")

    try:
        with open(notebook_path, "rb") as f:
            notes = pickle.load(f)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Помилка при завантаженні нотаток: {e}")
    return book, notes



