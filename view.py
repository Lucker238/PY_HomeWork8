

def show_menu() -> int:
    print("\n" + "=" * 40)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    print("=" * 40)
    return int(input("Введите номер необходимого действия: "))

def get_employee_data() -> str:
    return input('Введите имя, фамилию или должность сотрудника: ')

def get_title() -> str:
    return input('Введите должность: ')

def get_salary() -> str:
    print("Введите диапазон зарплаты")
    return [input('От: '), input('До: ')]

def get_new_employee() -> str:
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    job_title = input("Введите должность: ")
    phone_number = input("Введите номер телефона: ")
    salary = input("Введите зарплату: ")
    return f'{last_name},{first_name},{job_title},{phone_number},{salary}'

def get_id_delete() -> str:
    id_delete = input('Введите ID сотрудника для удаления: ')

