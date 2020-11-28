import random
class Employee:

    def employeeAttendance(self):
        if random.choice([1, 0]) == 0:
            return "present"
        return "absent"

if __name__ == "__main__":
    print("Welcome to Employee Wage Program")

    emp = Employee()
    print(emp.employeeAttendance())