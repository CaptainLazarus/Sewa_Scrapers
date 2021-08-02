import csv
import re

count = 1

emails = []

with open('removed.csv', newline='') as f:
    a = csv.reader(f, delimiter=' ', quotechar='|')
    for row in a:
        for i in row:
            if i.find('@') != -1 :
                emails.append(i)

c_emails = []
REG = '[0-9a-zA-Z_.]+[0-9a-zA-Z_.]+@[0-9a-zA-Z_]+\.[a-zA-Z0-9_]+'
# REG = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# REG = '\S+@\S+'
for i in emails:
    # i.replace("," , "")
# c_i.replace("," , "")
    c_i = re.search(REG, i)
    if c_i:
        c_emails.append(c_i.group(0))
    # print(c_i)
    # if re.search(REG, i):
        # c_i = re.search(REG, i).group(1)
    # c_emails.append(c_i)

# for i in c_emails:
#     print(i)


with open('removed.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(c_emails)
