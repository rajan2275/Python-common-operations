# -----------------------------------------
# add 1 to list of numbers using generators
# ------------------------------------------

def add_one(numbers):
    for num in numbers:
        yield(num + 1)


numbers = [1, 2, 3, 4, 5]

for num in add_one(numbers):  # DO NOT CONVERT numbers (e.g. list(number) TO LIST AS PERFORMANCE GAIN WILL BE LOST.
    print(num)