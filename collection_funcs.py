from functools import reduce

#f(x) = 1 + x; Mathmatics formula that helps to understand maps

#Domain: [1,2]
#Range:  [2,3]

domain = [1,2,3,4,5]
#f(x) = x * 2

our_range = map(lambda num: num*2, domain)

#Output of a map will always be the same length as the collection that is going into it.
print(list(our_range))

#Filters out the True from the lambda
evens = filter(lambda num: num %2==0, domain)
print(list(evens))


the_sum = reduce( lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default:")
print(sorted(words))

print("Sorting with a lambda key:")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method:")
#This sets this sort to see the keys as lowercase and reverse the order.
words.sort(key=str.lower, reverse=True)
print(words)


