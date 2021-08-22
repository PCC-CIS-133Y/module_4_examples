# example 4.1
def main():
    # call the function and store the returned value
    # in the variable num
    num = getValidInput()
    print('num contains:', num)
    print()

    # call the function and print the returned value
    # it will not be saved to be used later!
    print('function returns:', getValidInput())

def getValidInput():
    valid = False
    # prompt for an integer and store in number
    while not valid:
        try:
            number = int(input("Enter integer: "))
            valid = True
        except:
            print("Not an integer!")
    
    # return the value stored in number
    return number

main()