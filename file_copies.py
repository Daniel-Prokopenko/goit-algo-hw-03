import os


def copy_files(old_dir, new_dir):
    try:
        files = os.listdir(old_dir)
    except FileNotFoundError:
        return 'Файл або теку не знайдено.'
    for filename in files:
        if filename != new_dir: # не заходимо у щойно створену папку
            filepath = old_dir + '\\' + filename
        if os.path.isdir(filepath): # перевіряємо чи є директорія папкою
            copy_files(filepath, new_dir)
        else:
            if '.' in filename: # чи наявний формат у файла
                file_format = filename.split('.')[-1]
            else:
                file_format = 'non_defined'
            if not os.path.exists(new_dir + '\\' + file_format):
                try:
                    os.mkdir(new_dir + '\\' + file_format)
                except PermissionError:
                    return 'Неможливо створити нову теку. Недостатньо прав.'
            try:
                with open(new_dir + '\\' + file_format + '\\' + filename, 'wb') as new_file: # робимо читання старого файлу і запис у новий
                    with open(filepath, 'rb') as old_file:
                        new_file.write(old_file.read())
            except PermissionError:
                return 'Недостатньо прав для створення/читання файлу.'
    return 'All done!'
                    

pathlist = input('Введіть шлях до старої та нової директорій: <old\path new\path> ===>  ').split()
old_dir = fr"{pathlist.pop(0)}"

if not pathlist: # перевіряємо чи надано шлях до нової папки
    new_dir = old_dir + '\dist'
    try:
        os.mkdir(new_dir)
        print(copy_files(old_dir, new_dir))
    except PermissionError:
        print('Неможливо створити нову теку. Недостатньо прав.')
else:
    new_dir = pathlist.pop()
    print(copy_files(old_dir, new_dir))
