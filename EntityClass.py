#!/usr/bin/python
# -*- coding: UTF-8 -*-
# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    # '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

if __name__ == "__main__":
    e = Employee('zs', 10000)
    d = Employee('ls', 12000)
    e.displayEmployee()
    d.displayEmployee()
    e.displayCount()