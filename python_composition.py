#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class BasePage(metaclass=ABCMeta):
    def __init__(self):
        self._name = type(self).__name__
        print("Creating", self._name)

    @abstractmethod
    def do_report(self):
        pass

class Page1(BasePage):
    def do_report(self):
        print(self._name, "creating Page 1")

class Page2(BasePage):
    def do_report(self):
        print(self._name, "creating Page 2")

class Page3(BasePage):
    def do_report(self):
        print(self._name, "creating Page 3")

class Report():
    def __init__(self):
        self._pages = []

    def add_page(self, page):
        self._pages.append(page)

    def print_report(self):
        print("REPORT HEADER")
        for page in self._pages:
            page.do_report()
        print("REPORT FOOTER")

r1 = Report()
p1 = Page1()
p2 = Page2()
r1.add_page(p1)
r1.add_page(p2)
r1.print_report()
print('-' * 60)

r2 = Report()
p1 = Page3()
p2 = Page1()
r2.add_page(p1)
r2.add_page(p2)
r2.print_report()
