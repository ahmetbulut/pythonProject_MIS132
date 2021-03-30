fruit = 'banana'
basket = (fruit,
          "apple",
          "pear",
          "strawberry",
          9999,
          fruit.lower,
          ("ahmet", "bulut")
          )

# basket[4] = 9999 + 1 --> Immutable!

for item in basket:
    print(item)

def f(n):
    x = (2 + n) / 5
    y = n ** 2
    return (x, y)

a, b = f(3)
print(a, b)