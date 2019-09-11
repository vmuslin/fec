# FEC - Federal Election Commission Database Loader

The program dbloader.py creates a SQLite database and loads FEC datasets.

Please note that currently a few things are hardcoded (in dbloader.py) file  that is
to be run from command line with no parameters. Specifically,
 - Location of the database is hardcoed at ../data/fec/FEC.db,
 - Location of the datasets directory is hardcoded at ../data/fec.
   - See the expected structure of the datasets directory below.

Shell script run_sql.sh simplifies some of the queries (need m4 macro processor).
Some sample queries are in the queries subdirectory.

The datasets can be downloaded from the FEC website [bulkload data page](https://www.fec.gov/data/browse-data/?tab=bulk-data).

Each dataset reflects a two-year period (such as 2019-2020). A dataset consists of a number of files.
Each file corresponds to a table. The documentation is available at the FEC website but the
PDF's can be found in the doc subdirectory.

The loader expects each dataset to be in its own directory. All datasets should be in subdirectories
of a common parent directory. It is best to name each dataset directory with the range of years, such
as "2015-2016."

Note that datasets are stored as zipped archives. They need to be extracted into the directory structure.

## Datasets directory structure

```
  datasets
  |
  +--2015-2016
  |  |
  |  +--ccl.txt
  |  +--cm.txt
  |  +--cn.txt
  |  +--itcont.txt
  |  +--itoth.txt
  |  +--itpas2.txt
  |  +--oppexp.txt
  |  +--weball16.txt
  |  +--wbk16.txt
  |  +--web16.txt
  |
  +--2016-2018
  |  |
  |  +--ccl.txt
  |  +--cm.txt
  |  +--cn.txt
  |  +--itcont.txt
  |  +--itoth.txt
  |  +--itpas2.txt
  |  +--oppexp.txt
  |  +--weball18.txt
  |  +--wbk18.txt
  |  +--web18.txt
  ```

## To Do List
 - [ ] Parse command line parameters to:
   - [ ] Set the location and name of the database
   - [ ] Set the location of the datasets directory
 - [ ] Create an option to build indexes for better query performance