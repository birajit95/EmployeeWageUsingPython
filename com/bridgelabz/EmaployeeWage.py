import random


class Employee:

    __FULL_DAY_HOUR = 8
    __PART_TIME_HOUR = 4
    __WORKING_DAY_PER_MONTH = 20
    __WAGE_PER_HOUR = 20

    def employeeAttendance(self):
        if random.choice([1, 0]) == 0:
            return "present"
        return "absent"

    def getEmpPerDayWorkingHour(self):
        workHourDict = {0: Employee.__PART_TIME_HOUR, 1: Employee.__FULL_DAY_HOUR}
        return workHourDict.get(random.choice([0, 1]))

    def getWorkingDayPerMonth(self):
        return Employee.__WORKING_DAY_PER_MONTH

    def getWagePerHour(self):
        return Employee.__WAGE_PER_HOUR


class EmployeeWageBuilder:

    def setEmployee(self, empObj):
        self.empObj = empObj

    def calculateDailyEmployeeWage(self):
        return self.empObj.getWagePerHour() * self.empObj.getEmpPerDayWorkingHour()

    def calculateMonthlyEmployeeWage(self):
        workingDayPerMonth = self.empObj.getWorkingDayPerMonth()
        dailyEmpWage = self.calculateDailyEmployeeWage()
        return workingDayPerMonth * dailyEmpWage


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")

    emp = Employee()
    wageBuilder = EmployeeWageBuilder()
    wageBuilder.setEmployee(emp)

    print(emp.employeeAttendance())
    print(wageBuilder.calculateMonthlyEmployeeWage())

