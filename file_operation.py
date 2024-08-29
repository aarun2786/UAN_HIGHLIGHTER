import json
import datetime
import pytz

def create_json():
    data = {"Data":[]}
    with open('Json_data.json', 'a') as file:
        json.dump(data,file)

def update_json(name,page_data,type,filename):
    with open('Json_data.json', 'r') as file:
        data = json.load(file)

    add_data = {'Project_Name': name, "Page": page_data, "Date": time_covert()[0], "Type": type,'Filename': filename}
    data['Data'].append(add_data)

    with open("TEXT.txt", "a") as file:
        file.write(f"{add_data}\n")

    with open('Json_data.json','w') as file:
        json.dump(data, file, indent=6)

def get_json():
    with open('Json_data.json', 'r') as file:
        data = json.load(file)
    return  data['Data'][::-1]


def time_covert():
    utc_zone = pytz.utc
    indian_zone = pytz.timezone('Asia/kolkata')
    utc_now = datetime.datetime.utcnow()
    indian_time = utc_now.replace(tzinfo=utc_zone).astimezone(indian_zone)
    time_format = indian_time.strftime("%d-%m-%Y %I:%M %p")
    return time_format,indian_time.day
