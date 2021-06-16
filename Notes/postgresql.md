### resources
- https://www.postgresqltutorial.com/postgresql-show-databases/

``` bat
brew install postgresql
brew services start postgresql
psql postgres
```


``` sql
# list databases
postgres=# \l+

postgres=# \l

SELECT datname FROM pg_database;
```

``` sql
# create schema
create schema if not exists sechema_name;

# list schema names
select schema_name from information_schema.schemata;
```
