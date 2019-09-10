#!/bin/bash

# This is a handy script to simplify some common queries
# (check out the query subdirectory)

function usage
{
    echo 'run_sql.sh [-h|--help] db sqlscript [where_clause]'
    echo ''
    echo '    db'
    echo '        sqlite database file.'
    echo ''
    echo '    sqlscript'
    echo '        File containing SQL commands.'
    echo ''
    echo '    where_clause'
    echo '        A where clause to be used in the query'
    echo ''
    echo 'Example:'
    echo '   ./run_sql.sh queries/template_individual_contributions.sql "WHERE name LIKE ''NOLAN, SUSAN%''"'
}

echo $*
echo $#

WHERE=""

if (( $# < 2 )); then
    usage
    exit 1
elif (( $# == 3 )); then
    WHERE=$2

fi

DB=$1
QUERY=$2

set -x
m4 -D _WHERE_="${WHERE}" ${QUERY} > xquery.sql
time sqlite3 -header -column -echo ${DB} '.read xquery.sql'
rm xquery.sql
