import sys
import glob
import os
import os.path
import time

import sqlite3
from sqlite3 import Error
from collections import namedtuple

from datadic import DataDic
from sqlite_wrapper import SQLite
from dbconfig import Tables
 

class Fec:

    def __init__(self, database, filepath):
        self.database = database
        self.filepath = filepath
        self.datadic = DataDic(Tables, self.filepath)


    @property
    def tables(self):
        return self.datadic.tables


    def bulkload_db(self, conn, batch_size=10000, max_rows=None):

        for table in self.tables:
            filenames = self.datadic.get_filenames(table)
            if filenames is not None:
                for filename in filenames:
                    self.bulkload_table(conn, table, filename, batch_size, max_rows)
                    conn.commit()


    @staticmethod
    def seconds_since_epoch(day, month, year, year_increase=0):
        return int(time.mktime((int(year)+year_increase,
                                int(month),
                                int(day),
                                0, 0, 0, 0, 0, 0)))
    

    def bulkload_table(self, conn, table, filename, batch_size=10000, max_rows=None):

        print('Loading %s into %s' % (filename, table))
        columns = self.datadic.get_columns(table)

        c = conn.cursor()
        
        with open(filename) as file:
            nrows = 0
            rows = []
            insert_statement = self.datadic.insert_stmt(table, filename=filename)

            for row in file:

                if max_rows is not None:
                    if nrows == max_rows:
                        break;

                nrows += 1

                try:
                    split_row = row[:-1].split('|')[:len(self.datadic.get_columns(table))]

                    for col in range(len(split_row)):
                        column = columns[col]

                        if column.datatype == 'MONEY':
                            split_row[col] = self.process_money_field(split_row[col])

                        elif column.datatype == 'DATE':
                            split_row[col] = self.process_date_field(split_row[col])

                except ValueError as e:
                    print('Load error!')
                    print('Row #%d = %s' % (nrows, row[:-1]))
                    print('Col #%d/%s = %s' % (col, column.name, split_row[col]))
                    raise e

                rows.append(split_row)
                if nrows % batch_size == 0: 
                    c.executemany(insert_statement, rows)
                    conn.commit()
                    rows = []
                    print('Inserted %d rows' % nrows)

            if rows:
                c.executemany(insert_statement, rows)

            conn.commit()
            print('Final: Inserted %d rows' % nrows)

        
    def process_money_field(self, field):
        if field:
            return int(float(field) * 100) # Store money amounts in cents
        else:
            return 0


    def process_date_field(self, field):
        field_len = len(field)

        if '/' in field:
            month, day, year = field.split('/')
            if field_len == 10:  # Assume format MM/DD/YYYY
                return self.seconds_since_epoch(day, month, year)
            elif field_len == 8: # Assume format MM/DD/YY
                return self.seconds_since_epoch(day, month, year, 2000)
            else:
                return 0
        else:
            if field_len == 8: # Assume format MMDDYYYY
                return self.seconds_since_epoch(day=field[2:4],
                                                month=field[0:2],
                                                year=field[4:])
            elif field_len == 6: # Assume format MMDDYY
                return self.seconds_since_epoch(day=field[2:4],
                                                month=field[0:2],
                                                year=field[4:],
                                                year_increase=2000)
            else:
                return 0


    def create_connection(self):
        return SQLite.create_connection(self.database)


    def create_tables_and_views(self, conn):

        c = conn.cursor()

        for table in self.tables:
            filenames = self.datadic.get_filenames(table)

            if filenames is not None:
                for filename in filenames:
                    sql = self.datadic.create_table_stmt(table, filename=filename)
                    print(sql)
                    c.execute(sql)
                sql = self.datadic.create_view_stmt(table, filenames)
                print(sql)
                c.execute(sql)
            else:
                sql = self.datadic.create_table_stmt(table, filename=filename)
                print(sql)
                c.execute(sql)

        self.datadic.create_v_individual_contributions_to_candidates('icontributions')

        conn.commit()


def test():

    database = '../data/fec/FEC.db'
    datasets = '../data/fec/*'

    print('Creating database %s and loading from %s' % (database, datasets))

    db = Fec(database, datasets)

    conn = db.create_connection()

    if conn is not None:
        db.create_tables_and_views(conn)
        db.bulkload_db(conn, 10000, 3)
        #dbshell.db_shell(conn)

    conn.close()


if __name__ == '__main__':
    test()
