def daa(a,b):
    return a+b

result = daa(5,7)
print(result)

def calculate_average(number):
    if len(number) == 0:
        return 0
    return sum(number)/len(number)

number=[30,20,40,10,5]
average=calculate_average(number)
print(average)

def fibonacci(n):
    fibonacci_sequnce=[0,1]
    while len(fibonacci_sequnce)<n:
        fibonacci_sequnce.append(fibonacci_sequnce[-1]+fibonacci_sequnce[-2])
    return fibonacci_sequnce

n=10
fibonacci_sequnce=fibonacci(n)
print(fibonacci_sequnce)

def find_max(number):
    if len(number) == 0:
        return None,None
    return max(number),min(number)
number=[30,20,40,10,5]
max_value,min_value=find_max(number)
print(max_value,min_value)

def list_intersection(list1,list2):
    return list(set(list1)&set(list2))

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
intersection=list_intersection(list1,list2)
print(intersection)

def factorial(n1):
    if n1 == 0:
        return 1
    else:
        return n*factorial(n1-1)

    number = 5
    fact = factorial(number)
    print(fact)