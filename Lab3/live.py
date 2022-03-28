import random


def write_to_file(path, load):
    with open(path, 'w') as file2:
        file2.write(load)
def add_to_file(path, load):
    with open(path, 'a') as file2:
        file2.write(load)

def litwa(file,*args, **kwargs):
    for argss in args:
        if argss % 4 == 0 and (argss % 100 != 0 or argss % 400 == 0):
            write_to_file(file, str(argss))
    for key,syb in kwargs.items():
        if(syb>10):
            add_to_file(file,key)


file_path = "file1.txt"
file_path2 = "file2.txt"
litwa(file_path,2002,2000,1998,poniedzialek = 70, sroda = 7)


def Read(what):
    print('Read {}'.format(what))


def Write(what):
    add_to_file(file_path2,what)
    add_to_file(file_path2, "\n")


books = [(Read, 'wladca pierscieni'), (Write, 'kubus puchatek'), (Read, 'iglo'), (Write, 'mama w krainie snow')]


# Poprawna metoda realizacji tego samego:

def Action(activity, object):
    activity(object)

for activity, object in books:
    Action(activity, object)



def CreateFunction(kind = 'randint'):
    source = '''

def f(*args):
    import random
    result = 0
    for a in args:
        result +=  random.{}(0, 50)
    return result
''' .format(kind)
    exec(source, globals())


    return f  # Wykonywanie dynamicznego kodu polecenie exec()


f_add = CreateFunction("randint")
print(f_add(6))
