import os.path
import glob

class DataDic:

    def __init__(self, datadic, filepath=None):
        self.datadic = datadic
        if filepath:
            self.filepath = os.path.join(*filepath.split('/'))
        else:
            self.filepath = '.'

        self.filenames = {}
        for table in datadic:
             if 'filenames' in datadic[table]:
                 self.filenames[table] = glob.glob(os.path.join(self.filepath, self.datadic[table]['filenames']))
             else:
                self.filenames[table] = None


    @property
    def tables(self):
        for table in self.datadic:
            if table[0] != '#':
                yield table


    def get_columns(self, table):
        return self.datadic[table]['columns']


    def get_dataset(self, filename):
        return os.path.basename(os.path.dirname(filename)).replace('-', '_')


    def get_tablename(self, table, filename):
        return table + '_' + self.get_dataset(filename)

    
    def get_filenames(self, table):
        return self.filenames[table]


    def real_tablename(self, table, filename=None, suffix=None):
        if filename is not None:
            return self.get_tablename(table, filename)
        elif suffix is not None:
            return table + suffix
        else:
            return table


    def create_table_stmt(self, table, filename=None, suffix=None):
        s = 'CREATE TABLE IF NOT EXISTS %s (\n' % self.real_tablename(table, filename, suffix)
        for column in self.get_columns(table):
            if column.datatype == 'DATE':
                column = [column.name, 'INTEGER', column.other, column.nullable]
            elif column.datatype == 'MONEY':
                column = [column.name, 'INTEGER', column.other, column.nullable]
            else:
                column = [column.name, column.datatype, column.other, column.nullable]
            s += '\t' + ' '.join(column) + ',\n'
        s = s[:-2] + ');'

        return s
    

    def create_view_stmt(self, table, filenames):
        s = 'CREATE VIEW IF NOT EXISTS %s (\n' % table

        sel = ''
        for column in self.get_columns(table):
            s += '\t%s,\n' % column.name
            sel += '\t%s,\n' % column.name
        s = s[:-2] + ') AS\n'
        sel = sel[:-2]

        for filename in filenames:
            s += 'SELECT %s\nFROM %s\nUNION ALL\n'  % (sel, self.real_tablename(table, filename))
        s = s[:-10]

        return s
        

    def create_v_individual_contributions_to_candidates(self, table):
        s = 'CREATE VIEW IF NOT EXISTS v_individual_contributions_to_candidates AS '

        i = 0
        for file in self.get_filenames(table):
            if i > 0:
                s += 'UNION ALL\n';
                i += 1
            
            dataset = self.get_dataset(file)

            s += '''
            SELECT
              i.cmte_id,
              m.cand_id,
              m.cand_name,
              c.cmte_name,
              i.name,
              i.city,
              i.state,
              i.zip_code,
              i.employer,
              i.occupation,
              i.transaction_amt,
              i.transaction_dt
            FROM
              icontributions_%s i
              LEFT JOIN committees_%s c ON i.cmte_id = c.cmte_id
              LEFT JOIN cc_linkages_%s l ON c.cmte_id = l.cmte_id
              LEFT JOIN candidate_master_%s m ON l.cand_id = m.cand_id
            ''' % (dataset, dataset, dataset, dataset)

        return s


    def insert_stmt(self, table, filename=None, suffix=None):
        return ('INSERT INTO %s VALUES(' % self.real_tablename(table, filename, suffix)) + \
                '?,' * (len(self.get_columns(table))-1) + '?)'


if __name__ == '__main__':
    from dbconfig import Tables
    db = DataDic(Tables, '../data/fec/*')

    for t in db.tables:

        for f in db.get_filenames(t):
            print('--- Table: %s (%d columns) ---' % (t, len(db.get_columns(t))))
            print(db.create_table_stmt(t, f))
            print(db.insert_stmt(t))
            print('')
            
        print('--- View %s ---' % t)
        print(db.create_view_stmt(t, db.get_filenames(t)))
        print('')

    print('--- View v_individual_contributions_to_candidates ---')
    print(db.create_v_individual_contributions_to_candidates('icontributions'))
