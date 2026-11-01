"""
Category: String Methods + Data Validation
Difficulty: Intermediate
DE relevance: ★★★★★

A pipeline receives:
quantity = "48"



Your task:
1. Check whether quantity contains only digits using isdigit().
2. If valid, convert it to an integer and print "Valid quantity:" with the value.
3. Otherwise, print "Invalid quantity:" with the original value."""

quantity = "48"

if quantity.isdigit():
    print("valid quantity:",int(quantity))
else:
    print("Invalid quantity:", quantity)
    