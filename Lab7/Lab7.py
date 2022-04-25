from timeit import default_timer as timer

# Zadanie1

all_cases = []
by_date = {}
by_country = {}


def measure(func):
    def time_it(*args, **kwargs):
        start_time = timer()
        try:
            # wykonujemy funkcję którą potrzebujemy
            return func(*args, **kwargs)
        finally:
            end_time = timer()
            result = end_time - start_time
            print(f"Czas wykonywania funkcji {func.__name__} wynosi {result * 1000} ms")

    return time_it


def add_a(day, month, year, cases, deaths, countries_and_territories):
    tuple1 = (countries_and_territories, year, month, day, deaths, cases)
    all_cases.append(tuple1)


def add_d(day, month, year, cases, deaths, countries_and_territories):
    if (year, month, day) in by_date.keys():
        by_date[(year, month, day)].append((countries_and_territories, deaths, cases))
    else:
        by_date[(year, month, day)] = [(countries_and_territories, deaths, cases)]


def add_c(day, month, year, cases, deaths, countries_and_territories):
    if countries_and_territories in by_country.keys():
        by_country[countries_and_territories].append((year, month, day, deaths, cases))
    else:
        by_country[countries_and_territories] = [(year, month, day, deaths, cases)]


def read_file():
    with open(r'Covid.txt', encoding="utf-8") as file:
        line_number = 0
        for line in file:
            if line_number != 0:
                data = line.split()

                add_a(data[1], data[2], data[3], data[4], data[5], data[6])
                add_d(data[1], data[2], data[3], data[4], data[5], data[6])
                add_c(data[1], data[2], data[3], data[4], data[5], data[6])

            line_number += 1


# Zadanie2

@measure
def for_date_a(year, month, day):
    number_deaths = 0
    number_cases = 0

    for tuple1 in all_cases:
        if tuple1[1] == str(year) and tuple1[2] == str(month) and tuple1[3] == str(day):
            number_deaths += int(tuple1[4])
            number_cases += int(tuple1[5])
    return number_deaths, number_cases


@measure
def for_date_d(year, month, day):
    number_deaths = 0
    number_cases = 0
    for key in by_date.keys():
        if key == (str(year), str(month), str(day)):
            for date in by_date[key]:
                number_deaths += int(date[1])
                number_cases += int(date[2])
            break
    return number_deaths, number_cases


@measure
def for_date_c(year, month, day):
    number_deaths = 0
    number_cases = 0

    for key in by_country.keys():
        for number in by_country[key]:
            if number[0] == str(year) and number[1] == str(month) and number[2] == str(day):
                number_deaths += int(number[3])
                number_cases += int(number[4])
    return number_deaths, number_cases


# Zadanie3

@measure
def for_country_a(country):
    number_deaths = 0
    number_cases = 0
    for tuple1 in all_cases:
        if tuple1[0] == str(country):
            number_deaths += int(tuple1[4])
            number_cases += int(tuple1[5])
    return number_deaths, number_cases


@measure
def for_country_d(country):
    number_deaths = 0
    number_cases = 0
    for key in by_date.keys():
        for date in by_date[key]:
            if date[0] == country:
                number_deaths += int(date[1])
                number_cases += int(date[2])
    return number_deaths, number_cases


@measure
def for_country_c(country):
    number_deaths = 0
    number_cases = 0
    for key in by_country.keys():
        if key == country:
            for date in by_country[key]:
                number_deaths += int(date[3])
                number_cases += int(date[4])
            break
    return number_deaths, number_cases


# Zadanie4

@measure
def for_date_country_a(year, month, day, country):
    number_deaths = 0
    number_cases = 0
    for tuple1 in all_cases:
        if tuple1[0] == str(country) and tuple1[1] == str(year) and tuple1[2] == str(month) and tuple1[3] == str(day):
            number_deaths += int(tuple1[4])
            number_cases += int(tuple1[5])
    return number_deaths, number_cases


@measure
def for_date_country_d(year, month, day, country):
    number_deaths = 0
    number_cases = 0
    for key in by_date.keys():
        if key == (str(year), str(month), str(day)):
            for date in by_date[key]:
                if date[0] == country:
                    number_deaths += int(date[1])
                    number_cases += int(date[2])
    return number_deaths, number_cases


@measure
def for_date_country_c(year, month, day, country):
    number_deaths = 0
    number_cases = 0
    for key in by_country.keys():
        if key == country:
            for number in by_country[key]:
                if number[0] == str(year) and number[1] == str(month) and number[2] == str(day):
                    number_deaths += int(number[3])
                    number_cases += int(number[4])
    return number_deaths, number_cases


if __name__ == '__main__':
    read_file()
    print(for_date_a(2020, 10, 11))
    print(for_date_d(2020, 10, 11))
    print(for_date_c(2020, 10, 11))
    print(for_country_a("Poland"))
    print(for_country_d("Poland"))
    print(for_country_c("Poland"))
    print(for_date_country_a(2020, 10, 11, "Montenegro"))
    print(for_date_country_d(2020, 10, 11, "Montenegro"))
    print(for_date_country_c(2020, 10, 11, "Montenegro"))
