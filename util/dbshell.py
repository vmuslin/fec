import sqlite3

from sqlite_wrapper import SQLite

def db_shell(conn):

    cur = conn.cursor()

    buffer = ""

    print("Enter your SQL commands to execute in sqlite3.")
    print("Enter a blank line to exit.")

    while True:
        line = input('SQL> ')
        if line == "":
            break
        buffer += line
        if sqlite3.complete_statement(buffer):

            try:
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT"):
                    for row in cur.fetchall():
                        print(row)

            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])

            buffer = ""


def main():
    conn = SQLite.create_connection('./FEC.db')
    db_shell(conn)
    conn.close()


if __name__ == '__main__':
    main()
