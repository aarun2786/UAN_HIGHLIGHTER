import datetime
import os
import time
from file_operation import *
def restart_file():
    path = r"static/PDF"
    files = os.listdir(path)

    for file in files:
        file_delete = f"{path}/{file}"
        os.remove(file_delete)

    os.remove('Json_data.json')
    create_json()

days = datetime.datetime.now().day

if days == 19 :
    print('True')
    restart_file()

