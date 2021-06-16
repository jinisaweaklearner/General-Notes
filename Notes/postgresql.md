### resources
- https://www.postgresqltutorial.com/postgresql-show-databases/


```
# list databases
postgres=# \l+

postgres=# \l

SELECT datname FROM pg_database;
```

```
# create schema
create schema if not exists sechema_name;

# list schema names
select schema_name from information_schema.schemata;
```
