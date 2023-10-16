# Напишите функцию группового переименования файлов. Она должна:
#- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#- принимать параметр количество цифр в порядковом номере.
#- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#- принимать параметр расширение конечного файла.
#- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os

def group_rename_files(source_dir, desired_name, num_digits, source_extension, target_extension, name_range=None):
    if name_range is None:
        name_range = (0, 0)

    
    files = os.listdir(source_dir)

    files = [file for file in files if file.endswith(source_extension)]

    files.sort()

    count = name_range[0]

    for file in files:
       
        file_name, file_ext = os.path.splitext(file)

        
        truncated_name = file_name[name_range[0]:name_range[1]]

        
        new_name = f"{truncated_name}_{desired_name}_{count:0{num_digits}d}.{target_extension}"

        
        old_file_path = os.path.join(source_dir, file)
        new_file_path = os.path.join(source_dir, new_name)

        
        os.rename(old_file_path, new_file_path)

        
        count += 1

source_directory = "C:\\Users\\iriba\\Desktop\\Home_works_python\\homework_python7"
 
desired_name = "new"  
num_digits = 2  
source_extension = ".txt"  
target_extension = "md" 
name_range = (3, 6)  

group_rename_files(source_directory, desired_name, num_digits, source_extension, target_extension, name_range)
