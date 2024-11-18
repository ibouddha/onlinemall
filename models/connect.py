import psycopg2


def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="onlinemall",
            user="bouddha",
            password="logyouin",
            host="localhost",
        )
        print("Connected to PostgreSQL database")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    return conn


def close_connection(conn):
    if conn is not None:
        conn.close()
        print("PostgreSQL connection is closed")
    