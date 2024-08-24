import os

def check_file_pairs(directory):
    jpg_files = []
    json_files = []
    missing_pairs = []

    # Получаем список всех файлов в директории
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            jpg_files.append(filename)
        elif filename.endswith('.json'):
            json_files.append(filename)

    # Сравниваем списки и находим файлы без пар
    for jpg_file in jpg_files:
        json_file = jpg_file[:-4] + ".json"
        if json_file not in json_files:
            missing_pairs.append(jpg_file)

    for json_file in json_files:
        jpg_file = json_file[:-5] + ".jpg"
        if jpg_file not in jpg_files:
            missing_pairs.append(json_file)

    # Выводим информацию о количестве файлов
    print(f"Количество JPG файлов: {len(jpg_files)}")
    print(f"Количество JSON файлов: {len(json_files)}")

    # Записываем в файл имена файлов без пар
    if missing_pairs:
        with open("missing_pairs.txt", "w", encoding="utf-8") as error_file:
            for file in missing_pairs:
                error_file.write(f"{file}\n")
        print(f"Файлы без пар записаны в файл missing_pairs.txt")
    else:
        print("Все файлы имеют одноименную пару.")

# Запрашиваем путь к директории у пользователя
directory_path = input("Введите путь к директории: ").strip()

# Проверяем, существует ли директория
if os.path.isdir(directory_path):
    check_file_pairs(directory_path)
else:
    print("Указанная директория не существует. Пожалуйста, проверьте путь.")
