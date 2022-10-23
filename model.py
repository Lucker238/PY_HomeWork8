    # print("1. Найти сотрудника")
    # print("2. Сделать выборку сотрудников по должности")
    # print("3. Сделать выборку сотрудников по зарплате")
    # print("4. Добавить сотрудника")
    # print("5. Удалить сотрудника")
    # print("6. Обновить данные сотрудника")
    # print("7. Экспортировать данные в формате json")
    # print("8. Экспортировать данные в формате cmv")
    # print("9. Закончить работу")

def read_csv() -> list:
    file = open('database.csv', 'r')
    data = []
    counter = 0
    headings = ["ID", "Фамилия", "Имя", "Должность", "Номер телефона", "Зарплата"]
    for line in file:
        counter += 1
        line = str(counter) + ',' + line
        data.append(dict(zip(headings,line[:-1].split(','))))
    return data

def find_employee(emp_list: list, emp_data: str):
    for employee in emp_list:
        for k, v in employee.items():
            if emp_data.lower() in v.lower():
                print(employee)
                break

def show_employees_title(emp_list: list, title: str):
    for employee in emp_list:
        if title.lower() in employee["Должность"].lower():
            print(employee)

def show_employees_salary(emp_list: list, salary: str):
    for employee in emp_list:
        if salary in employee["Зарплата"]:
            print(employee)

def add_employee(emp_data: str):
    with open('database.csv', 'a') as file:
        file.write(emp_data)

def delete_employee(emp_list: list, delete_id: str):
    for employee in emp_list:
        for k,v in employee.items():
            if delete_id == v:
                emp_list.remove(employee)
    file = open('database.csv', 'w')
    for emp in emp_list:
        line = ''
        for k,v in emp.items():
            if k == 'ID':
                continue
            line += v + ','
        file.write(f'{line[:-1]}\n')
delete_employee(read_csv(),input())

