fruit = 'banana'
print(fruit, "contains", len(fruit), "characters")

print("the first letter", fruit[0])
print("the last letter", fruit[len(fruit)-1])

print("while loop example")
index = 0 # initialization
while index < len(fruit): # loop check
    print(fruit[index])   # body action
    index = index + 1     # index increment/decrement

print("for loop example")
for item in fruit:
    print(item)

print("middle slice", fruit[4:6])

# fruit[0] = 'B' --> You cannot do this, because strings are immutable.

new_fruit = 'B' + fruit[1:]
print(fruit, new_fruit)

U_fruit = fruit.upper()

substring = 'nan'
print(substring, "is at index", fruit.find(substring))

if 'nana' in fruit:
    print("oh, that must be banana :D")

check = ("apple" == "banana")
print(check)

empty_string = ''
print(empty_string, len(empty_string))