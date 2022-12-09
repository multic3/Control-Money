import pandas as pd
import csv


class ControlMoney:
    def __init__(self, name):
        self.__name = name
        self._file = pd.read_csv(name, parse_dates=['Date'], index_col='id')
        self.head = 'id,Category,Product,Cost,Date'.split(',')
        with open(name, 'r', encoding='utf-8') as file:
            self._file_temp = list(csv.DictReader(file))

    @property
    def file(self):
        return self._file

    def file_adder(self, *args):
        line = dict(zip(self.head, args))

        self.rec(line, mod='A')

    def file_deleter(self, id_mark):
        self._file_temp = list(filter(lambda x: x['id'] != str(id_mark), self._file_temp))
        self._file = self._file_temp[:]
        self.rec(self._file, mod='W')

    def show_by_choice(self, value=None, rev=False):
        if value is None:
            return self
        return self._file.sort_values(by=value)

    def rec(self, lst, mod='A'):
        if mod == 'A':
            with open(self.__name, 'a', encoding='utf-8') as file_new:
                writer = csv.DictWriter(file_new, fieldnames=self.head)
                writer.writerow(lst)
        elif mod == 'W':
            with open(self.__name, 'w', encoding='utf-8') as file_new:

                writer = csv.DictWriter(file_new, fieldnames=self.head)
                writer.writeheader()
                for line in lst:
                    writer.writerow(line)

    def __str__(self):
        return str(self._file)

    def __len__(self):
        return len(self._file)
