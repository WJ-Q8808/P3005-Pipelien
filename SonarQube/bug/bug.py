# -*- coding: utf-8 -*-#
# 随便提交
bug = "bug个数"

def count_number(start):
    add_number =+ start     #bug001
    return add_number

def count_str(start):
    add_number =- start    #bug002
    return add_number

def count_list(start):
    add_number =+ start   #bug003
    return add_number

if __name__ == '__main__':
    count_number(2)
