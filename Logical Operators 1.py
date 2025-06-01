# logical operators = evaluate multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

# or operator
temp1 = float(input("Temperature: "))
is_raining = False

if temp1 > 35 or temp1 < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and operator
item_aisle = int(input("What aisle did you find the item: "))
is_on_sale = True

if item_aisle < 0 and is_on_sale:
    print("This aisle cannot be located at this store, we have only 1 - 10 aisle")
if item_aisle <= 3 and is_on_sale:
    print("The item is on sale")
elif item_aisle > 3 and is_on_sale:
    print("This item is not for sale, check aisle 1-3")
else:
    print("The item is not on sale")

# not operator
temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")