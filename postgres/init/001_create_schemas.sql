
CREATE DATABASE airflow_db;

GRANT ALL PRIVILEGES ON DATABASE airflow_db TO dwh_user;
GRANT ALL PRIVILEGES ON DATABASE dwh TO dwh_user;

CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date TIMESTAMP,
    status VARCHAR(50),
    total_amount DECIMAL(10, 2)
);