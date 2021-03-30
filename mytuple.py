fruit = 'banana'
basket = (fruit,
          "apple",
          "pear",
          "strawberry",
          9999,
          fruit.lower,
          ("ahmet", "bulut")
          )

basket[4] = 9999 + 1

for item in basket:
    print(item)
