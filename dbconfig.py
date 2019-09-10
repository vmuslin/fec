from collections import namedtuple

Column = namedtuple('Column', 'name datatype nullable other')

Tables = {
            
    # FEC Data
    #
    # A table is skipped if hash sign (#) is the first character
            
    #----------------------------------------------------------------------
    # Campaigns Table

    'campaigns' : {
        'filenames' : 'webl*.txt',
        'columns' : (
            Column('cand_id', 'TEXT', 'NOT NULL', ''),
            Column('cand_name', 'TEXT', '', ''),
            Column('cand_ici', 'TEXT', '', ''),
            Column('pty_cd', 'TEXT', '', ''),
            Column('cand_pty_affiliation', 'TEXT', '', ''),
            Column('ttl_receipts', 'MONEY', '', ''),
            Column('trans_from_auth', 'MONEY', '', ''),
            Column('ttl_disb', 'MONEY', '', ''),
            Column('trans_to_auth', 'MONEY', '', ''),
            Column('coh_bop', 'MONEY', '', ''),
            Column('coh_cop', 'MONEY', '', ''),
            Column('cand_contrib', 'MONEY', '', ''),
            Column('cand_loans', 'MONEY', '', ''),
            Column('other_loans', 'MONEY', '', ''),
            Column('cand_loan_repay', 'MONEY', '', ''),
            Column('other_loan_repay', 'MONEY', '', ''),
            Column('debts_owed_by', 'MONEY', '', ''),
            Column('ttl_indiv_contrib', 'MONEY', '', ''),
            Column('cand_office_st', 'TEXT', '', ''),
            Column('cand_office_district', 'TEXT', '', ''),
            Column('spec_election', 'TEXT', '', ''),
            Column('prim_election', 'TEXT', '', ''),
            Column('run_election', 'TEXT', '', ''),
            Column('gen_election', 'TEXT', '', ''),
            Column('gen_election_precent', 'INTEGER', '', ''),
            Column('other_pol_cmte_contrib', 'MONEY', '', ''),
            Column('pol_pty_contrib', 'MONEY', '', ''),
            Column('cvg_end_dt', 'DATE', '', ''),
            Column('indiv_refunds', 'TEXT', '', ''),
            Column('cmte_refunds', 'TEXT', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Candidates Table

    'candidates' :
    {
        'filenames' : 'weball*.txt',
        'columns' : (
            Column('cand_id', 'TEXT', 'NOT NULL', ''),
            Column('cand_name', 'TEXT', '', ''),
            Column('cand_ici', 'TEXT', '', ''),
            Column('pty_cd', 'TEXT', '', ''),
            Column('cand_pty_affiliation', 'TEXT', '', ''),
            Column('ttl_receipts', 'MONEY', '', ''),
            Column('trans_from_auth', 'MONEY', '', ''),
            Column('ttl_disb', 'MONEY', '', ''),
            Column('trans_to_auth', 'MONEY', '', ''),
            Column('coh_bop', 'MONEY', '', ''),
            Column('coh_cop', 'MONEY', '', ''),
            Column('cand_contrib', 'MONEY', '', ''),
            Column('cand_loans', 'MONEY', '', ''),
            Column('other_loans', 'MONEY', '', ''),
            Column('cand_loan_repay', 'MONEY', '', ''),
            Column('other_loan_repay', 'MONEY', '', ''),
            Column('debt_owed_by', 'MONEY', '', ''),
            Column('ttl_indiv_contrib', 'MONEY', '', ''),
            Column('cand_office_st', 'TEXT', '', ''),
            Column('cand_ffice_district', 'TEXT', '', ''),
            Column('spec_election', 'TEXT', '', ''),
            Column('prim_election', 'TEXT', '', ''),
            Column('run_election', 'TEXT', '', ''),
            Column('get_election', 'TEXT', '', ''),
            Column('gen_election_precent', 'INTEGER', '', ''),
            Column('other_pol_cmte_contrib', 'MONEY', '', ''),
            Column('pol_pty_contrib', 'MONEY', '', ''),
            Column('cvg_end_dt', 'DATE', '', ''),
            Column('indiv_refunds', 'MONEY', '', ''),
            Column('cmte_refunds', 'MONEY', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Candidate Committee Linkages Table

    'cc_linkages' :
    {
        'filenames' : 'ccl*.txt',
        'columns' : (
            Column('cand_id', 'TEXT', 'NOT NULL', ''),
            Column('cand_election_yr', 'INTEGER', 'NOT NULL', ''),
            Column('fec_election_yr', 'INTEGER', 'NOT NULL', ''),
            Column('cmte_id', 'TEXT', '', ''),
            Column('cmte_tp', 'TEXT', '', ''),
            Column('cmte_dsgn', 'TEXT', '', ''),
            Column('linkage_id', 'INTEGER', 'NOT NULL', '')
        )
    },

    #----------------------------------------------------------------------
    # Candidate Master Table

    'candidate_master' :
    {
        'filenames' : 'cn*.txt',
        'columns' : (
            Column('cand_id', 'TEXT', 'NOT NULL', ''),
            Column('cand_name', 'TEXT', '', ''),
            Column('cand_pty_affiliation', 'TEXT', '', ''),
            Column('cand_election_yr', 'TEXT', '', ''),
            Column('cand_office_st', 'TEXT', '', ''),
            Column('cand_office', 'TEXT', '', ''),
            Column('cand_office_district', 'TEXT', '', ''),
            Column('cand_ici', 'TEXT', '', ''),
            Column('cand_status', 'TEXT', '', ''),
            Column('cand_pcc', 'TEXT', '', ''),
            Column('cand_st1', 'TEXT', '', ''),
            Column('cand_st2', 'TEXT', '', ''),
            Column('cand_city', 'TEXT', '', ''),
            Column('cand_st', 'TEXT', '', ''),
            Column('cand_zip', 'TEXT', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Committees Table

    'committees' :
    {
        'filenames' : 'cm*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('cmte_name', 'TEXT', '', ''),
            Column('tres_name', 'TEXT', '', ''),
            Column('cmte_st1', 'TEXT', '', ''),
            Column('cmte_st2', 'TEXT', '', ''),
            Column('cmte_city', 'TEXT', '', ''),
            Column('cmte_st', 'TEXT', '', ''),
            Column('cmte_zip', 'TEXT', '', ''),
            Column('cmte_dsgn', 'TEXT', '', ''),
            Column('cmte_tp', 'TEXT', '', ''),
            Column('cmte_pty_affiliation', 'TEXT', '', ''),
            Column('cmte_filing_freq', 'TEXT', '', ''),
            Column('org_tp', 'TEXT', '', ''),
            Column('connected_org_nm', 'TEXT', '', ''),
            Column('cand_id', 'TEXT', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Committee Contributions Table
    
    'ccontributions' :
    {
        'filenames' : 'itpas2*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('amndt_ind', 'TEXT', '', ''),
            Column('rpt_tp', 'TEXT', '', ''),
            Column('transaction_pgi', 'TEXT', '', ''),
            Column('image_num', 'TEXT', '', ''),
            Column('transaction_tp', 'TEXT', '', ''),
            Column('entity_tp', 'TEXT', '', ''),
            Column('name', 'TEXT', '', ''),
            Column('city', 'TEXT', '', ''),
            Column('state', 'TEXT', '', ''),
            Column('zip_code', 'TEXT', '', ''),
            Column('employer', 'TEXT', '', ''),
            Column('occupation', 'TEXT', '', ''),
            Column('transaction_dt', 'DATE', '', ''),
            Column('transaction_amt', 'MONEY', '', ''),
            Column('other_id', 'TEXT', '', ''),
            Column('cand_id', 'TEXT', '', ''),
            Column('tran_id', 'TEXT', '', ''),
            Column('file_num', 'INTEGER', '', ''),
            Column('memo_cd', 'TEXT', '', ''),
            Column('memo_tet', 'TEXT', '', ''),
            Column('sub_id', 'INTEGER', 'NOT NULL', '')
        )
    },

    #----------------------------------------------------------------------
    # Expenditures Table
    
    'expenditures' :
    {
        'filenames' : 'oppexp*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('amndt_ind', 'TEXT', '', ''),
            Column('rpt_yr', 'INTEGER', '', ''),
            Column('rpt_tp', 'TEXT', '', ''),
            Column('image_num', 'TEXT', '', ''),
            Column('line_num', 'TEXT', '', ''),
            Column('from_tp_cd', 'TEXT', '', ''),
            Column('sched_tp_cd', 'TEXT', '', ''),
            Column('name', 'TEXT', '', ''),
            Column('city', 'TEXT', '', ''),
            Column('state', 'TEXT', '', ''),
            Column('zip_code', 'TEXT', '', ''),
            Column('transaction_dt', 'DATE', '', ''),
            Column('transaction_amt', 'MONEY', '', ''),
            Column('transaction_pgi', 'TEXT', '', ''),
            Column('purpose', 'TEXT', '', ''),
            Column('category', 'TEXT', '', ''),
            Column('category_desc', 'TEXT', '', ''),
            Column('memo_cd', 'TEXT', '', ''),
            Column('memo_text', 'TEXT', '', ''),
            Column('entity_tp', 'TEXT', '', ''),
            Column('sub_id', 'INTEGER', 'NOT NULL', ''),
            Column('file_num', 'INTEGER', '', ''),
            Column('tran_id', 'TEXT', '', ''),
            Column('back_ref_tran_id', 'TEXT', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Individual Contributions Table

    'icontributions' :
    {
        'filenames' : 'itcont*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('amndt_ind', 'TEXT', '', ''),
            Column('rpt_tp', 'TEXT', '', ''),
            Column('transaction_pgi', 'TEXT', '', ''),
            Column('image_num', 'TEXT', '', ''),
            Column('transaction_tp', 'TEXT', '', ''),
            Column('entity_tp', 'TEXT', '', ''),
            Column('name', 'TEXT', '', ''),
            Column('city', 'TEXT', '', ''),
            Column('state', 'TEXT', '', ''),
            Column('zip_code', 'TEXT', '', ''),
            Column('employer', 'TEXT', '', ''),
            Column('occupation', 'TEXT', '', ''),
            Column('transaction_dt', 'DATE', '', ''),
            Column('transaction_amt', 'MONEY', '', ''),
            Column('other_id', 'TEXT', '', ''),
            Column('tran_id', 'TEXT', '', ''),
            Column('filenum', 'INTEGER', '', ''),
            Column('memo_cd', 'TEXT', '', ''),
            Column('memo_TEXT', 'TEXT', '', ''),
            Column('sub_id', 'INTEGER', 'NOT NULL', '')
        )
    },

    #----------------------------------------------------------------------
    # PACs Table
    
    'pacs' :
    {
        'filenames' : 'webk*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('cmte_nm', 'TEXT', '', ''),
            Column('cmte_tp', 'TEXT', '', ''),
            Column('cmte_dsgn', 'TEXT', '', ''),
            Column('cmte_filing_freq', 'TEXT', '', ''),
            Column('ttl_receipts', 'MONEY', '', ''),
            Column('trans_from_aff', 'MONEY', '', ''),
            Column('indv_contrib', 'MONEY', '', ''),
            Column('other_pol_cmte_contrib', 'MONEY', '', ''),
            Column('cand_contrib', 'MONEY', '', ''),
            Column('cand_loans', 'MONEY', '', ''),
            Column('ttl_loans_received', 'MONEY', '', ''),
            Column('ttl_disb', 'MONEY', '', ''),
            Column('trans_to_aff', 'MONEY', '', ''),
            Column('indv_refunds', 'MONEY', '', ''),
            Column('other_pol_cmte_refunds', 'MONEY', '', ''),
            Column('cand_loan_repay', 'MONEY', '', ''),
            Column('loan_repay', 'MONEY', '', ''),
            Column('coh_bop', 'MONEY', '', ''),
            Column('coh_cop', 'MONEY', '', ''),
            Column('debts_owed_by', 'MONEY', '', ''),
            Column('nonfed_trans_received', 'MONEY', '', ''),
            Column('contrib_to_othe_cmte', 'MONEY', '', ''),
            Column('ind_exp', 'MONEY', '', ''),
            Column('pty_coord_exp', 'MONEY', '', ''),
            Column('nonfed_share_exp', 'MONEY', '', ''),
            Column('cvg_end_dt', 'DATE', '', '')
        )
    },

    #----------------------------------------------------------------------
    # Transactions Table

    'transactions' :
    {
        'filenames' : 'itoth*.txt',
        'columns' : (
            Column('cmte_id', 'TEXT', 'NOT NULL', ''),
            Column('amndt_ind', 'TEXT', '', ''),
            Column('rpt_tp', 'TEXT', '', ''),
            Column('transaction_pgi', 'TEXT', '', ''),
            Column('image_num', 'TEXT', '', ''),
            Column('transaction_tp', 'TEXT', '', ''),
            Column('entity_tp', 'TEXT', '', ''),
            Column('name', 'TEXT', '', ''),
            Column('city', 'TEXT', '', ''),
            Column('state', 'TEXT', '', ''),
            Column('zip_code', 'TEXT', '', ''),
            Column('employer', 'TEXT', '', ''),
            Column('occupation', 'TEXT', '', ''),
            Column('transaction_dt', 'DATE', '', ''),
            Column('transaction_amt', 'MONEY', '', ''),
            Column('other_id', 'TEXT', '', ''),
            Column('tran_id', 'TEXT', '', ''),
            Column('file_num', 'INTEGER', '', ''),
            Column('memo_cd', 'TEXT', '', ''),
            Column('memo_text', 'TEXT', '', ''),
            Column('sub_id', 'ITNEGER', 'NOT NULL', '')
        )
    }
}
