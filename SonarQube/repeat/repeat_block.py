# -*- coding: utf-8 -*-#

repeat_block = "{}:代码块".format("重复")

def count_number(start):
    add_number = 0
    add_number += int(start)
    print(count_number)
    return count_number

def count_str(start):
    add_number = "str"
    add_number += start
    count_str = len(add_number)
    print(count_str)
    return count_str

def count_list(start):
    add_number = ["list01","list02"]
    add_number.append(start)
    count_list = len(add_number)
    print(count_list)
    print(count_list)
    print(count_list)
    print(count_list)
    print(count_list)
    print(count_list)
    print(count_list)
    return count_list

if __name__ == '__main__':
    count_number(2)
    count_str("str1")
    count_list("ces")

