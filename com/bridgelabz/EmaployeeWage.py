import random


class Employee:
    __WAGE_PER_HOUR = 20
    __FULL_DAY_HOUR = 8
    __PART_TIME_HOUR = 4

    def employeeAttendance(self):
        if random.choice([1, 0]) == 0:
            return "present"
        return "absent"

    def getEmpPerDayWorkingHour(self):
        workHourDict = {0: Employee.__PART_TIME_HOUR, 1: Employee.__FULL_DAY_HOUR}
        return workHourDict.get(random.choice([0, 1]))

    def calculateDailyEmployeeWage(self, employeeWorkHours):
        return Employee.__WAGE_PER_HOUR * employeeWorkHours



if __name__ == "__main__":
    print("Welcome to Employee Wage Program")

    emp = Employee()
    print(emp.employeeAttendance())
    print(emp.calculateDailyEmployeeWage(emp.getEmpPerDayWorkingHour()))
    print(emp.getEmpPerDayWorkingHour())
