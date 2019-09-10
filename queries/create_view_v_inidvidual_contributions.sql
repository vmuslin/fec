CREATE VIEW IF NOT EXISTS v_individual_contributions_to_candidates
AS
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
    icontributions_2019_2020 i
    LEFT JOIN committees_2019_2020 c ON i.cmte_id = c.cmte_id
    LEFT JOIN cc_linkages_2019_2020 l ON c.cmte_id = l.cmte_id
    LEFT JOIN candidate_master_2019_2020 m ON l.cand_id = m.cand_id
  UNION ALL
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
    icontributions_2017_2018 i
    LEFT JOIN committees_2017_2018 c ON i.cmte_id = c.cmte_id
    LEFT JOIN cc_linkages_2017_2018 l ON c.cmte_id = l.cmte_id
    LEFT JOIN candidate_master_2017_2018 m ON l.cand_id = m.cand_id
  UNION ALL
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
    icontributions_2015_2016 i
    LEFT JOIN committees_2015_2016 c ON i.cmte_id = c.cmte_id
    LEFT JOIN cc_linkages_2015_2016 l ON c.cmte_id = l.cmte_id
    LEFT JOIN candidate_master_2015_2016 m ON l.cand_id = m.cand_id
;
