# create a database for a hospital, make these tables: patients, doctors & medicine
# patients have a name, email, telephone & a family doctor assigned
# doctors have a name & specialty
# medicine has a name, type & number of items in stock
# create method for removing an amount of medicine from stock
# create methods for adding a medicine, patient & doctors
# create method for removing patient & doctors
# create method for listing all medicines & doctors

import sqlite3

def connect_to_database():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    return connection, cursor


def execute_sql(commands: list[str]):
    connection, cursor = connect_to_database()
    for one_command in commands:
        cursor.execute(one_command)
    connection.commit()  # we save to the system
    connection.close()  # we close so other processes can write


def init_database():
    commands = []
    commands.append("CREATE TABLE patients ('name' TEXT, 'doctor' TEXT)")
    commands.append("CREATE TABLE doctors ('name' TEXT, 'specialty' TEXT)")
    commands.append("CREATE TABLE medicine('name' TEXT, 'items' INTEGER)")
    execute_sql(commands)
    # look at add_medicine, the above can be written in the same way = the same thing but written differently

#  BELOW is the code would look like if execute_sql was not defined above
# def init_database():
#     connection = sqlite3.connect("hospital.db")
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE patients ('name' TEXT, 'doctor' TEXT)")
#     cursor.execute("CREATE TABLE doctors ('name' TEXT, 'specialty' TEXT)")
#     cursor.execute("CREATE TABLE medicine('name' TEXT, 'items' INTEGER)")
#     connection.commit() # we save to the system
#     connection.close() # we close so other processes can write


# init_database()

def add_medicine(name: str, items: int):
    commands = ["INSERT INTO medicine ('name', 'items') VALUES ('" +  name + "', " + str(items) + ")"]
    execute_sql(commands)

#  BELOW is the code that was written before execute_sql

# def add_medicine(name: str, items: int):
#     connection = sqlite3.connect("hospital.db")
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO medicine ('name', 'items') VALUES ('" +  name + "', " + str(items) + ")")
#     connection.commit()
#     connection.close()


add_medicine("parasinus", 300)

def take_medicine(name: str, items_to_remove: int):
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM medicine WHERE name = '" + name + "'")
    medicine = cursor.fetchone()
    connection.close()
    current_items = medicine[1]
    print(current_items)
    current_items -= items_to_remove
    execute_sql(["UPDATE medicine SET items=" + str(current_items) + " WHERE name= '" + name + "'"])


def get_all_medicine() -> list[str]:
    connection, cursor = connect_to_database()
    cursor.execute("SELECT name FROM medicine")
    medicines = cursor.fetchall()
    connection.close()
    print(medicines)
    return medicines




get_all_medicine()


# take_medicine("nurofen", 10)