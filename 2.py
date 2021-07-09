# -*- coding: utf-8 -*-
# @Author  : Evil0ctal
# @Time    : 2021/07/09
# @Function:
# Enter the number of hours and salary rate, calculate the total salary and output to the console.

hours = input("Please input the total hours of the employee worked: ")
rate = input("Please input the hour rate of the employee pay: ")

if hours.isdigit() and rate.isdigit():
    hours = int(hours)
    rate = int(rate)
    if int(hours) < 40:
        print("Total:" + str(hours*rate))
    else:
        extra_pay = hours - 40
        print("Total:" + str((40 * rate) + (extra_pay * rate * 1.5)))
else:
    print('Please input a number only')

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

Please input the total hours of the employee worked: aaa
Please input the hour rate of the employee pay: aaa
Please input a number only
'''
