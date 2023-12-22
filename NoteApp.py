class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print("Note added successfully.")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            print("Note deleted successfully.")
        else:
            print("Invalid note index.")

    def show_notes(self):
        if self.notes:
            print("Your Notes:")
            for idx, note in enumerate(self.notes, start=1):
                print(f"{idx}. {note}")
        else:
            print("No notes available.")

# Example usage:
note_app = NoteApp()
note_app.show_notes()
note_app.add_note("Remember to buy vegetables")
note_app.add_note("Call Bob tomorrow")
note_app.show_notes()
note_app.delete_note(1)
note_app.show_notes()