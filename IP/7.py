def main():
    # Promp the user for number of fibonacci numbers to generate
    num = int(input("Enter the number of fibonacci numbers you would like to generate: "))

    # Print the fibonacci numbers
    display_fibonacci(num)


def display_fibonacci(count):
    # Set the n1 and n2 to n2 to n2 0 and 1
    n1 = 0
    n2 = 1
    # Print n1 and n2
    print(n1)
    print(n2)

    # Loop 'count' times
    for _ in range(count):
        # Calculate and print the sum of previous two numbers
        sum = n1 + n2
        print(sum)

        # Update the value of n1 and n2
        n1 = n2
        n2 = sum


if __name__ == "__main__":
    main()