
#Regular function definition
def name (a,b):
	print("Something")
	1+a
	return b

#A function that helps to test our lambda function being created. 
def square(num):
	return num * num

#Lambda function that will be tested agains the square function above
square_lambda = lambda num: num * num

#Test that makes sure that our regular function and lambda functions return the same answer.
assert square(4) == square_lambda(4)


