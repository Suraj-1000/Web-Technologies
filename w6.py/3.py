def over_18(people):
    """this function is used to check the people are over 18 or not"""
    return [p for p in people if p["age"]>18]
people=[{'name':'suraj','age':20},
        {'name':'raj','age':30},
        {'name':'sujan','age':25},
        {'name':'suman','age':19},]
output=over_18(people)
print(output)

            