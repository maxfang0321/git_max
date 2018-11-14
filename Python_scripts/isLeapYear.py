# -*-coding:utf-8 -*-

import sys

year = sys.argv[1]

def isLeapYear(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

print(isLeapYear(int(year)))
