"""
Author: Pham Dinh Nam
Date: 02/10/2021
Problem:
    Write a code segment that displays the values of the integers x, y, and z on a single line, such that each value is right-justified with a field width of 6
Solution:

"""

x = int(input("Nhap X: "))
y = int(input("Nhap Y: "))
z = int(input("Nhap Z: "))

# noinspection PyStringFormat
print("-%6s" % x, y, z)
