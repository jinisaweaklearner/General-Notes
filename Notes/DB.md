## why driver
a DBMS (database management system) needs a database driver that enables a database connection in other systems.

## what is ODBC
https://www.progress.com/faqs/datadirect-odbc-faqs/what-is-an-odbc-driver

## what is DDL
https://en.wikipedia.org/wiki/Data_definition_language

## select top limited values in Microsoft SQL server
```
select top 50 *
from table_name
```

## Identity Column
https://en.wikipedia.org/wiki/Identity_column
https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property?view=sql-server-ver15

## General Data Types
http://www-db.deis.unibo.it/courses/TW/DOCS/w3schools/sql/sql_datatypes_general.asp.html


## OLAP vs OLTP
OLAP (Online Analytic Processing)
- Redshift is design for OLAP and store data in columns not rows. 
Since OLAP is optimized for analyzing data, basic transactional procedures like writes or updates tend to be done in infrequent batches, typically once a day or an hour. OLAP shines when it comes to reads and analytical calculations like aggregation. Several well-known OLAP systems are: 
Amazon Redshift 
- HP Vertica 
- Teradata 
- IBM Netezza 
- KDB+ 
 

OLTP (Online Transactional Processing)
These type of problems require a system that can look up and update one or more columns within one or many rows. The strength of OLTPs is that they support fast writes. A typical workload for OLTP is both frequent reads and writes, but the reads tend to be more of looking up a specific value rather than scanning all values to compute an aggregate. Common OLTP systems are: 
- MySQL 
- PostgreSQL 
- Amazon Aurora 
- Oracle RDBMS 
- IBM DB2 