from sotrudniki import Manager

def main():
    name = input('Введите имя сотрудника:') 
    position = float(input('Введите на каком месте сотрудник:'))
    salary = float(input('Введите тарифную ставку:'))
    department = input('Введите отдел:')
    num_employees = int(input('Введите количество сотрудников в отделе:'))
    manager = Manager(name, position,  salary, department, num_employees)
    manager.info()
    worked_days = int(input('Введите количество проработанных дней:'))
    money_1 = manager.calc_salary(worked_days)
    print('Зарплата сотрудника:', money_1)
if __name__ == '__main__':
    main()
