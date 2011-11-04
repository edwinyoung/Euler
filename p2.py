import sys

fib = [0, 1]

def createFib():
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])
    
createFib()
print sum([i for i in fib if i % 2 == 0])

