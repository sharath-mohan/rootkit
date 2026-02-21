# PostgreSQL Schema Management

![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This module demonstrates core concepts of **PostgreSQL Schema management**, including namespacing, table isolation, and administrative operations like renaming and cascading drops.

## 🏗️ Key Operations

PostgreSQL schemas (also known as namespaces) allow you to organize database objects into logical groups, which is essential for multi-tenant applications or complex system architectures.

### 1. Schema Lifecycle

The provided `schema.sql` illustrates the full lifecycle of a schema:

- **Creation**: Using `CREATE SCHEMA` to initialize new namespaces (e.g., `ADMIN`, `FINANCE`).
- **Renaming**: Dynamically changing schema names using `ALTER SCHEMA ... RENAME TO ...`.
- **Cleanup**: Safe removal using `DROP SCHEMA IF EXISTS` and forced removal of dependencies using the `CASCADE` keyword.

### 2. Object Isolation

Learn how to create and interact with tables within specific schemas:

- Creating tables within a namespace: `CREATE TABLE schema_name.table_name (...)`.
- Data manipulation: `INSERT` and `SELECT` operations scoped to the schema.

### 3. Metadata Inspection

Common queries to inspect your database structure:

- `SELECT CURRENT_SCHEMA();`: Identify your current active namespace.
- `SELECT * FROM pg_catalog.pg_namespace;`: List all available schemas in the catalog.

## 🚀 How to Use

To execute the demonstration script against your PostgreSQL instance:

```bash
# Using psql directly
psql -d <your_database> -f schema.sql

# Using Docker
docker exec -i <container_id> psql -U postgres -d <your_database> < schema.sql
```

## 🔍 Script Breakdown

The `schema.sql` file follows a step-by-step progression:

1. **Initialize**: Creates the `ADMIN` schema.
2. **Interact**: Creates a `USERS` table and inserts sample data.
3. **Inspect**: Queries the schema catalog.
4. **Refactor**: Renames `ADMIN` to `ADM`.
5. **Modernize**: Creates a `FINANCE` schema.
6. **Cleanup**: Teardown using `CASCADE` to remove the schema and all its tables in one command.

---

_Part of the [Rootkit](../../README.md) Engineering Excellence series._
