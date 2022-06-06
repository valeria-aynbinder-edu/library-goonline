import os
from library import Library
import pickle


if __name__ == '__main__':

    if not os.path.exists("library.pickle"):
        library = Library()
    else:
        # load the file
        with open("library.pickle", "rb") as file_handler:
            library = pickle.load(file_handler)

    try:

        print("Welcome to the library")
        print(library.get_all_customers())

        for i in range(3):
            #user chooses to add a new customer
            customer_id = int(input("Insert id: "))
            name = input("Insert a name: ")
            birth_date = input("Insert birth date: ")
            address = input("Insert address: ")
            library.add_customer(customer_id, name, address, birth_date)

        print("bye")



    except Exception as e:

        print(f"Error occured: {e}")

    finally:
        #save to file
        with open("library.pickle", "wb") as file_handler:
            pickle.dump(library, file_handler)
