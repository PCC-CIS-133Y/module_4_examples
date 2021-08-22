# valid_try.py
def get_age():
    age = 0
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0 or age > 120:
                print("Invalid. Only ages 0-120 allowed.")
            else:
                break
        except:
            print("Invalid. Only integer input allowed.")
    return age