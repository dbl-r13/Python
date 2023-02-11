#!/bin/python3

import math

age = int(input("What is your current age? "))

remaining_years = 90 - age

total_days = remaining_years * 365

print("*" * 26)
print(f"You will turn 90 years onld in: ")
print(f"{remaining_years} years")
print(f"      OR")
print(f"{remaining_years*12} months")
print(f"      OR")
print(f"{round(total_days/7)} weeks")
print(f"      OR")
print(f"{total_days} days")
print("*" * 26)
