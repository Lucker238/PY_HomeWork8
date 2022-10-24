Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате txt")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
import csv
import json
from pathlib import Path
def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee

import csv
import json
from pathlib import Path

def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


for employee in employees:
        if employee['id'] == id:
            return employee

def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result
