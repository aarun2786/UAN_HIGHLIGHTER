import json
import datetime


def create_json():
    data = {"Data":[]}
    with open('Json_data.json', 'a') as file:
        json.dump(data,file)

def update_json(name,page_data,type,filename):
    with open('Json_data.json', 'r') as file:
        data = json.load(file)

    add_data = {'Project_Name': name, "Page": page_data, "Date": datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p"), "Type": type,'Filename': filename}
    data['Data'].append(add_data)

    with open("TEXT.txt", "a") as file:
        file.write(f"{add_data}\n")

    with open('Json_data.json','w') as file:
        json.dump(data, file, indent=6)

def get_json():
    with open('Json_data.json', 'r') as file:
        data = json.load(file)
    return  data['Data'][::-1]







