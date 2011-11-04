num = 600851475143

# Factors are 71, 839, 1471, 6857

factors = []

def primeFactor(input):
    maxDiv = input / 2
    i = 2
    while i <= maxDiv:
        if input % i == 0:
	    factors.append(i)
	    input /= i
	    return primeFactor(input)
	i += 1
    factors.append(input)
    return input

primeFactor(num)
factors.sort()
print factors[-1] #somehow prints off 1471 instead of 6857
