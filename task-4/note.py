
from address_book import NoteBook, Note

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Note not found"
        except IndexError:
            return "Invalid command."
    return inner

@input_error
def add_note_cmd(args: list, notebook: NoteBook) -> str:
    if not args:
        return "Invalid command. Usage: add-note [текст нотатки] [--tag тег1 --tag тег2 ...]"
    content_parts = []
    tags = []
    i = 0
    while i < len(args):
        if args[i] == "--tag":
            if i + 1 < len(args):
                tags.append(args[i + 1])
                i += 2
            else:
                return "Missing tag value after --tag"
        else:
            content_parts.append(args[i])
            i += 1
    if not content_parts:
        return "Note content cannot be empty."
    note = Note(" ".join(content_parts), tags)
    notebook.add_note(note)
    return "Note added."

@input_error
def find_note_cmd(args: list, notebook: NoteBook) -> str:
    if not args:
        return "Invalid command. Usage: find-note [ключове слово]"
    keyword = args[0]
    results = notebook.find_note(keyword)
    if results:
        return "Found notes:\n" + "\n".join(map(str, results))
    else:
        return f"No notes found containing '{keyword}'."

@input_error
def edit_note_cmd(args: list, notebook: NoteBook) -> str:
    if len(args) < 2:
        return "Invalid command. Usage: edit-note [id нотатки] [новий текст]"
    try:
        note_id = int(args[0])
        new_content = " ".join(args[1:])
        if notebook.edit_note(note_id, new_content):
            return f"Note with id {note_id} updated."
        else:
            raise KeyError
    except ValueError:
        return "Note ID must be an integer."

@input_error
def delete_note_cmd(args: list, notebook: NoteBook) -> str:
    if not args:
        return "Invalid command. Usage: delete-note [id нотатки]"
    try:
        note_id = int(args[0])
        if notebook.delete_note(note_id):
            return f"Note with id {note_id} deleted."
        else:
            raise KeyError
    except ValueError:
        return "Note ID must be an integer."

@input_error
def search_note_by_tag_cmd(args: list, notebook: NoteBook) -> str:
    if not args:
        return "Invalid command. Usage: search-tag [тег]"
    tag = args[0]
    results = notebook.search_by_tag(tag)
    if results:
        return f"Notes with tag '{tag}':\n" + "\n".join(map(str, results))
    else:
        return f"No notes found with tag '{tag}'."

@input_error
def sort_notes_by_tag_cmd(args: list, notebook: NoteBook) -> str:
    sorted_notes = notebook.sort_by_tag()
    if sorted_notes:
        return "Notes sorted by tag:\n" + "\n".join(map(str, sorted_notes))
    else:
        return "No notes to sort."