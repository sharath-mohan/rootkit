# PgBouncer + Python/SQLAlchemy Integration

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)
![Docker](https://img.shields.io/badge/docker-required-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This project demonstrates how to integrate **PgBouncer** as a connection pooler between a **Python application** (using SQLAlchemy) and a **PostgreSQL database**.

## 🏗️ Architecture

The connection flow is as follows:
`Python App` → `PgBouncer (Port 6432)` → `PostgreSQL (Port 5430)`

- **PgBouncer** is configured in `transaction` mode to maximize connection efficiency.
- **SQLAlchemy** connects to PgBouncer using the `psycopg2` driver.

## 📋 Prerequisites

Before starting, ensure you have the following installed:

- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- [uv](https://github.com/astral-sh/uv) (Python package manager)

## 🚀 Quick Start

### 1. Start Infrastructure

Start the PostgreSQL and PgBouncer containers using the provided startup script:

```bash
chmod +x startup.sh
./startup.sh
```

### 2. Configure Environment

Create a `.env` file in the `app` directory with your database connection URL:

```bash
echo "DATABASE_URL=postgresql+psycopg2://postgres:mysecretpassword@localhost:6432/mydb" > app/.env
```

### 3. Install Dependencies

Use `uv` to sync dependencies and create a virtual environment:

```bash
cd app
uv sync
```

### 4. Run the Application

Execute the main script to test the connection and create sample data:

```bash
uv run main.py
```

## 🔍 Application Logic

The `app/main.py` script performs the following actions:

1. **Verifies Connectivity**: Tests the connection to PostgreSQL via PgBouncer.
2. **Schema Initialization**: Creates a `users` table if it doesn't exist.
3. **Data Generation**: Uses `Faker` to generate and insert a new user record.
4. **Validation**: Prints the created user details to the console.

## ⚙️ Configuration

- `.env`: Environment variables for the application (e.g., `DATABASE_URL`).
- `pgbouncer.ini`: Main configuration for PgBouncer, defining database backends and pooling parameters.
- `userlist.txt`: Contains authentication credentials for PgBouncer (using `scram-sha-256`).
- `startup.sh`: Automates the Docker deployment of the entire stack.

---

_Developed for research and demonstration purposes._
