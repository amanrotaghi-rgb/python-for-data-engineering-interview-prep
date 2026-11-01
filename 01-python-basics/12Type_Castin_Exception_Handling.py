"""
Category: Type Casting + Exception Handling
Difficulty: Intermediate
DE relevance: ★★★★★

A pipeline receives:
price = "free"

Your task:
1. Try converting price to a float.
2. If conversion succeeds, print "Valid price:" and the converted value.
3. If conversion fails, catch ValueError and print "Invalid price:" and the original value."""

price = "free"
try:
    price = int(price)
    print("valid price:",price)
except ValueError:
    print("Invalid price:", price)
    