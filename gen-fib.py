#!/usr/bin/env python3

def gen_range(stop, start=1, step=1):
	num = start
	while num <= stop:
		yield num
		num += step

def gen_fib():
	a,b = 0,1
	while True:
		a,b = b, a+b
		yield a


def num_suffix(string):
	l = [d for d in string]

	if int(l[0]) == 1 and len(l) == 2 :
		return ''.join(l) + "th" 
	elif int(l[-1]) == 1:
		return ''.join(l) + "st"
	elif int(l[-1]) == 2:
		return ''.join(l) + "nd"
	elif int(l[-1]) == 3:
		return ''.join(l) + "rd"
	else:
		return ''.join(l) + "th"

response = input("What number of the Fibonacci Sequence do you want to see? ")
fib = gen_fib()

result = [next(fib) for _ in range(int(response))][-1]
print(f"{result} is the {num_suffix(response)} number in the Fibonacci Sequence.")
fib = gen_fib()
