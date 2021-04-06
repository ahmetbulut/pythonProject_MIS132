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
     StudentID: {"First Name": "Hüseyin", GPA: 3.75, courses_taken: ["MIS132", "MIS233"]},
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