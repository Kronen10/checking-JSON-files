import os

def check_empty_json_files(directory):
    empty_files_count = 0
    all_files_count = 0

    # Открываем файл для записи пустых файлов
    with open("empty_json_files.txt", "w", encoding="utf-8") as error_file:
        # Получаем список всех JSON файлов в директории
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                all_files_count += 1
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Читаем первый символ файла
                        first_char = f.read(1)
                        if not first_char:
                            print(f"Файл {filename} пустой.")
                            error_file.write(f"{filename}\n")  # Записываем имя файла в файл с ошибками
                            empty_files_count += 1
                        else:
                            # Если файл не пустой, сбрасываем указатель в начало файла
                            f.seek(0)
                except Exception as e:
                    print(f"Ошибка при обработке файла {filename}: {e}")

    print(f"\nКоличество пустых файлов: {empty_files_count}")
    print(f"Общее количество JSON файлов: {all_files_count}")

# Запрашиваем путь к директории у пользователя
directory_path = input("Введите путь к директории с JSON файлами: ").strip()

# Проверяем, существует ли директория
if os.path.isdir(directory_path):
    check_empty_json_files(directory_path)
else:
    print("Указанная директория не существует. Пожалуйста, проверьте путь.")
