
# видалити всіх людей без посади


import sqlite3 as sq
import time
from random import choice, randint
from catalog import NAMES_SET, SURNAMES_SET, POSITIONS_SET, AGE_INTERVAL
from pprint import pprint


def create_table_people():
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        try:
            cursor.execute('''
                    CREATE TABLE people(
                    id INTEGER primary key not null,
                    name TEXT not null,
                    surname TEXT not null,
                    gender TEXT not null,
                    salary INTEGER,
                    position TEXT,
                    email TEXT,
                    age INTEGER not null 
                    );''')
        except sq.OperationalError:
            print('The table already exists')


def records_generator(number_of_records: int = 20):
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        for i in range(number_of_records):
            identifier = int(time.time()*10000)+i  # we must be sure that id always be unique
            name = choice(NAMES_SET)
            surname = choice(SURNAMES_SET)
            gender = choice(['male', 'female'])
            salary = choice([randint(10_000, 100_000), None])
            position = choice([choice(POSITIONS_SET), None])
            email = choice([str(f'{identifier}@ukr.net'), None])
            age = randint(*AGE_INTERVAL)

            cursor.execute(f"""
            INSERT INTO people VALUES ({identifier}, 
                                    '{name}', 
                                    '{surname}', 
                                    '{gender}', 
                                    ?, 
                                    ?,
                                    ?,
                                    '{age}');
                                    """, (salary, position, email))



def add_2_wachowski():
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        for i in range(2):
            identifier = int(time.time()*10000)+i  # we must be sure that id always be unique
            name = ['Laurence', 'Andrew']
            surname = "Wachowski"
            gender = 'male'
            salary = choice([randint(10_000, 100_000), None])
            position = choice([choice(POSITIONS_SET), None])
            email = choice([str(f'{identifier}@ukr.net'), None])
            age = randint(18, 80)

            cursor.execute(f"""
            INSERT INTO people VALUES ({identifier}, 
                                    '{name[i]}', 
                                    '{surname}', 
                                    '{gender}', 
                                    ?, 
                                    ?,
                                    ?,
                                    '{age}');
                                    """, (salary, position, email))


def amend_gender_for_wachowski_or_any_other_by_surname(surname: str = "Wachowski", new_gender: str = 'female'):
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"""
                    UPDATE people 
                    SET gender = '{new_gender}'
                    WHERE surname = '{surname}';""")


def amend_name_by_name_and_surname(name: str = 'Laurence', surname: str = "Wachowski", new_name: str = 'Lana'):
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"""
                    UPDATE people 
                    SET name = '{new_name}'
                    WHERE name = '{name}' AND surname = '{surname}';""")


def fill_empty_emails():
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"""
                    UPDATE people 
                    SET email = (SELECT name || '_' || surname || '@ukr.net')
                    WHERE email IS NULL;""")


def choose_people_by_salary(salary: int = 10_000):
    """
    :param salary: more than
    """
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        data = tuple(cursor.execute(f"""
                    SELECT name, surname, salary
                    FROM people  
                    WHERE salary > {salary};"""))

        print(f'Data for people with salary > {salary}')

        if data:
            for row in data:
                print(data.index(row)+1, *row)
        else:
            print("No data with your parameters")

        print()

def choose_people_by_salary_and_age(salary: int = 10_000, age: int = 25):
    """
    :param salary: equal to
    :param age: older than
    """
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        data = tuple(cursor.execute(f"""
                    SELECT name, surname, salary
                    FROM people  
                    WHERE salary = {salary} AND age > {age};"""))

        print(f'Data for people with salary = {salary} and age > {age}')

        if data:
            for row in data:
                print(data.index(row)+1, *row)
        else:
            print("No data with your parameters")

        print()

def delete_records_by_empty_field(empty_field: str = 'position'):
    with sq.connect('my_database.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f"""
                    DELETE
                    FROM people
                    WHERE {empty_field} IS NULL;""")


if __name__ == "__main__":
    print("This is work module for main running file")

