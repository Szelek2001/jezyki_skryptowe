# 1
import math


def to_rad(x):
    return x * math.pi / 180


x = math.radians(360)
print(x, to_rad(360))

x = math.radians(90)
print(x, to_rad(90))

x = math.radians(45)
print(x, to_rad(45))

# 2
import random

countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark',
             'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland', 'Serbia',
             'Costa Rica', 'Sweden', 'Mexico', 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama',
             'Colombia', 'Japan', 'Senegal', 'Poland']

random.shuffle(countries)


def random_choice_and_print():
    c_list = [random.choice(countries)]
    print(c_list)
    return c_list


A = random_choice_and_print()
B = random_choice_and_print()
C = random_choice_and_print()
D = random_choice_and_print()
E = random_choice_and_print()
F = random_choice_and_print()
G = random_choice_and_print()
H = random_choice_and_print()

# 3
import random


def add_4():
    list = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    return list


list1 = add_4()
list2 = add_4()

if sum(list1) > sum(list2):
    print("more in turn nr. 1  - %d" % sum(list1))
elif sum(list1) < sum(list2):
    print("more in turn nr. 2 -  %d" % sum(list2))
else:
    print("equals -  %d" % sum(list2))

# 4

numbers = set([])

while len(numbers) < 7:
    numbers.add(random.randint(1, 49))

print(sorted(numbers))

# 5
import random


def create(colors, figures):
    cards = []
    for color in colors:
        for figure in figures:
            cards.append((figure, color))
    return cards


def give_cards_to_players(cards_in_game, n):
    random.shuffle(cards_in_game)
    p1, p2 = [], []
    for i in range(n):
        p1.append(cards_in_game[i])
        p2.append(cards_in_game[-i - 1])
    return p1, p2


colors_base = ['Trefl', 'Karo', 'Kier', 'Pik']
figures_base = ['As', 'King', 'Queen', 'Jack', '10', '9']

all_card = create(colors_base, figures_base)
player1, player2 = give_cards_to_players(all_card, 5)
print(player1)
print(player2)

cards_rank = dict(zip(figures_base, [i for i in range(8, 14)]))

free_cards = []

while len(player1) != 0 and len(player2) != 0:
    cards_player_1 = player1.pop()
    cards_player_2 = player2.pop()
    free_cards.append(cards_player_1)
    free_cards.append(cards_player_2)
    if cards_rank[cards_player_1[0]] < cards_rank[cards_player_2[0]]:
        player1.extend(free_cards)
        free_cards.clear()
    elif cards_rank[cards_player_1[0]] > cards_rank[cards_player_2[0]]:
        player2.extend(free_cards)
        free_cards.clear()

if len(player1) == len(player2):
    print("remis")
elif len(player1) > len(player2):
    print("Wygrał gracz nr 1")
else:
    print("Wygrał gracz nr 2")
# 6

def day_to_end():
    import datetime

    today = datetime.datetime.today()
    year = today.year
    date_end_year = datetime.datetime(year, 12, 31)
    delta = date_end_year - today
    print(delta.days)
    print(delta)
    return


day_to_end()


# 7
import os
import time

dir1 = input("Podaj katalog")
if os.path.isdir(dir1):
    file1 = input("Podaj plik")
    full_file = os.path.join(dir1, file1)
    if os.path.isfile(full_file):
        print(time.localtime(os.path.getmtime(full_file)))
        print(time.localtime(os.path.getctime(full_file)))
        print(time.localtime(os.path.getatime(full_file)))
        print(os.path.getsize(full_file))
    else:
        print("Nie ma takiego pliku")
else:
    print("Nie ma takiego katalogu")


# 8

def write_to_file(path, load):
    with open(path, 'w') as file2:
        file2.write(load)


def add_to_file(path, load):
    with open(path, 'a') as file2:
        file2.write('\n')
        file2.write(load)


def read_to_file(path):
    with open(path, 'r') as file2:
        for line in file2:
            print(line)


website = input('Podaj adres strony')
file_path = "file1.txt"

print("Utworzenie")

write_to_file(file_path, website)
read_to_file(file_path)

print("dodanie")

add_to_file(file_path, website)
add_to_file(file_path, website)
add_to_file(file_path, website)
read_to_file(file_path)

print("Nadpisanie")
write_to_file(file_path, website)
read_to_file(file_path)
