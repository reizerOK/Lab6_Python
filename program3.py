import json

def main():
    students_data = {
        "Коваленко": ["Олександр", "Петрович", 2004],
        "Шевченко": ["Марія", "Іванівна", 2005],
        "Бойко": ["Дмитро", "Сергійович", 2004],
        "Лисенко": ["Анна", "Миколаївна", 2006],
        "Ткаченко": ["Віктор", "Олексійович", 2003],
        "Кравченко": ["Олена", "Володимирівна", 2005],
        "Мельник": ["Андрій", "Васильович", 2004],
        "Олійник": ["Юлія", "Тарасівна", 2006],
        "Поліщук": ["Максим", "Ігорович", 2004],
        "Григоренко": ["Наталія", "Михайлівна", 2005],
        "Іщенко": ["Денис", "Андрійович", 2006]
    }

    filename = "students.json"

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(students_data, json_file, ensure_ascii=False, indent=4)
    print(f"Дані успішно записано у файл {filename}.")

    print("\nЧитання даних з файлу:\n")
    with open(filename, 'r', encoding='utf-8') as json_file:
        loaded_data = json.load(json_file)

    for surname, details in loaded_data.items():
        name, patronymic, year = details
        print(f"Прізвище: {surname:12} | Ім'я: {name:10} | По батькові: {patronymic:15} | Рік народження: {year}")

if __name__ == "__main__":
    main()
