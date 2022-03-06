# 1a

print("Product  Amount  Vat          Price")
product = "%7s %7d %4d %14d"
print(product % ("Bread", 2, 23, 15))
print(product % ("Egg", 5, 6, 2))
print(product % ("Butter", 13, 0, 9))
print(product % ("Tomato", 2, 3, 1))
print(product % ("LEGO", 1, 23, 1000))

# 1b

print()
print("Product  Amount  Vat          Price")
product = "{0:7s} {1:7d} {2:4d} {3:14d}"
print(product.format("Bread", 2, 23, 15))
print(product.format("Egg", 5, 6, 2))
print(product.format("Butter", 13, 0, 9))
print(product.format("Tomato", 2, 3, 1))
print(product.format("LEGO", 1, 23, 1000))

# 2

is_lights_on = False
is_night = True
is_difficult_conditions = False

if is_night or is_difficult_conditions:
    is_lights_on = True
    print("Lights On")
else:
    print("Lights off")


# 3
emails = []
domains = []

for i in range(5):
    emails.append(input())
    domains.append()

