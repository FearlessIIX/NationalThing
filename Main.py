from os.path import exists


def main():
    employee_directory()


def employee_directory():
    employee_dir = {}
    employee_dir = unpickle(employee_dir)
    while True:
        command = input(f"{print_menu()} > ")
        # Match-Case for command control flow
        match command:
            case "1":
                (employee, status) = lookup_employee(employee_dir)
                print("")
                # if the employee was returned successfully
                if status:
                    print(employee)
                    print("")
            case "2":
                add_employee(employee_dir)
                print("")
            case "3":
                change_employee(employee_dir)
                print("")
            case "4":
                delete_employee(employee_dir)
                print("")
            case "5":
                exit_employee_directory(employee_dir)
            # when chosen command is not a number from One to Five
            case _:
                print(f"Command '{command}' is invalid!\n")


def print_menu():
    return ("Type the number for your desired action\n"
            " 1) Look Up Employee. 2) Add New Employee. \n"
            " 3) Change Existing Employees Information\n 4) Delete An Employee."
            " 5) Quit The Program\n")


# <lookup_employee> arguments: <e_dir> Employee Dict, <mode> used internally to change functionality,
# <target_id> used internally to specify pre-destined employee ID target
# Returns a tuple containing An Employee<empty if not found>, and the success-state<if employee was found>
def lookup_employee(e_dir, mode=True, target_id=""):
    # Used to control whether the function prints, for internal use only
    if mode:
        print(" --- Employee Lookup --- ")
    # When <e_dir> is empty: Automatically returns an empty Employee and the success-state (False)
    if len(e_dir) == 0:
        if mode:
            print("Employee Directory is currently empty")
        return Employee(), False
    # Loops until user either exits or enters a valid Employee ID
    while True:
        # Used to control whether the function prints, for internal use only
        if mode:
            target_id = input("Enter the ID of the employee you want to lookup. Enter 'quit' to exit Employee Lookup: ")
            # Quits the validation loop when user enters 'quit'. Returns with an empty Employee and-
            # the success-state (False)
            if target_id == "quit":
                return Employee(), False
        # Goes over all keys in the <e_dir> Dict
        for key in e_dir:
            # When the key matches <target_id>: returns the target Employee and the success-state (True)
            if target_id == key:
                return e_dir[target_id], True
        # Used to control whether the function prints, for internal use only
        if mode:
            print("Employee Not found, check the ID you entered, or type 'quit' to exit Employee Lookup\n")
        # When not printing, Return an empty Employee, and the success-state (False). For internal use only
        else:
            return Employee(), False


# <add_employee> parameters: <e_dir> Employee Dict
# Return Value: Unused/Ignored
def add_employee(e_dir):
    print(" --- Add Employee --- ")
    # Loops until user either exits or enters a Non-Used Employee ID
    while True:
        eid = input("Enter the employees ID, enter 'quit' to exit Add Employee: ")
        # Exits function when user types exit
        if eid == "exit":
            return None
        # Verifies that chosen Employee ID is entirely numeric
        if not eid.isnumeric():
            print("Employee ID must be numeric")
        # Skips next verification step when <e_dir> is empty
        elif len(e_dir) == 0:
            break
        # Verifies that chosen Employee ID isn't taken by attempting to lookup chosen ID
        else:
            (_, status) = lookup_employee(e_dir, False, eid)
            # When Employee Lookup is successful
            if status:
                print("There is already an Employee with that ID, assign a different ID")
            else:
                break
    # Getting the rest of the Employee information, then creating the Employee
    # All values here are validated against the symbol ':'
    while True:
        ename = input("Enter the Employees Name: ")
        if ename.__contains__(":"):
            print("You may not use this symbol in the name!")
        else:
            break
    while True:
        edept = input("Enter the Employees Department: ")
        if edept.__contains__(":"):
            print("You may not use this symbol in the department!")
        else:
            break
    while True:
        etitle = input("Enter the Employees Job Title: ")
        if edept.__contains__(":"):
            print("You may not use this symbol in the job title!")
        else:
            break

    e_dir[eid] = Employee(eid, ename, edept, etitle)


