from customer import Customer


class CustomersMngr:

    def __init__(self) -> None:
        self.customers = {} # customer_id => Customer
        self.customers_by_name = {} # customer_name => Customer

    def add_customer(self, id, name, address, birth_date):
        customer = Customer(id, name, birth_date, address)
        self.customers[id] = customer
        self.customers_by_name[name] = customer

    def get_all_customers(self):
        return self.customers.values()

    def remove_customer(self):
        pass

    def find_customer(self):
        pass