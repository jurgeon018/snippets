########################################################
# Corey Schafer - CSV Module
from csv import writer
from collections import Counter
import re
import csv

with open('test.csv', 'r') as rf:
    for line in csv.reader(rf):
        print(line)
    for line in csv.DictReader(rf):
        print(line)
    with open('new_names.csv', 'w') as wf:
        for line in csv.reader(rf):
            csv.writer(wf, delimiter='\t').writerow(line)
        csv.DictWriter(wf, fieldnames=['IP', 'Amosunt'], delimiter='\t').writeheader()
        for line in csv.reader(rf):
            csv.DictWriter(wf, fieldnames=['IP', 'Amosunt'], delimiter='\t').writerow()
########################################################
# Corey Schafer - Real World Example - Parsing Names From a CSV to an HTML List


html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    # We don't want first line of bad data
    # next(csv_data)
    for line in csv_data:
        # if line['FirstName'] == 'No Reward':
            # break
        names.append(f"{line['FirstName']} {line['LastName']}")

# html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
# html_output += '\n<ul>'
for name in names:
    html_output += f'\n\t<li>{name}</li>'
# html_output += '\n</ul>'
print(html_output)

# with open('ht.html', 'w') as f:
#     f.write(html_output)

########################################################
# Олег Молчанов - парсер логов сервера
with open('/home/jurgeon/Desktop/dev/molchanov/apache_log_parser/test.log', 'r') as f:
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips_list = re.findall(pattern, f.read())
with open('output.csv', 'w') as f:
    count = Counter(ips_list)
    writer = csv.writer(f, delimiter=':')
    writer.writerow(['IP', 'Amount'])
    for i in count:
        writer = csv.writer(f, delimiter=':')
        writer.writerow((i, count[i]))
