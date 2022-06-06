from book import Book
from customer import Customer
from customers import CustomersMngr


class Library:

    def __init__(self) -> None:
        # option 1
        self.customers = {} # customer_id => Customer
        self.books = {}
        self.loans = {}

        #option 2
        self.customers_mngr = CustomersMngr()

    def add_customer(self, id, name, address, birth_date):
        customer = Customer(id, name, birth_date, address)
        self.customers[id] = customer

    def add_customer(self, id, name, address, birth_date):
        # option 1
        customer = Customer(id, name, birth_date, address)
        self.customers[id] = customer

        # option 2
        self.customers_mngr.add_customer(id, name, address, birth_date)

    def get_all_customers(self):
        return self.customers_mngr.get_all_customers()

    def find_book(self, name) -> Book:
        for book in self.books.values():
            if book.name == name:
                return book