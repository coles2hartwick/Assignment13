# Sam Cole
# 4/30/2020

import sqlite3
from sqlite3 import Error


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
connection = create_connection("myDatabase")


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
  id INTEGER PRIMARY KEY AUTOINCREMENT,
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
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  isbn INTEGER,
  edition INTEGER,
  price FLOAT,
  publisher TEXT NOT NULL
);
  """

create_book = """
INSERT INTO 
  book (title, author, isbn, edition, price, publisher)
VALUES
  ('Waterland', 'Graham Swift', 0434753300, 1, 16.95, 'William Heinemann')
"""

# String holds the query to add data to the table
create_customers = """
INSERT INTO
  customer (first_name, last_name, street, city, state, zip)
VALUES
  ('James', 'Smith', '969 North Creek Dr.', 'Hyde Park', 'MA', 02136),
  ('Leila', 'Jones', '9570 Overlook St.', 'Cleveland', 'TN', 37312),
  ('Brigitte', 'Griffing', '134 Pulaski St.', 'Winter Park' , 'FL', 32792),
  ('Mike', 'Colameco', '1 Willow Drive', 'Powder Springs', 'GA', 30127),
  ('Elizabeth', 'McGovern', '558 West Bowman St.', 'Bowling Green', 'KY', 42101);
"""

# Execute the four queries to create the tables of the database

execute_query(connection, create_customer_table)
execute_query(connection, create_customers)
execute_query(connection, create_book_table)
execute_query(connection, create_book)

#--------------------------------------------------#
# Everything above this line was to create the SQL Database
steady = 1
while steady == 1:
    print("""Main Menu:
    1. Customers
    2. Books
    3. Exit""")
    request = input()
    if request == 1:
        print("""Customer Menu:
        1. Add a new customer
        2. Modify an existing customer
        3. Print a list of all customers
        4. Delete a customer
        5. Return to Main Menu""")
        request2 = input
        if request2 == 1:


print("\nLet's see what's in the people table:")

# Create a query to return data from the users table
select_people = "SELECT * from person"
people = execute_read_query(connection, select_people)

for person in people:
    print(person)


# Turns out that Elizabeth McGovern married James Smith, need to change her name
print("\n\nLet's change Elizabeth McGovern's last name to Smith and print all Smith's")
update_person_name = """
UPDATE
  person
SET
  last_name = 'Smith'
WHERE
  last_name = 'McGovern'
"""

execute_query(connection, update_person_name)

select_people = "SELECT * from person WHERE last_name == 'Smith'"
smiths = execute_read_query(connection, select_people)
print(smiths)


# Let's add two more people to the database
add_people = """
INSERT INTO
  person (first_name, last_name, age)
VALUES
  ('Johnny', 'Corona-Virus', 20),
  ('Alex', 'A', 21);
"""
