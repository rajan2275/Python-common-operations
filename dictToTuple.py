# -------------------------------------------
# Convert two dictionaries to list of tuples
# -------------------------------------------
dict1 = { 'a': 'A', 'b': 'B', 'c': 'C'}
dict2 = {'a': '1', 'b': '2', 'c': '3'}

# Need list of tuples with matching values from dict1 and dict2.

result = [(v, y) for k, v in dict1.items() for x, y in dict2.items() if k == x]

print(result)


