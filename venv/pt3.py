# Problem 3: Recursive digit count

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

values = [15, 105, 15105]

for val in values:
    digits = count_digits(val)
    print(f"The number {val} has {digits} digit(s).")
