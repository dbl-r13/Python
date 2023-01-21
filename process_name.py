#!/usr/bin/ python3

name = input("What is your first name? ")

verdict = "shorter" if len(name)<6 else "as long or longer"

isCommon = " not" if name[0].lower() in ["a", "j", "m", "e", "l"] else ""

vowels = ['a','e','i','u']
v= "vowel"
c="consonant" 

print(f"Your name is {verdict} than the average first name in the United States.")

print(f"The first letter of your name is{isCommon} among the five most common")

for letter in name:
	print(f"{letter} is a {v if letter in vowels else c }")


