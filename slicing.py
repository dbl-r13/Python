#! /usr/bin/env python3

message = input("Enter a message: ")

print("First Character: " + message[0])
print("Last Character: " + message[-1])
print(f"Middle Character: {message[int(len(message)/2)]}")
print(f"Even Indexed Characters: {message[::2]}")
print(f"Odd Indexed Characters: {message[1::2]}")
print(f"Message Reversed: {message[::-1]}")
