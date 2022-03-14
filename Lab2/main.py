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
    try:
        emails.append(input())
        domains.append(emails[i][emails[i].index("@") + 1:])
    except ValueError as e:
        print('You need to enter email')


domain = "%10s %2d"
for domai in domains:
    print(domain % (domai, domains.count(domai)))


# 4a

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def print_factor(x):
    print("The factors of %d are:" % x)
    for i in range(1, x + 1):
        if x % i == 0:
            print("%d " % i)


list1 = [19, 3, 15, 43, 98, 16, 9, 23, 4]

for i in list1:
    if isPrime(i):
        print("%d is prime" % i)
    else:
        print_factor(i)

# 4b

list2 = [19, 3, 15, 43, 98, 16, 9, 23, 4]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# 4c

list3 = [19, 3, 15, 43, 98, 16, 9, 23, 4]
tuple1 = (list3[0], list3[1], list3[2])
tuple2 = sorted(tuple1)
for i in range(3):
    list3[i] = tuple2[i]
print(list3)

# 5

list4 = [12, 5, 8, 8, 23, 15, 7, 8, 9, 12, 34, 6, 9, 16, 8, 23, 12, 7, 5, 3]
capacity = 100
list4.sort(reverse=True)
sum_elem = 0
while sum_elem < capacity:
    sum_elem += list4[0]
    print(list4[0])
    del list4[0]
    if len(list4) == 0: break

# 6

name_everyone = []
surname_everyone = []
name_and_surname_everyone = []
pwr_domain = "@pwr.edu.pl"

for i in range(4):
    name = input("Your name:")
    surname = input("Your surname:")
    name_everyone.append(name)
    surname_everyone.append(surname)
    name_and_surname_everyone.append(name + " " + surname)
    print(name.lower() + '.' + surname.lower() + pwr_domain)

print(name_everyone)
print(surname_everyone)
print(name_and_surname_everyone)