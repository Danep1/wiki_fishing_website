import os

def get_file_structure(directory, indent=0):
    structure = ""
    for root, dirs, files in os.walk(directory):
        # Добавляем отступ для текущей директории
        structure += "  " * indent + os.path.basename(root) + "/\n"
        # Добавляем отступ для файлов в текущей директории
        for file in files:
            structure += "  " * (indent + 1) + file + "\n"
        # Рекурсивно обрабатываем поддиректории
        for subdir in dirs:
            structure += get_file_structure(os.path.join(root, subdir), indent + 1)
        break  # Прерываем цикл после обработки текущей директории
    return structure

if __name__ == '__main__':
    print(get_file_structure(r"C:\Users\epikm\PycharmProjects\wiki_fishing_website\wiki_fishing"))
