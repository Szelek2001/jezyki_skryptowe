

class File:
    _file_path = "file1.txt"

    def __init__(self,website):
        self.website = website

    def write_to_file(self):
        with open(self._file_path, 'w') as file1:
            file1.write(self.website)

    def add_to_file(self):
        with open(self._file_path, 'a') as file1:
            file1.write('\n')
            file1.write(self.website)

    def read_to_file(self):
        with open(self._file_path, 'r') as file1:
            for line in file1:
                print(line)

file3 = File("kokos")

file3.add_to_file()
file3.read_to_file()