def change_employee(e_dir):
    print(" --- Change Employee Info --- ")
    # Returns if Employee Directory is empty
    if len(e_dir) == 0:
        print("Employee Directory is currently empty")
        return None
    # Loops until user enters valid Employee ID, or enters 'quit'
    while True:
        eid = input("Enter the Employees ID, enter 'quit' to exit Change Employee Info: ")
        if eid == "quit":
            return None
        # Verifies chosen ID is entirely numeric
        elif not eid.isnumeric():
            print("Invalid Employee ID, all Employee IDs are numeric")
        # Verifies that Employee exists
        else:
            (employee, status) = lookup_employee(e_dir, False, eid)
            if status:
                break
            else:
                print("Employee doesn't exist!")
    (eid, name, _, _) = employee.get_all()
    print(f"Changing Employee {eid}: {name}")
    # Changing all aspects of Employee, option to press enter without any value to keep that property the same
    while True:
        ename = input("Enter the Employees new Name, or just press enter to keep the old name: ")
        if not ename == "":
            if ename.__contains__(":"):
                print("You may not use this symbol in the name!")
            else:
                employee.change_name(ename)
            break
        else:
            break
    while True:
        edept = input("Enter the Employees new Department, or just press enter to keep the old Department: ")
        if not edept == "":
            if edept.__contains__(":"):
                print("You may not use this symbol in the department!")
            else:
                employee.change_department(edept)
                break
        else:
            break
    while True:
        etitle = input("Enter the Employees new Job Title, or just press enter to keep the old Job Title: ")
        if not etitle == "":
            if etitle.__contains__(":"):
                print("You may not use this symbol in the job title!")
            else:
                employee.change_job_title(etitle)
                break
        else:
            break

    e_dir[eid] = employee


# <delete_employee> parameters: <e_dir> Employee Dict
# Return Value: Unused/Ignored
def delete_employee(e_dir):
    print(" --- Delete Employee --- ")
    # Exits function if Employee Directory is empty
    if len(e_dir) == 0:
        print("Employee Directory is currently empty")
        return None
    # Loops until user enters an existing Employee ID, or enters 'quit'
    while True:
        eid = input("Enter the Employees ID, enter 'quit' to exit Delete Employee: ")
        if eid == "exit":
            return None
        # Verifies eid is entirely numeric
        elif not eid.isnumeric():
            print("Invalid Employee ID, all Employee IDs are numeric")
        # Verifies an Employee with <eid> exists
        else:
            (_, status) = lookup_employee(e_dir, False, eid)
            if status:
                break
            else:
                print("Employee doesn't exist!")

    e_dir.pop(eid)


def exit_employee_directory(employee_dir):
    pickle(employee_dir)
    exit(0)


def pickle(employees):
    outfile = open("./employeeDirectoryStorage.txt", "w")

    for key in employees:
        employee = employees[key]
        (eid, name, dept, title) = employee.get_all()
        outfile.write(
            f"{eid}:{name}:{dept}:{title}\n"
        )
    outfile.close()


def unpickle(employee_dir):
    if exists("./employeeDirectoryStorage.txt"):
        infile = open("./employeeDirectoryStorage.txt", "r")
        contents = infile.readlines()
        for line in contents:
            (employee, eid) = create_employee(line)
            employee_dir[eid] = employee
        return employee_dir
    else:
        return {}


def create_employee(line=None, mode=1):
    properties = line.split(":")
    return Employee(properties[0], properties[1], properties[2], properties[3]), properties[0]


class Employee:
    _name = ""
    _ID = ""
    _department = ""
    job_title = ""

    def __init__(self, eid="", name="", department="", title=""):
        self._ID = eid
        self._name = name
        self._department = department
        self.job_title = title

    def __repr__(self):
        return (f"Employee: {self._name}\nEmployee ID: {self._ID}\n"
                f"Department: {self._department}\nJob Title: {self.job_title}")

    def get_all(self):
        return self._ID, self._name, self._department, self.job_title

    def change_name(self, new_name):
        self._name = new_name

    def change_job_title(self, new_title):
        self.job_title = new_title

    def change_department(self, new_department):
        self._department = new_department


if __name__ == "__main__":
    main()
