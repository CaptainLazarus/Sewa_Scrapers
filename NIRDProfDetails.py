from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

URL = "http://nirdpr.org.in/people.aspx"
PAGE = urlopen(URL)
soup = BeautifulSoup(PAGE, "html.parser")
tables = soup.find_all("tbody")

data = []
edu = []
phone = []
email = []
for i in tables:
    rows = i.find_all("tr")
    rows = rows[1:4]
    e1 = rows[0].text.replace("Areas of Specialisation" , "").strip()
    e1 = e1.replace(":" , "").strip()
    e1 = e1.replace(";" , ",").strip()
    e1 = e1.replace("\n" , "").strip()
    e1 = e1.replace("\r" , "").strip()
    e1 = e1.replace("                                          " , "").strip()
    # print(e1)
    ph = rows[1].text.replace("Email" , "").strip()
    ph = ph.replace(":" , "").strip()
    ph = ph.replace("\n" , "").strip()
    ph = ph.replace("\r" , "").strip()
    ph = ph.replace("[at]" , "@").strip()

    em = rows[2].text.replace("Phone" , "").strip()
    em = em.replace(":" , "").strip()
    em = em.replace("\n" , "").strip()
    em = em.replace("\r" , "").strip()

    edu.append(e1)
    email.append(ph)
    phone.append(em)
    # email.append(em)
print(edu)
print(email)
print(phone)

f = open('2.csv', 'w')
writer = csv.writer(f)
writer.writerow(edu)
writer.writerow(email)
writer.writerow(phone)
f.close()
