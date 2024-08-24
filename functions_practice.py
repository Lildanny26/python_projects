# Question 1
# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print('Hello, user!')

hello()

# Question 2
# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

result = pack('apple', 'banana', 'cherry')
print(result)

# Question 3 
# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.


def eat_Lunch(lunchItems):
    if not lunchItems:
        print("My lunchbox is empty.")
    else:
        for i, item in enumerate(lunchItems):
            if i == 0:
                print(f"First I eat my {item}.")
            else:
                print(f"Next I eat my {item}.")

eat_Lunch(["Sandwich", "Apple", "Chips"])

eat_Lunch([])