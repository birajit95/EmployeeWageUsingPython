import random


class Employee:
    __WAGE_PER_HOUR = 20
    __FULL_DAY_HOUR = 8

    def employeeAttendance(self):
        if random.choice([1, 0]) == 0:
            return "present"
        return "absent"

    def calculateDailyEmployeeWage(self):
        return Employee.__WAGE_PER_HOUR * Employee.__FULL_DAY_HOUR



if __name__ == "__main__":
    print("Welcome to Employee Wage Program")

    emp = Employee()
    print(emp.employeeAttendance())
    print(emp.calculateDailyEmployeeWage())


