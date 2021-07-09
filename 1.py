# -*- coding: utf-8 -*-
# @Author  : Evil0ctal
# @Time    : ${DATE} ${TIME}
# @Function:
# Ask user input a number then output the result compare with 10

size = input("Please input an number: ")

if size.isdigit():
    if int(size) < 10:
        print('smaller')
    elif int(size) > 10:
        print('bigger')
    else:
        print('fit')
else:
    print('Please input a number only')

'''
input 1 output smaller
input 11 output bigger
input 10 output fit
input abc output Please input a number only
'''
