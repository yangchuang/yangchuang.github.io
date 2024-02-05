---
layout: post
title: '解决PostgreSQL 15 [42501]: ERROR: permission denied for schema public 报错问题'
date: 2023-11-11 10:24:00
feature: https://static.ericsky.com/images/tech/test_user-login.png
summary: '解决PostgreSQL 15 [42501]: ERROR: permission denied for schema public 报错问题'
categories: study
---

PostgreSQL 15 对public schema的默认权限做了修改，`PostgreSQL 15 also revokes the CREATE permission from all users except a database owner from the public (or default) schema.`。见 [PostgreSQL 15 Released](https://www.postgresql.org/about/news/postgresql-15-released-2526/) 

这会导致登录超级用户postgres使用下方的SQL创建新数据库、新用户、及授权后，用新用户登录新数据库建表，会出现`[42501]: ERROR: permission denied for schema public`报错。

```sql
# Postgresql 14及之前的版本适用，15及之后的版本会有问题
create DATABASE test_db;
CREATE USER test_user WITH ENCRYPTED PASSWORD 'Test#2023';
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;
```

<img src="/images/tech/postgres-login.png" alt="postgres登录"/>

test_user登录test_db，PostgreSQL 15及之后的版本，建表会失败（15之前的版本正常）

```sql
create TABLE test(
	id text
)
```

<img src="/images/tech/test_user-login.png"  alt="test_user登录"/>

**正确的步骤应该是**

1.超级用户postgres登录postgres数据库，创建新数据库及新用户

```sql
CREATE DATABASE test_db;
CREATE USER test_user WITH ENCRYPTED PASSWORD 'Test#2023';
```

2.超级用户postgres登录新数据库test_db，给新用户test_user授权

```sql
GRANT ALL ON SCHEMA public TO test_user;
```

<img src="/images/tech/postgres-login-testdb.png"  alt="test_user登录"/>

3.使用新用户test_user登录新数据库test_db, 可以成功建表了

```sql
create TABLE test(
  id text
)
```

<img src="/images/tech/create-table-success.png"  alt="test_user登录"/>

参考资料：  
[POSTGRESQL ERROR: PERMISSION DENIED FOR SCHEMA PUBLIC](https://www.cybertec-postgresql.com/en/error-permission-denied-schema-public/)  
[Postgres 15. permission denied for schema public](https://stackoverflow.com/questions/74110708/postgres-15-permission-denied-for-schema-public)  
[PostgreSQL 15 Released](https://www.postgresql.org/about/news/postgresql-15-released-2526/)  