"""
Question
Find all the prime factors of a given number
"""

#Approach
"""
-> This becomes an important base problem for other problems
Refer Striver video, timestamp: 8:00:
https://www.youtube.com/watch?v=LT7XhVdeRyg

Below code will return prime factors with duplicates, we can use a set to remove duplicates
"""

#Code
def findAllPrimeFactors(n):
    primeFactors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            primeFactors.append(i)
            n = n // i
    if n > 2:
        primeFactors.append(n)
    return primeFactors