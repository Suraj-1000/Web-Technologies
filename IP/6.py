'''
Write a program to enter the numbers till the user wants and at the 
end it should display the count of positive, negative and zeros entered.
'''

def main():
    numbers = get_numbers()
    print_numbers(numbers)


def get_numbers():
    numbers = []
    tries = 0 
    while True:
        if tries == 0:
            num = int(input("\nEnter a number: "))
            numbers.append(num)
            tries += 1
        else:
            option = input("Would you like to enter another number? [y/n] ").lower()
            if option in ["y", "yes"]:
                num = int(input("Enter a number: "))
                numbers.append(num)
            elif option in ["n", "no"]:
                return numbers
            
def print_numbers(numbers):
    postive_num = []
    negative_num = []
    zeros = []
    for number in numbers:
        if number > 0:
            postive_num.append(number)
        elif number < 0:
            negative_num.append(number)
        else:
            zeros.append(numbers)
    
    print(f"\nPostive numbers: {len(postive_num)}")
    print(f"Negative numbers: {len(negative_num)}")
    print(f"Zeros: {len(zeros)}")


if __name__ == "__main__":
    main()
