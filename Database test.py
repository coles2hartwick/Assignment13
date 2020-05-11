# Sam Cole
# 4/30/2020

import sqlite3
from sqlite3 import Error
import datetime


# Method to create the connection to the database.
# The cool part is you do not need to modify this method,
# it will create a connection to a database that you specify
# in the parameter.  If it does not exist, it will create it.
# If it does exist, it will open it for use.
def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


# Create the connection object to the database, "database filename" is the parameter
print("Connect to SQLite database:")
connection = create_connection("Assignment13.db")


# Execute predefined write queries
# Send the query as a parameter
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Execute predefined read queries
# Send the query as a parameter
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# String holds the query to create a table
create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  street TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip INTEGER
);
"""

create_book_table = """
CREATE TABLE IF NOT EXISTS book (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  isbn INTEGER,
  edition INTEGER,
  price FLOAT,
  publisher TEXT NOT NULL
);
  """


create_order_table = """
CREATE TABLE IF NOT EXISTS order (
 order_num INTEGER PRIMARY KEY AUTOINCREMENT,
 order_date TEXT NOT NULL,
 order_total INTEGER,
 customer_id INTEGER FOREIGN KEY AUTOINCREMENT
);
  """

create_orderLineItem_table = """
CREATE TABLE IF NOT EXISTS orderLineItem (
 order_num INTEGER FOREIGN KEY,
 book_id INTEGER FOREIGN KEY,
 quantity INTEGER
):
  """
# Execute the four queries to create the tables of the database

execute_query(connection, create_customer_table)
execute_query(connection, create_book_table)
# --------------------------------------------------#
# Everything above this line was to create the SQL Database
steady = 1
while steady == 1:
    request = int(input("""Main Menu:
    1. Customers
    2. Orders
    3. Books
    4. Exit"""))
    if request == 1:
        print("""Customer Menu:
        1. Add a new customer
        2. Modify an existing customer
        3. Print a list of all customers
        4. Delete a customer
        5. Return to Main Menu""")
        request2 = int(input())
        # asks the questions to create a new customer
        if request2 == 1:
            first = input("What is their first name?")
            last = input("What is their last name?")
            street = input("What is their street address?")
            city = input("What city do they live in?")
            state = input("What state do the live in(initials)?")
            zip = input("What is there zip code?")
            add_customer = f"""
            INSERT INTO
              customer (first_name, last_name, street, city, state, zip)
            VALUES
              ('{first}', '{last}', '{street}', '{city}', '{state}', '{zip}');
            """
            execute_query(connection, add_customer)
        # asks the questions to find and modify a customer
        elif request2 == 2:
            print("What would you like to modify?")
            print("""1. First name
            2. Last name
            3. address""")
            change = int(input())
            # modifies the first name of the customer
            if change == 1:
                print("What was their name?")
                oldname = input()
                print("What is their new name?")
                newname = input()
                update_customer_name = f"""
                UPDATE
                  customer
                SET
                  first_name = {newname}
                WHERE
                  first_name = {oldname}
                """
                execute_query(connection, update_customer_name)
            # modifies the last name of the customer
            elif change == 2:
                print("What was their name?")
                old_name = input()
                print("What is their new name?")
                new_name = input()
                update_customer_name = f"""
                UPDATE
                  customer
                SET
                  last_name = {new_name}
                WHERE
                  last_name = {old_name}
                """
                execute_query(connection, update_customer_name)
            # modifies the address of the customer
            elif change == 3:
                old_street = input("What was their old street address?")
                old_city = input("What was their old city?")
                old_state = input("What was their old state?(initials)")
                old_zip = input("What was there old zip code?")
                new_street = input("What is their new street address?")
                new_city = input("What is their new city?")
                new_state = input("What is their new state?(initials)")
                new_zip = input("What is there new zip code?")
                update_customer_address = f"""
                UPDATE
                    customer
                SET
                    street = {new_street}, city = {new_city}, state = {new_state}, zip = {new_zip}
                WHERE
                    street = {old_street}, city = {old_city}, state = {old_state}, zip = {old_zip}
                """
                execute_query(connection, update_customer_address)
        # prints list of all the customers in the table
        elif request2 == 3:
            select_customer = "SELECT * from customer"
            customers = execute_read_query(connection, select_customer)
            for customer in customers:
                print(customer)
        # finds and deletes a customer
        elif request2 == 4:
            del_customer = input("What is the name of the customer you would like to delete?")
            delete_customer = f"""
            DELETE FROM
                customer
            WHERE
                first_name = {del_customer}
            """
            execute_query(connection,delete_customer)
        elif request2 == 5:
            steady = 1
    if request == 2:
        print("""Order Menu:
        1. Add a new order
        2. Modify an existing order
        3. Print a list of all orders
        4. Delete an order
        5. Return to Main Menu""")
        request2 = int(input())
        # asks the questions to create a new order
        if request2 == 1:
            order_date = input("What is the date of the order?(mm/dd/yyyy)")
            order_total = input("What is the total price of the order?")
            add_order = f"""
            INSERT INTO
              order (order_date, order_total)
            VALUES
              ('{order_date}', '{order_total}');
            """
            execute_query(connection, add_order)
        # asks the questions to find and modify and order
        elif request2 == 2:
            print("What would you like to modify?")
            print("""1. Order date
            2. Order total""")
            change = int(input())
            if change == 1:
                print("What was the previous date?")
                oldDate = input()
                print("What is the new date?")
                newDate = input()
                update_order_date = f"""
                UPDATE
                  customer
                SET
                  first_name = {newDate}
                WHERE
                  first_name = {oldDate}
                """
                execute_query(connection, update_order_date)
            elif change == 2:
                print("What was the old price?")
                old_price = input()
                print("What is the new price?")
                new_price = input()
                update_order_price = f"""
                UPDATE
                  customer
                SET
                  last_name = {new_price}
                WHERE
                  last_name = {old_price}
                """
                execute_query(connection, update_order_price)
        # prints a list of all orders in the table
        elif request2 == 3:
            select_order = "SELECT * from order"
            orders = execute_read_query(connection, select_order)
            for order in orders:
                print(order)
        # deletes an order from the table
        elif request2 == 4:
            del_order = input("What is the date of the order you would like to delete?")
            delete_order = f"""
            DELETE FROM
                order
            WHERE
                order_date = {del_order}
            """
            execute_query(connection,delete_order)
        elif request2 == 5:
            steady = 1
    if request == 3:
        print("""Book Menu:
        1. Add a new book
        2. Modify an existing book
        3. Print a list of all books
        4. Delete a book
        5. Return to main menu""")
        request2 = int(input())
        # asks the questions to add a new book to the table
        if request2 == 1:
            title = input("What is the Title of the book?")
            author = input("Who is the author of the book?")
            isbn = input("What is the ISBN of the book?")
            edition = input("What edition is the book?")
            price = input("What is the price of the book(no $)?")
            publisher = input("Who is the publisher of the book?")
            add_book = f"""
            INSERT INTO
              book (title, author, isbn, edition, price, publisher)
            VALUES
              ('{title}', '{author}', '{isbn}', '{edition}', '{price}', '{publisher}');
            """
            execute_query(connection, add_book)
        # asks the questions to find and modify a book in the table
        elif request2 == 2:
            print("""What would you like to modify?
            1. Title
            2. Author
            3. ISBN
            4. Edition
            5. Price
            6. Publisher""")
            change = input()
            # changes the title of the book
            if change == 1:
                old_title = input("What was the old Title of the book?")
                new_title = input("What is the new Title of the book?")
                update_book_title = f"""
                UPDATE
                  book
                SET
                  title = {new_title}
                WHERE
                  title = {old_title}
                """
                execute_query(connection, update_book_title)
                # changes the author of the book
            elif change == 2:
                old_author = input("What was the old author of the book?")
                new_author = input("What is the new author of the book?")
                update_book_author = f"""
                UPDATE
                  book
                SET
                  author = {new_author}
                WHERE
                  author = {old_author}
                """
                execute_query(connection,update_book_author)
                # changes the isbn of the book
            elif change == 3:
                old_isbn = input("What was the old ISBN of the book?")
                new_isbn = input("What is the new ISBN of the book?")
                update_book_ISBN = f"""
                UPDATE
                    book
                SET
                    isbn = {new_isbn}
                WHERE
                    isbn = {old_isbn}
                """
                execute_query(connection, update_book_ISBN)
                # changes the edition of the book
            elif change == 4:
                old_edition = input("What was the old edition of the book?")
                new_edition = input("What is the new edition of the book?")
                update_book_edition = f"""
                UPDATE
                  book
                SET
                  edition = {new_edition}
                WHERE
                  edition = {old_edition}
                """
                execute_query(connection, update_book_edition)
                # changes the price of the book
            elif change == 5:
                old_price = input("What was the old price of the book?")
                new_price = input("What is the new price of the book?")
                update_book_price = f"""
                UPDATE
                  book
                SET
                  price = {new_price}
                WHERE
                  price = {old_price}
                """
                execute_query(connection, update_book_price)
                # changes the publisher of the book
            elif change == 6:
                old_pub = input("What was the old publisher of the book?")
                new_pub = input("What is the new publisher of the book?")
                update_book_publisher = f"""
                UPDATE
                  book
                SET
                  publisher = {new_pub}
                WHERE
                  publisher = {old_pub}
                """
                execute_query(connection, update_book_publisher)
                # prints list of all books in the table or in stock
        elif request2 == 3:
            select_book = "SELECT * from book"
            books = execute_read_query(connection, select_book)

            for book in books:
                print(book)
                # deletes book from table
        elif request2 == 4:
            del_book = input("What is the name of the book you would like to delete?")
            delete_book = f"""
            DELETE FROM
                book
            WHERE
                title = {del_book}
            """
            execute_query(connection,delete_book)
        elif request2 == 5:
            steady = 1
    if request == 4:
        steady = 0
