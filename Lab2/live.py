# 1A

text = "The OCaml toolchain includes an interactive top-level interpreter, a bytecode compiler, " \
       "an optimizing native code compiler, a reversible debugger, and a package manager (OPAM). " \
       "OCaml was initially developed in the context of automated theorem proving, and has an outsize " \
       "presence in static analysis and formal methods software. Beyond these areas, it has found serious " \
       "use in systems programming, web development, and financial engineering, among other application domains." \
       "The acronym CAML originally stood for Categorical Abstract Machine Language, but OCaml omits this " \
       "abstract machine.[3] OCaml is a free and open-source software project managed and principally maintained " \
       "by the French Institute for Research in Computer Science and Automation (INRIA). In the early 2000s, elements " \
       "from OCaml were adopted by many languages, notably F# and Scala."

words = text.split(' ')
actual_list = []

for word in words:
    if word == "OCaml":
        actual_list = []
    else:
        actual_list.append(word)

print(actual_list)

# 1B

count = 0

for letter in text:
    if letter == 'a' or letter == 'A':
        count = count + 1

print(count)

# 1C

text2 = text.replace(",", ";")
print(text2)

# 1D

print(text.count("for"))

# 1E

text3 = set(text)
print(len(text3))

#  2

name = []
surname = []
password = []

while True:

    while True:
        user_pass = input("Podaj hasło (hasło zawiera minimum 10 znaków, małe i wielkie litery oraz znak specjalny ‘#’.) ")
        if (len(user_pass) < 10):
            print("Hasło było za krótkie")
            continue
        elif user_pass.count("#") == 0:
            print("Brak znaku specjalnego")
            continue
        elif user_pass.islower():
            print("Brak dużych liter")
            continue
        elif user_pass.isupper():
            print("Brak małych liter")
            continue
        password.append(user_pass)
        break

    name_user = input("Podaj imie")
    name.append(name_user)
    surname_user = input("Podaj nazwisko")
    surname.append(surname_user)
    user_a_pass = input("Podaj haslo")
    if(user_a_pass in password):
        print("Udalo sie zalogowac")
    czy_next = input("czy wprowadzic następnego użytkownika 1 - Tak")
    if czy_next != 1:
        break

print(name)
print(surname)
print(password)
# 3

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]


countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']



# 3A

minimum_val = min(percent)
maximum_val = max(percent)

min_max = "Minimalna wartość wynosi: %10f , a maksymalna: %10f"

print(min_max % (minimum_val, maximum_val))


# 3B

dictionary1 = dict(zip(percent, countries))

sum_all = sum(percent)

letter = ["A", "B", "C", "D", "E"]
sum_abcde = 0

for per, country in dictionary1.items():
    if country[0] in letter:
        sum_abcde = sum_abcde + per


print("Suma wszytskich wynosi: {0:f}, a na litery od A do E: {1:f}".format(sum_all, sum_abcde))