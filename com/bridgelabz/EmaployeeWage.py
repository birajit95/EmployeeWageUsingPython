import random


class Employee:
    __FULL_DAY_HOUR = 8
    __PART_TIME_HOUR = 4
    __WORKING_DAY_PER_MONTH = 20
    __WAGE_PER_HOUR = 20
    __MAX_WORKING_HOURS = 100

    def __init__(self):
        self.__totalWage = 0

    def setTotalWage(self, totalWage):
        self.__totalWage = totalWage

    def getTotalWage(self):
        return self.__totalWage

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

    def getMaxWorkingHours(self):
        return self.__MAX_WORKING_HOURS


class EmployeeWageBuilder:

    def setEmployee(self, empObj):
        self.empObj = empObj

    def calculateDailyEmployeeWage(self, perDayWorkHours):
        return self.empObj.getWagePerHour() * perDayWorkHours

    def calculateMonthlyEmployeeWage(self):
        workingDayPerMonth = self.empObj.getWorkingDayPerMonth()
        perDayWorkHorus = self.empObj.getEmpPerDayWorkingHour()
        dailyEmpWage = self.calculateDailyEmployeeWage(perDayWorkHorus)
        return workingDayPerMonth * dailyEmpWage

    def wageBuilder(self):
        maxWorkingHours = self.empObj.getMaxWorkingHours()
        maxWorkingDays = self.empObj.getWorkingDayPerMonth()
        totalWorkingHours = 1
        totalWorkingDays = 1
        totalWage = 0
        totalDays = 0
        while totalWorkingHours <= maxWorkingHours and totalWorkingDays <= maxWorkingDays and totalDays <= 30:
            totalDays += 1
            if self.empObj.employeeAttendance() == "present":
                totalWorkingDays += 1
                perDayWorkingHours = self.empObj.getEmpPerDayWorkingHour()
                totalWorkingHours += perDayWorkingHours
                dailyWage = self.calculateDailyEmployeeWage(perDayWorkingHours)
                totalWage += dailyWage
        self.empObj.setTotalWage(totalWage)


if __name__ == "__main__":
    print("Welcome to Employee Wage Program")

    emp = Employee()
    wageBuilder = EmployeeWageBuilder()
    wageBuilder.setEmployee(emp)
    wageBuilder.wageBuilder()
    print(emp.getTotalWage())
