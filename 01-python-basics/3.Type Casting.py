"""Category: Type Casting
Difficulty: Easy
Question: 06/300

A data pipeline receives:
items = "8"unit_price = "125.50"



Your task:
1. Convert items to an integer.
2. Convert unit_price to a float.
3. Calculate total_cost = """

items = "8"
unit_price = "125.50"

print(int(items))
print(float(unit_price))

total_cost = int(items) * float(unit_price)
print(total_cost)
print(type(total_cost))
print("The data type of total_cost is:", type(total_cost))
print(type(items))