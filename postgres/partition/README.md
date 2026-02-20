# PostgreSQL Table Partitioning

This directory contains examples of different **Table Partitioning** strategies in PostgreSQL. Partitioning refers to splitting one logically large table into smaller physical pieces, which can significantly improve performance and manageability for large datasets.

## 📋 Partitioning Strategies

### 1. [List Partitioning](./list_partition.sql)

List partitioning allows you to explicitly map rows to partitions based on a set of discrete values in a specific column.

- **Example**: `CUSTOMERS` table partitioned by `STATUS`.
- **Partitions**: `CUST_ACTIVE`, `CUST_EXPIRED`, and `CUST_OTHERS` (default).

### 2. [Range Partitioning](./range_partitions.sql)

Range partitioning maps rows to partitions based on a range of values in a column.

- **Example**: `DOCTOR` table partitioned by `ARR` (Annual Recurring Revenue).
- **Partitions**: `DOC_SMALL` (min-25), `DOC_MEDIUM` (25-75), and `DOC_LARGE` (75-max).

### 3. [Hash Partitioning](./hash_partition.sql)

Hash partitioning maps rows to partitions using a hash function on a partition key. This is useful for distributing rows evenly across a fixed number of partitions.

- **Example**: `EMPLOYEE` table partitioned by `ID`.
- **Modulus/Remainder**: Uses a modulus of 3 to distribute data into `EMP_SMALL`, `EMP_MEDIUM`, and `EMP_LARGE`.

## 🛠️ Key Concepts

- **Declarative Partitioning**: PostgreSQL uses declarative syntax (`PARTITION BY`) to define how a table should be split.
- **Sub-partitions**: Partitions can themselves be partitioned (not demonstrated here).
- **Default Partition**: A catch-all partition for rows that don't match any other partition criteria (used in List partitioning example).
- **System Columns**: The `TABLEOID::REGCLASS` column is used in the examples to verify which physical partition a specific row resides in.

## 🚀 How to Run

You can execute these SQL files against a running PostgreSQL instance:

```bash
psql -h localhost -U postgres -d mydb -f list_partition.sql
psql -h localhost -U postgres -d mydb -f range_partitions.sql
psql -h localhost -U postgres -d mydb -f hash_partition.sql
```

---

_Exploring PostgreSQL performance optimizations._
