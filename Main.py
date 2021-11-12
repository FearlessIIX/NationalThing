def main():
    employee_directory()


def employee_directory():
    # TODO implement the process of getting values from storage
    employee_dir = {}
    while True:
        command = input(f"{print_menu()}\n")
        # lookup
        if command == "1":
            lookup_employee()
        # add
        elif command == "2":
            add_employee()
        # change
        elif command == "3":
            pass
        # delete
        elif command == "4":
            pass
        # quit
        elif command == "5":
            pickle(employee_dir)


def print_menu():
    return ("Type the number for your desired action\n"
            " 1) Look Up Employee. 2) Add New Employee. \n"
            " 3) Change Existing Employees Information. 4) Delete An Employee\n"
            " 5) Quit The Program")


def lookup_employee():
    pass


def change_employee():
    pass


def delete_employee():
    pass


def add_employee():
    pass


# TODO implement the pickling process
def pickle(employees):
    pass


class Employee:
    _name = ""
    _ID = ""
    _department = ""
    job_title = ""

    def __init__(self, eid, name, department, title):
        self._ID = eid
        self._name = name
        self._department = department
        self.job_title = title

    def get_name(self): return self._name

    def get_id(self): return self._ID

    def get_department(self): return self._department

    def get_job_title(self): return self.job_title

    def change_name(self, new_name):
        self._name = new_name

    def change_job_title(self, new_title):
        self.job_title = new_title

    def change_department(self, new_department):
        self._department = new_department


if __name__ == "__main__":
    main()
