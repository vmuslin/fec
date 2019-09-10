.echo off
.headers off
SELECT '================================================================================';
SELECT 'EMPLOYER CONTRIBUTIONS SUMMARY';
SELECT 'for 2015-2020';
SELECT 'from icontributions, committees, cc_linkages, candidate_master';
SELECT '================================================================================';

.headers on
.width 30, 30, 20, 10, 2, 9, 20, 20, 10, 5
.echo on

SELECT
    cand_name AS 'Candidate',
    cmte_name AS 'Committee',
    employer AS 'Employer',
    SUM(transaction_amt)/100.0 AS 'Total',
    count(*) AS 'Count'
FROM v_individual_contributions_to_candidates
_WHERE_
GROUP BY
  employer,
  cand_name,
  cmte_name
ORDER BY
  employer ASC,
  Total DESC
;

