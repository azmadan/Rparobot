import os
from data import general_data
from work_with_entera import login_in_entera, load_file_in_entera


def check_files():
    files = os.listdir(general_data['path_to_scan'])
    if files:
        general_data['path_to_files'] = os.path.join(general_data['path_to_scan']+files[0])
        print(general_data['path_to_files'])
    else:
        print('Фаил отсутсвует')


check_files()

# login_in_entera()
# load_file_in_entera()