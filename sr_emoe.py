# запись в json файл
import json

s = {
    "name": "Barsik",
    "age": 7,
    "meals": [
        "Wiskas",
        "Royal Canin",
        "Purina",
        "Hills",
        "Brit Care"
    ]
}

with open('js.json', mode='w') as js_file:
    json.dump(s, js_file, indent=2, ensure_ascii=True)


















# получить словарь из js файла
import json

with open('js.json') as js_file:
    print(json.load(js_file))

# result:
# {
#     "name": "Barsik",
#     "age": 7,
#     "meals": [
#         "Wiskas",
#         "Royal Canin",
#         "Purina",
#         "Hills",
#         "Brit Care"
#     ]
# }











# из строки сделать словарь
import json

s = '''{
    "name": "Barsik",
    "age": 7,
    "meals": [
        "Wiskas",
        "Royal Canin",
        "Purina",
        "Hills",
        "Brit Care"
    ]
} '''
e = json.loads(s)
print(e)
#result: {'name': 'Barsik', 'age': 7, 'meals': ['Wiskas', 'Royal Canin', 'Purina', 'Hills', 'Brit Care']}

































































































#1 задачка
import csv
import json

with open('houses.csv', encoding="utf8") as csvfile:
    data = []
    reader = list(csv.reader(csvfile, delimiter=';'))
    for elem in reader[1:]:
        if elem[-3] != elem[-2]:
            address = elem[1]
            difference = abs(int(elem[2]) - int(elem[3]))
            data.append({'address': address, 'difference': difference})

with open('unusual.json', mode='w') as wr_file:
    json.dump(data, wr_file, ensure_ascii=True, indent=2)



#2 задача
import json
import requests


def check(colors, check_string):
    for elem in colors:
        if elem not in check_string:
            return False
    return True


with open('bouquet.json', mode='r') as file:
    data = json.load(file)
    host = data['host']
    port = data['port']
    color = data['color'].split(', ')

    zapr = f'http://{host}:{port}'
    get_res = requests.get(zapr).json()

    print_info = []
    for key in get_res:
        if check(color, get_res[key]):
            print_info.append(key)
    print(", ".join(sorted(print_info, reverse=True)))



#3 задача
import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
parser.add_argument('dela', nargs='*')
parser.add_argument('--cut', type=int, default=4)
parser.add_argument('--rest', action='store', type=int)

args = parser.parse_args()

zapr = f"http://{args.host}:{args.port}"
get_info = requests.get(zapr).json()

for key in get_info:
    val = get_info[key]
    for i in range(len(val)):
        if key in args.dela:
            if val[i] % args.cut == 0:
                val[i] = int(str(val[i])[0:-1])
            elif args.rest is not None:
                if val[i] % args.rest != 0:
                    val[i] += val[i] % 5 + val[i] % 7
    get_info[key] = val

data = []
for key in get_info:
    s = {}
    s['job'] = key
    s['diff'] = max(get_info[key]) - min(get_info[key])
    cred = sum(get_info[key]) / len(get_info[key])
    s['number'] = len(list(filter(lambda x: x > cred, get_info[key])))
    data.append(s)

data = sorted(data, key=lambda d: d['job'])

with open('good_day.json', mode='w') as file:
    json.dump(data, file, indent=2, ensure_ascii=True)


#чародей+цветы будущего


#3 фиксы

import argparse
import pprint

import requests
import json


parser = argparse.ArgumentParser()

parser.add_argument('host')
parser.add_argument('port')

parser.add_argument('argv', nargs='*')

parser.add_argument('--cut', default=4, type=int)
parser.add_argument('--rest', action='store')

args = parser.parse_args()

# respounse = requests.get(f'http://{args.host}:{args.port}')
# json_response = response.json()
json_response = {
    "walk": [211, 197, 243],
    "read": [235, 108, 121, 45],
    "clean": [22, 212, 111],
    "listen": [294, 179, 106]
}


lst = []
for key, value in json_response.items():
    lst_value = value
    for i in range(len(value)):
        if lst_value[i] % args.cut:
            lst_value[i] = lst_value[i] // 10
        elif args.rest == None:
            if lst_value[i] % args.rest == 0:
                lst_value[i] = lst_value[i] + lst_value[i] % 5 + lst_value[i] % 7
    job = key
    diff = max(lst_value) - min(lst_value)
    number = sum(sorted(lst_value)[len(lst_value) // 2:])

    lst.append({"job": job, "diff": diff, "number": number})

lst = sorted(lst, key=lambda d: d['job'])
pprint.pprint(lst)
with open("good_day.json", "w") as f:
    json.dump(lst, f)


