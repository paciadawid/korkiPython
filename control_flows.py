from collections import OrderedDict

a = 10

if a > 0:
    print('Wieksze od zera')
elif a == 0:
    print('Zero')
else:
    print('Mniejsze od zera')

# and, or, not, in

fruits = ["apple", "orange", "pear"]

def check_japko(list_of_fruits):
    for i in range(len(list_of_fruits)):
        if fruits[i] == "apple":
            return "Japko"
    return False

print(check_japko(fruits))

if "apple" not in fruits:
    print("NIE MA JAPKO")


if "apple" in fruits and len(fruits) >= 3:
    pass


for i in range(len(fruits)):
    if fruits[i] == "apple":
        print("JAPKO")

for i in range(10):
    print(i)

for fruit in fruits:
    if fruit == "apple":
        print("JAPKO")

fast_car = {
    "marka": "fiat",
    "model": "500",
    "waga": 700,
    "pasażerowie": ["Jan", "Maria"]
}

for key, value in fast_car.items():  # .keys(), .values()
    print(key, value)

for _ in range(10):
    pass

a = [1, 2]

_, c = a


i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# there is no do ... while in Python