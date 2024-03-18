# Problem 1: Recursive sum computation

def sum_recursive(x):
    if x == 1:
        return 1
    else:
        return x + sum_recursive(x - 1)

result = sum_recursive(10)
print(result)
