"""
Your practice question — Question 7.1
Category: Strings and Operators
Difficulty: Easy
Question: 14/300

A pipeline needs to create a shipment message using:
customer_name = "Rahul"shipment_id = "SHIP-702"



Your task: Create and print this message:
Shipment SHIP-702 is assigned to Rahul
"""
customer_name = "Rahul"
shipment_id = "SHIP-702"

message = "shipment_id" + shipment_id + "is assigned to " + customer_name
print(message)
