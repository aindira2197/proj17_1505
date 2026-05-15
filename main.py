numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
    squares.append(number ** 2)

print("Kvadratlar:")

for square in squares:
    print(square)

total = sum(squares)

print("Yigindi:", total)
