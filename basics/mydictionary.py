"""
Key: K
Value: V
An item in this case is (K,V)

d = {
       K1:V1,
       K2:V2,
       K3:V3,
       ...
       ...
     }
"""

d = {
    "cheese": "peynir",
     "chicken": "tavuk",
     "course": "ders",
     "car": "araba"
     }

#key-ed lookup
print(d["car"])

print(d.keys())
print(d.values())
print(d.items())

for V in d.values():
    print(V)

#key-ed modifications
d["car"] = "otomobil"
print(d.items())