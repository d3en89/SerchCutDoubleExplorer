import os
import time
import shutil

##

## Каталог где будут просматриваться подпапки на дубли
path_search = "...."
## Каталог куда будут перемещены дубли
path_out = "...."
### Лог файл
path_log = "...."

def create_massiv_double_path(arg):

    first_path = list(os.walk(arg))[0][1]
    for first_level in first_path:
        last_name_sec = ""
        secondary_path = os.listdir(f'{arg}\\{first_level}')
        for secondary_level in secondary_path:
            #### фиксируем дату и полный путь каталога
            full_path = f'{arg}\\{first_level}'
            #############
            ### Сравниваем наименования
            good_count = 0
            if len(last_name_sec) != 0 :
                if len(secondary_level) < len(last_name_sec):
                    check_string = secondary_level
                    two_check_string = last_name_sec
                else:
                    check_string = last_name_sec
                    two_check_string = secondary_level


                for symb in range(len(check_string)):
                    if check_string[symb] == two_check_string[symb]:
                        good_count += 1

                if good_count == len(check_string):
                    edit_time_s = time.gmtime(os.path.getctime(f'{arg}\\{first_level}\\{last_name_sec}'))
                    tm_s = int(f'{edit_time_s.tm_year}{edit_time_s.tm_mon}{edit_time_s.tm_mday}')
                    edit_time_f = time.gmtime(os.path.getmtime(f'{arg}\\{first_level}\\{secondary_level}'))
                    tm_f = int(f'{edit_time_f.tm_year}{edit_time_f.tm_mon}{edit_time_f.tm_mday}')
                    with open(path_log, 'a+') as f:
                        if tm_f <= tm_s:
                            f.write(f'{arg}\\{first_level}\\{secondary_level}\n')
                            shutil.move(f'{arg}\\{first_level}\\{secondary_level}', f'{path_out}\\{secondary_level}', copy_function=shutil.copytree)
                        else:
                            f.write(f'{arg}\\{first_level}\\{last_name_sec}')
                            shutil.move(f'{arg}\\{first_level}\\{last_name_sec}', f'{path_out}\\{last_name_sec}',
                                    copy_function=shutil.copytree)
                        f.close()
            #############
            last_name_sec = secondary_level


if __name__ == "__main__":
    create_massiv_double_path(path_search)