numbers = [12, 45]
# The list contains two elements
# List indices in Python start from 0.
# The last element sits at index 1, i.e numbers[1].

# Item lookup with respect to the *beginning* of the list,
# where indices start from 0.
#print(numbers[0])
#print(numbers[1])

# Item lookup with respect to the *end* of the list,
# where indices start from -1
#print(numbers[-1])
#print(numbers[-2])

cheeses = ['Ezine', 'Lor', 'Kasar', 'Tulum']

for item in cheeses:
    print(item)

print("We have", len(cheeses), "cheeses.")

for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].upper()

print(cheeses[-2:])

cheeses.append("Cheddar")
cheeses.sort()
for item in cheeses:
    print(item)

sentence = 'I::have::got::a::lot::of::cheeses'
words = sentence.split("::")
print(words)
print(",".join(words))

print(cheeses)
peynirler = cheeses
cheeses[-1] = "tulum"
print(peynirler)