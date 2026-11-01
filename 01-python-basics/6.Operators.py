"""
Your practice question — Question 6.1
Category: Operators
Difficulty: Easy
Question: 12/300

A pipeline should mark a customer record as valid only when:
- age is at least 18.
- account_active is True.
age = 22account_active = True



Your task:
1. Use and to check both conditions.
2. Store the result in is_valid_customer.
3. Print the result."""

age = 22
account_active = True

is_active = age  >= 18 and account_active
print(is_active)
