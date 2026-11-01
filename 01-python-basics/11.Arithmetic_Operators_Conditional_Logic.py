"""
Category: Arithmetic Operators
Difficulty: Easy
DE relevance: ★★★★☆

A pipeline has:
total_records = 27batch_size = 6



Your task:
1. Calculate the number of complete batches using //.
2. Calculate the remaining records using %.
3. Print both results.
"""


total_records = 27
batch_size = 6

complete_batches = total_records // batch_size
remaining_records = total_records % batch_size

print(complete_batches)
print(remaining_records)