def main():
    pass


def employee_directory():
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
