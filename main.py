from pprint import pprint
import re




# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# Задание 1
columns_names = contacts_list[0]
contacts_list.pop(0)
for idx, contact in enumerate(contacts_list):
  fio = " ".join(contact[:3])
  fio_list = fio.split(' ')
  fio_list = [elem for n, elem in enumerate(fio_list) if elem not in fio_list[:n]]
  try:
      fio_list.remove('')
  except ValueError:
      pass
  if len(fio_list) == 2:
    fio_list.append('')
  for i in range(3):
    contacts_list[idx][i] = fio_list[i]

# Задание 2
phones_list = []
for contact in contacts_list:
  phones_list.append(contact[-2])
pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?(доб.)?\s*(\d+)?\)?"
pattern_comp = re.compile(pattern)
for idx, phone in enumerate(phones_list):
  phones_list[idx] = pattern_comp.sub(r"+7(\2)\3-\4-\5 \6\7", phone)
  if (phones_list[idx] != '') and (phones_list[idx][-1] == ' '):
    phones_list[idx] = phones_list[idx][:-1]
for idx, contact in enumerate(contacts_list):
    contact[-2] = phones_list[idx]

#Задание 3
checked_indexes = []
unique_indexes = []
for i in range(len(contacts_list)):
    if i not in checked_indexes:
        unique_indexes.append(i)
        checked_indexes.append(i)
        contact = contacts_list[i]
        for j in range(i+1,len(contacts_list)):
            if j not in checked_indexes and contact[0]==contacts_list[j][0] and contact[1]==contacts_list[j][1]:
                next_contact = contacts_list[j]
                checked_indexes.append(j)
                for m in range(2,len(next_contact)):
                    if(contact[m]==''):
                        contact[m] += next_contact[m]
result_contacts_list = []
result_contacts_list.append(columns_names)
for i in unique_indexes:
    result_contacts_list.append(contacts_list[i])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result_contacts_list)
