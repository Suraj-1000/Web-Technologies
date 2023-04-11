'''Write a program that prompts the user to input a positive integer. 
It should then print the multiplication table of that number. '''

def main():
    # Promp the user for a positive number
    num = get_num()

    # Print the multiplication table of the number
    for i in range(1, 11):
        product = f"{i* num:02d}"
        print(product)



def get_num():
    num = int(input("Enter a number: "))
    while num < 0:
        num = int(input("Enter a positve number: "))

    return num

if __name__ == "__main__":
    main()