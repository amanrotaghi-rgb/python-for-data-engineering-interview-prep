"""
Category: Arithmetic Operators
Difficulty: Easy
DE relevance: ★★★★☆

A pipeline has:
total_records = 25
batch_size = 5



Your task:
1. Calculate the remainder using %.
2. Store it in a variable named remainder.
3. Print the result.
4. Tell me: does this record count divide evenly into batches?
"""
total_records = 25
batch_size = 5
remainder = total_records % batch_size
print(remainder)
if remainder == 0:
    print( "his record count divide evenly into batches")
