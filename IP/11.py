'''
Print multiplication table of 2, 4 and 5 using loop.
'''

for i in range(6):
    if i in [2, 4, 5]:
        for j in range(1, 11):
            product = f"{i * j:02d}"
            print(product, end=" ")
        print()