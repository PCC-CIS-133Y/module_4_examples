# example 4.2
def main():
    item, cost, qty = getItemInfo()
    print()
    print(item, " x ", qty, " @ $", format(cost, ".2f"), 
          " each = $", format((qty * cost), ".2f"), sep = '')

def getItemInfo():
    item = input("Enter item: ")
    cost = float(input("Enter cost: $ "))
    qty = int(input("Enter quantity: "))

    return qty, cost

main()