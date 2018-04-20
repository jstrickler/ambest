#!/usr/bin/env python


class TrimmedFile():

    def __init__(self, file_name):
        self._file_name = file_name
        self._file = open(self._file_name)


    def __iter__(self):
        return self

    def __next__(self):
        next_line = self._file.readline()
        if next_line == '':
            raise StopIteration
        else:
            return next_line.rstrip()

if __name__ == '__main__':
    m = TrimmedFile('DATA/mary.txt')
    for line in m:
        print(line)
