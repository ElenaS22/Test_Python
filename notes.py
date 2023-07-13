import json
import os
import datetime


class Note:
    def __init__(self, note_id, title, body, created_at, updated_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at


class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(note_data['note_id'], note_data['title'], note_data['body'],
                                note_data['created_at'], note_data['updated_at'])
                    self.notes.append(note)

    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'created_at': note.created_at,
                'updated_at': note.updated_at
            }
            data.append(note_data)

        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def create_note_id(self):
        if len(self.notes) == 0:
            return 1
        else:
            return self.notes[-1].note_id + 1

    def create_note(self, title, body):
        note_id = self.create_note_id()
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = created_at
        note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes()
        print(f"Запись с ID {note_id} успешно создана.")

    def read_notes(self):
        if len(self.notes) == 0:
            print("Запись не найдена.")
        else:
            for note in self.notes:
                print(f"ID: {note.note_id}")
                print(f"Наименование: {note.title}")
                print(f"Содержание: {note.body}")
                print(f"Создана запись: {note.created_at}")
                print(f"Обновлена запись: {note.updated_at}")
                print("--------------------")

    def read_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"ID: {note.note_id}")
                print(f"Наименование: {note.title}")
                print(f"Содержание: {note.body}")
                print(f"Создана запись: {note.created_at}")
                print(f"Обновлена запись: {note.updated_at}")
                return

        print(f"С указанным ID {note_id} не найдено ни одной записи.")

    def update_note_by_id(self, note_id, title, body):
        updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.updated_at = updated_at
                self.save_notes()
                print(f"Запись с ID {note_id} успешно обновлена.")
                return

        print(f"С указанным ID {note_id} не найдено ни одной записи.")

    def delete_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print(f"Запись с ID {note_id} успешно удалена.")
                return

        print(f"С указанным ID {note_id} не найдено ни одной записи.")


# Пример использования
note_manager = NoteManager('notes.json')

while True:
    print("Меню:")
    print("1. Создание записи")
    print("2. Прочитать все записи")
    print("3. Найти запись по ID")
    print("4. Обновить запись")
    print("5. Удалить запись")
    print("0. Выход")

    choice = input("Укажите цифру в соответствии с Ваши выбором: ")

    if choice == "1":
        title = input("Введите название записи: ")
        body = input("Введите текст, который будет содержать запись: ")
        note_manager.create_note(title, body)
    elif choice == "2":
        note_manager.read_notes()
    elif choice == "3":
        note_id = int(input("Введите ID записи: "))
        note_manager.read_note_by_id(note_id)
    elif choice == "4":
        note_id = int(input("Введите ID записи: "))
        title = input("Введите новое наименование записи: ")
        body = input("Введите новый текст, который будет содержать запись: ")
        note_manager.update_note_by_id(note_id, title, body)
    elif choice == "5":
        note_id = int(input("Введите ID записи: "))
        note_manager.delete_note_by_id(note_id)
    elif choice == "0":
        break
    else:
        print("Введено некорректное значение, попробуйте еще раз.")