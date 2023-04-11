# Prompt the user for a number
num = int(input("Enter a number: "))

factorial =  num

# Calculate the factorial
for i in range(1, num+1):
    factorial = factorial * i

# Print the output
print(factorial)