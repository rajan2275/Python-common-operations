# ------------------------------------------------------
# Example 1: add 1 to list of numbers using generators
# ------------------------------------------------------

def add_one(numbers):
    for num in numbers:
        yield(num + 1)

numbers = [1, 2, 3, 4, 5]

print('---------Start Example 1----------')
for num in add_one(numbers):               # DO NOT CONVERT numbers (e.g. list(number) TO LIST AS PERFORMANCE GAIN WILL BE LOST.
    print('Example 1:'+ str(num))


# ------------------------------------------------------
# Example 2: add 1 to list of numbers using generators
# ------------------------------------------------------

numbers = (x+1 for x in [1, 2, 3, 4, 5])   # replacing [] with () makes it generator.
                                           # DO NOT CONVERT numbers (e.g. list(number) TO LIST AS PERFORMANCE GAIN WILL BE LOST.
print('---------Start Example 2----------')
for num in numbers:
    print( 'Example 2:'+ str(num))