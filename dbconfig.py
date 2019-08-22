import os
import glob
from pprint import pprint

AMOUNT = 0
STRING = 1
DATE = 3

DBConfig = {
    'DataDir': 'data/2019-2020',
    'DataDirPattern' : 'data/*',
    'FieldSeparator' : '|',
    'Tables': {
        # Contributions by Individuals
        'CBI': {
            'ZipPattern' : 'indiv*.zip',
            'FilePattern' : 'itcont*.txt',
            'Path' : 'itcont.txt',
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
            'ZipPattern' : 'cn*.zip',
            'FilePattern' : 'cn*.txt',
            'Path' : 'cn.txt',
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
            'ZipPattern' : 'ccl*.zip',
            'FilePattern' : 'ccl*.txt',
            'Path' : 'ccl.txt',
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
            'ZipPattern' : 'cm*.zip',
            'FilePattern' : 'cm*.txt',
            'Path' : 'cm.txt',
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
            'ZipPattern' : 'weball*.zip',
            'FilePattern' : 'itcont*.txt',
            'Path' : 'itcont.txt',
            'Fields' : {}
        },
        # House/Sentate Current Campaigns
        'HSCC' : {
            'ZipPattern' : 'weball*.zip',
            'FilePattern' : '*.txt',
            'Path' : '.txt',
            'Fields' : {}
        },
        # PAC Summary
        'PAC' : {
            'ZipPattern' : 'webk*.zip',
            'FilePattern' : '*.txt',
            'Path' : '.txt',
            'Fields' : {}
        },
        # Contributions from committees to candidates & independent expenditures
        'CFC' : {
            'ZipPattern' : 'pas*.zip',
            'FilePattern' : '*.txt',
            'Path' : 'itcont.txt',
            'Fields' : {}
        },
        # Any transaction from one committee to another
        'TFC' : {
            'ZipPattern' : 'oth*.zip',
            'FilePattern' : '*.txt',
            'Path' : '.txt',
            'Fields' : {}
        },
        # Operating expenditures
        'OE' : {
            'ZipPattern' : 'oppexp*.zip',
            'FilePattern' : '*.txt',
            'Path' : '.txt',
            'Fields' : {}
        }
    }
}
        

class DBConfig:
    def __init__(self):
        pass

    @staticmethod
    def getArchives(table):
        pattern = os.path.join(Config.getDataDirPattern(),
                               FileConfig['Tables'][table]['ZipPattern'])
        archives = glob.glob(pattern)
        return archives

    @staticmethod
    def getDataDic(table):
        return FileConfig['Tables'][table]['Fields']

    @staticmethod
    def getDataDir():
        return FileConfig['DataDir']

    @staticmethod
    def getDataDirPattern():
        return FileConfig['DataDirPattern']

    @staticmethod
    def getFieldIndex(table): # dictionary { field_name : (index, datatype) }
        index = {}
        for count, tup in enumerate(Config.getDataDic(table)):
            name = tup[0]
            datatype = tup[1]
            index[name] = (count, datatype)
        return index

    @staticmethod
    def getFilePattern(table):
        return FileConfig['Tables'][table]['FilePattern']

    @staticmethod
    def getFiles(table):
        pattern = os.path.join(Config.getDataDirPattern(),
                               Config.getFilePattern(table))
        files =  glob.glob(pattern)
        return files

    @staticmethod
    def getFilesAndArchives(table):
        files = Config.getFiles(table)
        archives = Config.getArchives(table)
        return files + archives

    @staticmethod
    def getPath(table):
        return os.path.join(Config.getDataDir(),
                            FileConfig['Tables'][table]['Path'])

    @staticmethod
    def getSep():
        return FileConfig['FieldSeparator']


def tests():
    table = 'CANDIDATE'
    pprint(Config.getDataDic(table))
    pprint(Config.getFieldIndex(table))
    pprint(Config.getFilesAndArchives(table))

if __name__ == '__main__':
    tests()
