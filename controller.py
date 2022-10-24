import view as v
import model as m



def lets_start():
    check = True
    while check:
        choice = v.show_menu()
        while not 0 <= choice < 10:
            print('Введите число от 1 до 9')
            choice = v.show_menu()
        match choice:
            case 0:
                employees = m.read_csv()
                m.show_all(employees)
            case 1:
                employees = m.read_csv()
                data = v.get_employee_data()
                m.find_employee(employees, data)
            case 2:
                employees = m.read_csv()
                data = v.get_title()
                m.show_employees_title(employees,data)
            case 3:
                employees = m.read_csv()
                data = v.get_salary()
                m.show_employees_salary(employees,data)
            case 4:
                new_employee = v.get_new_employee()
                m.add_employee(new_employee)
            case 5:
                employees = m.read_csv()
                d_id = v.get_id()
                new_employees = m.delete_employee(employees,d_id)
                m.rewrite_csv(new_employees)
            case 6:
                employees = m.read_csv()
                e_id = v.get_id()
                n_data = v.get_edit_data()
                new_employees = m.edit_employee(employees,e_id,n_data)
                m.rewrite_csv(new_employees)
            case 7:
                employees = m.read_csv()
                m.import_json(employees)
            case 9:
                check = False