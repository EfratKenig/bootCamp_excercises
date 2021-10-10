from Office import Office


def main():
    # create an office
    office = Office([], [], [])
    # 	hire 3 managers and cleaners to the office
    for i in range(3):
        office.hire_manager('manager' + str(i))
        office.hire_cleaner('cleaner' + str(i))
    # each manager should hire 2 clerks
    for m in range(len(office.managers)):
        office.managers[m].hire_employee("clerk" + str(m+1))
        office.managers[m].hire_employee("clerk" + str(m+1) + 'a')

    office.start_work_day()


if __name__ == '__main__':
    main()
