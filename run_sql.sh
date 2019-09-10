#!/bin/bash

#QUERY=queries/template_individual_contributions.sql
#WHERE="WHERE name LIKE 'NOLAN, SUSAN%'"
#echo ${WHERE}

function usage
{
    echo 'run_sql.sh [-h|--help] sqlscript [where_clause]'
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

if (( $# == 0 )); then
    usage
    exit 1
elif (( $# == 2 )); then
    WHERE=$2

fi

QUERY=$1

set -x
m4 -D _WHERE_="${WHERE}" ${QUERY} > xquery.sql
time sqlite3 -header -column -echo FEC.db '.read xquery.sql' | tee xquery.txt
rm xquery.sql
