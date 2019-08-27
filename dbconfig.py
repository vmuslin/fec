import os
import glob
from pprint import pprint

AMOUNT = 0
STRING = 1
DATE = 3

DBSpec = {
    'DataDirPattern': None,
    'FieldSeparator' : '|',
    'Tables': {
        # Contributions by Individuals
        'CBI': {
            'FilePattern' : 'itcont*.txt',
            'Fields' : (('CMTE_ID', STRING),
                        ('AMNDT_IND', STRING),
                        ('RPT_TP', STRING),
                        ('TRANSACTION_PGI', STRING),
                        ('IMAGE_NUM', STRING),
                        ('TRANSACTION_TP', STRING),
                        ('ENTITY_TP', STRING),
                        ('NAME', STRING),
                        ('CITY', STRING),
                        ('STATE', STRING),
                        ('ZIP_CODE', STRING),
                        ('EMPLOYER', STRING),
                        ('OCCUPATION', STRING),
                        ('TRANSACTION_DT', DATE),
                        ('TRANSACTION_AMT', AMOUNT),
                        ('OTHER_ID', STRING),
                        ('TRAN_ID', STRING),
                        ('FILE_NUM', STRING),
                        ('MEMO_CD', 'NUMBER'),
                        ('MEMO_TEXT', STRING),
                        ('SUB_ID', 'NUMBER'))
        },
        # Candidate Master
        'CANDIDATE' : {
            'FilePattern' : 'cn*.txt',
            'Fields' : (('CAND_ID', STRING),
                        ('CAND_NAME', STRING),
                        ('CAND_PTY_AFFILIATION', STRING),
                        ('CAND_ELECTION_YR', STRING),
                        ('CAND_OFFICE_ST', STRING),
                        ('CAND_OFFICE', STRING),
                        ('CAND_OFFICE_DISTRICT', STRING),
                        ('CAND_ICI', STRING),
                        ('CAND_STATUS', STRING),
                        ('CAND_PCC', STRING),
                        ('CAND_ST1', STRING),
                        ('CAND_ST2', STRING),
                        ('CAND_CITY', STRING),
                        ('CAND_ST', STRING),
                        ('CAND_ZIP', STRING))
        },
        # Candidate Committee Linkage
        'CCL' : {
            'FilePattern' : 'ccl*.txt',
            'Fields' : (('CAND_ID', STRING),
                        ('CAND_ELECTION_YR', STRING),
                        ('FEC_ELECTION_YR', STRING),
                        ('CMTE_ID', STRING),
                        ('CMTE_TP', STRING),
                        ('CMTE_DSGN', STRING),
                        ('LINKAGE_ID', STRING))
        },
        # Committee Master
        'COMMITTEE' : {
            'FilePattern' : 'cm*.txt',
            'Fields' : (('CMTE_ID', STRING),
                        ('CMTE_NM', STRING),
                        ('TRES_NM', STRING),
                        ('CMTE_ST1', STRING),
                        ('CMTE_ST2', STRING),
                        ('CMTE_CITY', STRING),
                        ('CMTE_ST', STRING),
                        ('CMTE_ZIP', STRING),
                        ('CMTE_DSGN', STRING),
                        ('CMTE_TP', STRING),
                        ('CMTE_PTY_AFFILIATION', STRING),
                        ('CMTE_FILING_FREQ', STRING),
                        ('ORG_TP', STRING),
                        ('CONNECTED_ORG_NM', STRING),
                        ('CAND_ID', STRING))
        },
        # All Candidates
        'ALL' : {
            'FilePattern' : 'weball*.txt',
            'Fields' : {}
        },
        # House/Sentate Current Campaigns
        'HSCC' : {
            'FilePattern' : '*.txt',
            'Fields' : {}
        },
        # PAC Summary
        'PAC' : {
            'FilePattern' : 'webk*.txt',
            'Fields' : {}
        },
        # Contributions from committees to candidates & independent expenditures
        'CFC' : {
            'FilePattern' : 'pas*.txt',
            'Fields' : {}
        },
        # Any transaction from one committee to another
        'TFC' : {
            'FilePattern' : 'oth*.txt',
            'Fields' : {}
        },
        # Operating expenditures
        'OE' : {
            'FilePattern' : 'oppexp*.txt',
            'Fields' : {}
        }
    }
}
        

class DBConfig:
    def __init__(self):
        pass

    @staticmethod
    def getDataDic(table):
        return DBSpec['Tables'][table]['Fields']

    @staticmethod
    def getDataDirPattern():
        return DBSpec['DataDirPattern']

    @staticmethod
    def getFieldIndex(table): # dictionary { field_name : (index, datatype) }
        index = {}
        for count, tup in enumerate(DBConfig.getDataDic(table)):
            name = tup[0]
            datatype = tup[1]
            index[name] = (count, datatype)
        return index

    @staticmethod
    def getFilePattern(table):
        return DBSpec['Tables'][table]['FilePattern']

    @staticmethod
    def getFiles(table):
        pattern = os.path.join(DBConfig.getDataDirPattern(),
                               DBConfig.getFilePattern(table))
        files =  glob.glob(pattern)
        return files

    @staticmethod
    def getSep():
        return DBSpec['FieldSeparator']

    @staticmethod
    def setDataDirPattern(pattern):
        DBSpec['DataDirPattern'] = pattern


def tests():
    table = 'CANDIDATE'
    DBConfig.setDataDirPattern(os.path.join('..', 'data', 'fec-data', '*'))
    pprint(DBConfig.getDataDic(table))
    pprint(DBConfig.getFieldIndex(table))
    pprint(DBConfig.getFiles(table))

if __name__ == '__main__':
    tests()
