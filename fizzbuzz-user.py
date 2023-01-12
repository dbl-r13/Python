
num = int(input("How many values should I work through? "))

arr = [number for number in range(1,num+1)]

for el in arr:
    if el % 3 == 0 and el % 5 ==0:
        print("FizzBuzz")

    elif el % 3 == 0:
        print("Fizz")
    elif el % 5 == 0:
        print("Buzz")

    else:
        print(el)
else:
    print("-"*15)
    print("FizzBuzz Analysis completed")
