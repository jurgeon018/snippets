from random import choice
from urllib.request import urlopen
import json
import requests
import time

def analyze_json_APIs():
    r = requests.get('https://formulae.brew.sh/api/formula.json')
    packages_json = r.json()
    results = []
    for package in packages_json:
        package_name = package['name']
        package_desc = package['desc']

        package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"
        r = requests.get(package_url)
        package_json = r.json()
        installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
        installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
        installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]
        data = {'name':package_name,
                'desc':package_desc,
                'analytics': {'30d': installs_30,
                    '90d':installs_90,
                    '365d':installs_365
                }
        }
        results.append(data)
        print(f'We got {package_name} in {r.elapsed.total_seconds()}')



    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')
    with open('package_info.json', 'w') as f:
        json.dump(results, f, indent=2)
    with open('package_indo.json', 'r') as f:
        data = json.load(f)
    data.sort(key=lambda(package): package['analytics']['30d'], reverse=True)
    data_str = json.dumps(data, indent=2)


analyze_json_APIs()


def corey_ms():
    people_string = """
    {
        "people": [
            {
                "name":"John Smith",
                "phone":"815-555-7164",
                "emails":["jurgen018@gmail.com","jurgen019@gmail.com"],
                "has_license":false
            },
            {
                "name":"Jane Doe",
                "phone":"560-555-5153",
                "emails":null,
                "has_license":true
            }
        ]
    }

    """
    #json.dump(что, куда): python-словарь -> json-файл
    #json.dumps(): python-словарь -> json-строку
    #python_dict = json.load('file.json'): json-файл -> python-словарь
    #json.loads(что, куда): json-строка -> python-словарь

    # loads - превращает json-строку(people_string) в python-словарь(loads)
    loads = json.loads(people_string)

    # dumps - превращает python-словарь(loads) в json-строку(dumps)
    # True-> true, False-> false, None-> null, ' '-> " "
    dumps = json.dumps(loads, indent=4, ensure_ascii=False, sort_keys=True)

    # dump - превращает python-словарь(loads) в json-файл('states.json')
    # True-> true, False-> false, None-> null, ' '-> " "
    with open('states.json', 'w') as f:
        json.dump(loads, f, indent=4, ensure_ascii=False)

    # load - превращает json-файл('states.json') в python-словарь(load)
    with open('states.json') as f:
        load = json.load(f)

    print(loads, '\n', load, '\n', dumps, '\n')

#####################################################
def tceh():
    with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as r:
        source = r.read()
        data = json.loads(source)
        print(json.dumps())

#####################################################
def json_():
    with open('file.txt', 'w') as file:
        json.dump({"c": 0, "b": 0, "a": 0}, file, indent=2)

    x = json.dumps({"c": 0, "b": 0, "a": 0}, 'file.txt', sort_keys=True)
    x  # >>> {"a": 0, "b": 0, "c": 0}

    with open('file.txt', 'w') as file:
        x = json.load(file)

    json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
#####################################################
def oleg_molchanov():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    tel = ''
    name = ''

    while len(tel) != 8 or len(name) != 8:
        tel += choice(nums)
        name += choice(letters)
    person = {'name': name, 'tel': tel}

    for i in range(5):
        try:
            date = json.load(open('persons.json'))
        except:
            date = []
        date.append(persons)
        with open('persons.json', 'w') as file:
            json.dump(date, file, indent=4, ensure_ascii=False)
