
CREATE DATABASE airflow_db;
CREATE DATABASE dwh; -- про всяк випадок, якщо її немає за замовчуванням
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO dwh_user;
GRANT ALL PRIVILEGES ON DATABASE dwh TO dwh_user;er;