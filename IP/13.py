'''
Write a program to calculate the sum of all numbers between 1 and 100 that
are not divisible by 3 or 5 using a loop.
'''

sum = 0

for i in range(100):
    if i % 3 != 0 and i % 5 != 0:
        sum = sum + i

print(sum)