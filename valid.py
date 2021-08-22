# example 4.3 valid.py
def get_age():
    age = 0
    while True:
        age = int(input("Enter age: "))
        if age < 0 or age > 120:
            print("Invalid. Only ages 0-120 allowed.")
        else:
            break
    return age