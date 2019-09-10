import sqlite3

class SQLite:

    def __init__(self):
        pass


    @staticmethod
    def create_connection(database):
        ''' create a database connection to a SQLite database '''
        conn = None
        try:
            # Note that filename ':memory:' creates a database in RAM
            #conn = sqlite3.connect(db_file)
            with sqlite3.connect(database) as conn:
                print(sqlite3.version)
        except Error as e:
            print(e)

        # finally:
        #   if conn:
        #       conn.close()

        return conn
