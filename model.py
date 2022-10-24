
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
        if emp_data in employee.values():
            print(employee)
            continue

def show_employees_title(emp_list: list, title: str):
    for employee in emp_list:
        if title.lower() in employee["Должность"].lower():
            print(employee)

def show_employees_salary(emp_list: list, salary: list):
    for employee in emp_list:
        if salary[0] <= float(employee["Зарплата"]) <= salary[1]:
            print(employee)

def add_employee(emp_data: str):
    with open('database.csv', 'a') as file:
        file.write(f'{emp_data}\n')

def delete_employee(emp_list: list, delete_id: str) -> list:
    for employee in emp_list:
        if employee['ID'] == delete_id:
            print(f'{employee}\nДанные удалены')
            emp_list.remove(employee)
    return emp_list

def edit_employee(emp_list: list, edit_id: str, new_data: list) -> list:
    for i in emp_list:
        if i['ID'] == edit_id:
            print(i)
            i["Должность"] = new_data[0]
            i["Номер телефона"] = new_data[1]
            i["Зарплата"] = new_data[2]       
    return emp_list

def rewrite_csv(emp_list: list):
    file = open('database.csv', 'w')
    for emp in emp_list:
        line = ''
        for k,v in emp.items():
            if k == 'ID':
                continue
            line += v + ','
        file.write(f'{line[:-1]}\n')
    file.close()

def show_all(data: list):
    for i in data:
        for k,v in i.items():
            print(f"{k}: {v}", end='; ')
        print()

def import_json(emp_list: list):
    file = open('database.json','w')
    for i in emp_list:
        for k,v in i.items():
            file.write(f'{k}: {v}; ')
        file.write(f'\n')

def import_txt(emp_list: list):
    file = open('database.txt','w')
    for i in emp_list:
        for k,v in i.items():
            file.write(f'{k}: {v}; ')
        file.write(f'\n')