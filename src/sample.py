import psycopg2

my_connection = psycopg2.connect(
    host="localhost",
    dbname="db",
    user="postgres",
    password="postgres",
    port=5432,
)

my_cursor = my_connection.cursor()

my_cursor.execute("""
                  create schema if not exists mdm;
                  """)


my_cursor.execute(
    """CREATE TABLE IF NOT EXISTS mdm.person(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    email VARCHAR(50),
                    phone VARCHAR(50),
                    address VARCHAR(50),
                    city VARCHAR(50),
                    state VARCHAR(50),
                    zip VARCHAR(50)
                    );
    """
)

my_cursor.execute("""
INSERT INTO mdm.person (first_name, last_name, email, phone, address, city, state, zip)
VALUES ('John', 'Doe', 'no.one@nowhere.com', '555-555-5555', '123 Main St', 'Anytown', 'AK', '00053');
"""
)

my_connection.commit()

my_cursor.close()

my_connection.close()
