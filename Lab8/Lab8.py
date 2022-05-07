# Zadanie 1

class Controlled_text():
    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if value.isprintable() and not value.isspace() and len(value) > 0:
            self._text = value
        else:
            raise ValueError("Dane nie spełniają kryterium")


# Zadanie 2

class FirstName(Controlled_text):

    def __init__(self, new_name):
        super().__init__(new_name)
        self.name = new_name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        name_ = new_name.capitalize()
        if FirstName.is_name(name_):
            self._name = name_
        else:
            raise ValueError("Błedne imie")

    acceptable_names = {
        'male': [],
        'female': []
    }

    def is_male(self, new_name):
        if FirstName.male_name(new_name):
            print("{} to imię męskie".format(new_name))
        else:
            print("Imię {} nie jest imieniem męskim".format(new_name))

    def is_female(self, new_name):
        if FirstName.female_name(self.new_name):
            print("{} to imię żeńskie".format(self.new_name))
        else:
            print("Imię {} nie jest imieniem żenskim".format(self.new_name))

    @staticmethod
    def read_file():
        with open(r'PopularneImiona.txt', encoding='utf8') as file:
            data_file = []

            for line in file:
                data = line.split()
                if len(data) > 0:
                    data_file.append(data[0])

            pause = data_file.index('Mężczyźni')
            FirstName.adding_female(data_file, pause)
            FirstName.adding_male(data_file, pause)

    def adding_female(list_, number):
        for i in range(1, number):
            FirstName.acceptable_names['female'].append(list_[i])

    def adding_male(list_, number):
        for i in range(number + 1, len(list_)):
            FirstName.acceptable_names['male'].append(list_[i])

    def is_name(new_name):
        if FirstName.male_name(new_name) or FirstName.female_name(new_name):
            return True
        else:
            return False

    def male_name(name_):
        if FirstName.acceptable_names['male'].__contains__(name_):
            return True
        else:
            return False

    def female_name(name_):
        if FirstName.acceptable_names['female'].__contains__(name_):
            return True
        else:
            return False


# Zadanie 3


class LastName(Controlled_text):
    def __init__(self, new_last_name):
        super().__init__(new_last_name)
        self.lname = new_last_name

    def __str__(self):
        return self.lname

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, new_lname):
        if '-' in new_lname:
            where_two_last = new_lname.split("-")
            if where_two_last[0].capitalize() == where_two_last[0] and where_two_last[1].capitalize() == where_two_last[1]:
                self._lname = where_two_last[0] + '-' + where_two_last[1]
            else:
                raise ValueError("Nazwisko nie spelniaja wymogow")
        else:
            if new_lname.capitalize() == new_lname:
                self._lname = new_lname
            else:
                raise ValueError("Nazwisko nie spelniaja wymogow")


# Zadanie 4

class IndentNumber(Controlled_text):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.ident_number = numbers

    def __str__(self):
        return self.__ident_number

    @property
    def ident_number(self):
        return self._lname

    @ident_number.setter
    def ident_number(self,number):

        sum = 0
        rest = 0
        print()
        if len(number) != 9:
            raise ValueError("Liczba nie ma 9 cyfr")


        for i in range(7):
            sum = sum + int(number[i])

        for i in range(7,9):
            rest = rest + int(number[i])

        if sum % 97 == rest:
            self.__ident_number = number
        else:
            raise ValueError("Liczby nie spelniaja warunkow")


class Person:
    def __init__(self, name1, lname1, ident1):
        self.name_ = FirstName(name1)
        self.lname_ = LastName(lname1)
        self.ident_ = IndentNumber(str(ident1))

    def __str__(self):
        return self.name_.__str__() + " " + self.lname_.__str__() + " " + self.ident_.__str__() + "\n"

    @staticmethod
    def from_string(text):
        data = []
        if " " in text:
            data = text.split()
        elif "," in text:
            data = text.split(',')
        elif ";" in text:
            data = text.split(";")
        elif "/" in text:
            data = text.split("/")
        return Person(data[0], data[1], data[2])


def read_file_with_people():
    with open(r'people.txt', encoding='utf8') as file:
        for line in file:
            data = Person.from_string(line)
            print(data)


def save_data_to_file(data):
    file1 = open(r'saves.txt', "a")
    file1.write(data)
    file1.close()

if __name__ == '__main__':
    FirstName.read_file()
    name = 'Adam'
    lname = 'Kowalski'
    number1 = IndentNumber('100000010')
    read_file_with_people()

    person1 = Person(name, lname, number1)
    save_data_to_file(person1.__str__())