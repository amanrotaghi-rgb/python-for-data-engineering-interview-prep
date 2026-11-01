"""Your practice question — Question 4.1
Category: Operators
Difficulty: Easy
Question: 08/300

A data pipeline processes an order:
quantity = 6
unit_price = 175
discount = 50



Your task:
1. Calculate gross_amount as quantity multiplied by unit price.
2. Calculate final_amount by subtracting the discount from gross amount.
3. Print both values.    """

quantity = 6
unit_price = 175
discount = 50

total_gross_amount = quantity*unit_price
final_amount = total_gross_amount - discount

print(total_gross_amount)
print(final_amount)
