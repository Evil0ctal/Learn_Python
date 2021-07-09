# -*- coding: utf-8 -*-
# @Author  : Evil0ctal
# @Time    : 2021/07/09
# @Function:
# Enter the number of hours and salary rate, calculate the total salary and output to the console.
# If the input is not an number out put error message.

try:
    hours = int(input("Please input the total hours of the employee worked: "))
    rate = int(input("Please input the hour rate of the employee pay: "))
    if hours < 40:
        print("Total:" + str(hours*rate))
    else:
        extra_pay = hours - 40
        print("Total:" + str((40 * rate) + (extra_pay * rate * 1.5)))
except:
    print("Error,Please enter numeric input")

'''
Please input the total hours of the employee worked: 10
Please input the hour rate of the employee pay: 10
Total:100

Please input the total hours of the employee worked: 40
Please input the hour rate of the employee pay: 10
Total:400.0

Please input the total hours of the employee worked: 41
Please input the hour rate of the employee pay: 10
Total:415.0

Please input the total hours of the employee worked: 44
Please input the hour rate of the employee pay: nine
Error,Please enter numeric input

Please input the total hours of the employee worked: one
Please input the hour rate of the employee pay: ten
Error,Please enter numeric input
'''
