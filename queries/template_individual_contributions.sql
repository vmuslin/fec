.echo off
/*
Command:
  time sqlite3 -header -column FEC.db ".read queries/individual_contributions.sql"
  m4 -D "_WHERE_"="WHERE i.name LIKE 'NOLAN%'" queries/template_individual_contributions.sql > xquery.sql; time sqlite3 -header -column -echo FEC.db ".read xquery.sql"
*/


.echo off
.headers off
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS DEAILS';
SELECT 'for 2015-2020';
SELECT 'from icontributions, committees, cc_linkages, candidate_master';
SELECT '================================================================================';

.headers on
.width 30, 40, 30, 20, 2, 9, 40, 40
.echo on

SELECT
    cand_name AS 'Candidate',
    cmte_name AS 'Committee',
    name AS 'Donor',
    city AS 'City',
    state AS 'St',
    zip_code AS 'ZipCode',
    employer AS 'Employer',
    occupation AS 'Occupation',
    transaction_amt/100.0 AS 'Total',
    date(transaction_dt,'unixepoch') AS 'Date'
--    date(transaction_dt, 'unixepoch') AS 'Date'
FROM v_individual_contributions_to_candidates
_WHERE_
;

.echo off
.headers off
.width 0
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS SUMMARY';
SELECT 'For 2015-2020';
SELECT '================================================================================';

.headers on
.width 35, 35, 25, 20, 2, 9, 30, 30, 10, 5
.echo on

SELECT
    cand_name AS 'Candidate',
    cmte_name AS 'Committee',
    name AS 'Donor',
    city AS 'City',
    state AS 'St',
    zip_code AS 'ZipCode',
    employer AS 'Employer',
    occupation AS 'Occupation',
    SUM(transaction_amt)/100.0 AS 'Total',
    count(*) AS 'Count'
FROM v_individual_contributions_to_candidates
_WHERE_
GROUP BY
  employer,
  occupation,
  name,
  city,
  state,
  zip_code,
  cmte_id,
  cand_id
ORDER BY
  name ASC,
  Total DESC
;

.echo off

/*
.echo off
.width 40, 40, 40, 20, 2, 9, 40, 40, 15, 4
.width 0
.headers off
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS DETAILS';
SELECT 'for 2015-2020';
SELECT 'from icontributions';
SELECT '================================================================================';

.width 40, 20, 2, 9, 40, 40
.headers on

SELECT
  i.name AS 'Donor',
  i.city AS 'City',
  i.state AS 'St',
  i.zip_code AS 'ZipCode',
  i.employer AS 'Employer',
  i.occupation AS 'Occupation',
  (i.transaction_amt)/100.0 AS 'Total'
FROM
  icontributions i
_WHERE_
;
*/

/*
.headers off
.width 0
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS SUMMARY';
SELECT 'for 2015-2020';
SELECT 'from icontributions';
SELECT '================================================================================';

.headers on
.width 40, 20, 2, 9, 40, 40

SELECT
  i.name AS 'Donor',
  i.city AS 'City',
  i.state AS 'St',
  i.zip_code AS 'ZipCode',
  i.employer AS 'Employer',
  i.occupation AS 'Occupation',
  SUM (i.transaction_amt)/100.0 AS 'Total',
  count(*) AS 'Count'
FROM
  icontributions i
_WHERE_
GROUP BY
  i.cmte_id,
  i.name,
  i.city,
  i.state,
  i.zip_code,
  i.occupation,
  i.employer
ORDER BY
 Total DESC
;
*/

/*
.headers off
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS DETAILS';
SELECT 'for 2019-2020';
SELECT 'from icontributions, committees, cc_linkages, candidate_master';
SELECT '================================================================================';

.headers on
.width 40, 40, 40, 20, 2, 9, 40, 40

SELECT
  m.cand_name AS 'Candidate',
  c.cmte_name AS 'Committee',
  i.name AS 'Donor',
  i.city AS 'City',
  i.state AS 'St',
  i.zip_code AS 'ZipCode',
  i.employer AS 'Employer',
  i.occupation AS 'Occupation',
  (i.transaction_amt)/100.0 AS 'Total'
FROM
  icontributions_2019_2020 i
  LEFT JOIN committees_2019_2020 c ON i.cmte_id = c.cmte_id
  LEFT JOIN cc_linkages_2019_2020 l ON c.cmte_id = l.cmte_id
  LEFT JOIN candidate_master_2019_2020 m ON l.cand_id = m.cand_id
_WHERE_
ORDER BY
  Total DESC
;
*/

/*
.echo off
.headers off
.width 0
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS SUMMARY';
SELECT 'for 2019-2020';
SELECT 'from icontributions, committees, cc_linkages, candidate_master';
SELECT '================================================================================';

.headers on
.width 40, 40, 40, 20, 2, 9, 40, 40

SELECT
  m.cand_name AS 'Candidate',
  c.cmte_name AS 'Committee',
  i.name AS 'Donor',
  i.city AS 'City',
  i.state AS 'St',
  i.zip_code AS 'ZipCode',
  i.employer AS 'Employer',
  i.occupation AS 'Occupation',
  SUM(i.transaction_amt)/100.0 AS 'Total',
  count(*) AS 'Donations'
FROM
  icontributions_2019_2020 i
  LEFT JOIN committees_2019_2020 c ON i.cmte_id = c.cmte_id
  LEFT JOIN cc_linkages_2019_2020 l ON c.cmte_id = l.cmte_id
  LEFT JOIN candidate_master_2019_2020 m ON l.cand_id = m.cand_id
_WHERE_
GROUP BY
  i.cmte_id,
  m.cand_id,
  i.name,
  i.city,
  i.state,
  i.zip_code,
  i.employer
ORDER BY
  Total DESC
;

/*
.echo off
.headers off
.width 0
SELECT '================================================================================';
SELECT 'INDIVIDUAL CONTRIBUTIONS SUMMARY';
SELECT 'for 2015-2020';
SELECT 'from icontributions, committees, cc_linkages, candidate_master';
SELECT '================================================================================';

.headers on
.width 40, 40, 40, 20, 2, 9, 40, 40

SELECT
    cand_name AS 'Candidate',
    cmte_name AS 'Committee',
    name AS 'Donor',
    city AS 'City',
    state AS 'St',
    zip_code AS 'ZipCode',
    employer AS 'Employer',
    occupation AS 'Occupation',
    (i.transaction_amt)/100.0 AS 'Total',
    count(*)
FROM v_individual_contributions_to_candidates
_WHERE_
GROUP BY
  cmte_id,
  cand_id,
  name,
  city,
  state,
  zip_code,
  employer
ORDER BY
  Total DESC
;
*/
