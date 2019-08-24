import os
import glob
from pprint import pprint

AMOUNT = 0
STRING = 1
DATE = 3

DBSpec = {
    'DataDir': '../fec-data',
    'DataDirPattern' : 'data/*',
    'FieldSeparator' : '|',
    'Tables': {
        # Contributions by Individuals
        'CBI': {
            'ZipPattern' : '*.zip',
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
            'ZipPattern' : '*.zip',
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
            'ZipPattern' : '*.zip',
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
            'ZipPattern' : '*.zip',
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
            'ZipPattern' : '*.zip',
            'FilePattern' : 'weball*.txt',
            'Fields' : {}
        },
        # House/Sentate Current Campaigns
        'HSCC' : {
            'ZipPattern' : 'weball*.zip',
            'FilePattern' : '*.txt',
            'Fields' : {}
        },
        # PAC Summary
        'PAC' : {
            'ZipPattern' : '*.zip',
            'FilePattern' : 'webk*.txt',
            'Fields' : {}
        },
        # Contributions from committees to candidates & independent expenditures
        'CFC' : {
            'ZipPattern' : '*.zip',
            'FilePattern' : 'pas*.txt',
            'Fields' : {}
        },
        # Any transaction from one committee to another
        'TFC' : {
            'ZipPattern' : '*.zip',
            'FilePattern' : 'oth*.txt',
            'Fields' : {}
        },
        # Operating expenditures
        'OE' : {
            'ZipPattern' : '*.zip',
            'FilePattern' : 'oppexp*.txt',
            'Fields' : {}
        }
    }
}
        

class DBConfig:
    def __init__(self):
        pass

    @staticmethod
    def getArchives(table):
        pattern = os.path.join(DBConfig.getDataDirPattern(),
                               DBSpec['Tables'][table]['ZipPattern'])
        archives = glob.glob(pattern)
        return archives

    @staticmethod
    def getDataDic(table):
        return DBSpec['Tables'][table]['Fields']

    @staticmethod
    def getDataDir():
        return DBSpec['DataDir']

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
    def getFilesAndArchives(table):
        files = DBConfig.getFiles(table)
        archives = DBConfig.getArchives(table)
        return files + archives

    @staticmethod
    def getSep():
        return DBSpec['FieldSeparator']


def tests():
    table = 'CANDIDATE'
    pprint(DBConfig.getDataDic(table))
    pprint(DBConfig.getFieldIndex(table))
    pprint(DBConfig.getFilesAndArchives(table))

if __name__ == '__main__':
    tests()
