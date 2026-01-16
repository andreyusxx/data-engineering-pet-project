# E-commerce Data Platform (Pet Project) 🛒

## 📌 Overview
This is an end-to-end Data Engineering project that simulates a real-world data platform for an E-commerce business. The project demonstrates a fully automated **ELT (Extract, Load, Transform)** pipeline using a modern data stack.

**Key Goal:** Ingest raw sales data, transform it into business-ready insights, ensure data quality, and visualize the results.

## 🛠 Tech Stack
* **Infrastructure:** Docker & Docker Compose
* **Orchestration:** Apache Airflow
* **Data Warehouse:** PostgreSQL
* **Transformation:** dbt (Data Build Tool)
* **Data Quality:** dbt Tests (Schema & Singular tests)
* **Visualization (BI):** Metabase

## 🏗 Architecture & Data Flow
The pipeline follows a layered architecture approach:

1.  **Raw Layer (Bronze):** Airflow ingests raw CSV files (`users.csv`, `orders.csv`) directly into PostgreSQL (`raw` schema).
2.  **Staging Layer (Silver):** dbt cleans data, standardizes types, and removes duplicates (Views).
3.  **Marts Layer (Gold):** dbt builds final analytical tables (`dm_users`) ready for reporting (Tables).
4.  **Presentation:** Metabase connects to the Marts layer to display dashboards.

## 🚀 How to Run

### Prerequisites
* Docker Desktop installed.

### Steps
1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <project-folder>
    ```

2.  **Start the platform:**
    ```bash
    docker-compose up -d
    ```

3.  **Initialize Airflow (if running for the first time):**
    The setup is automated, but ensure the DAGs are visible at `http://localhost:8080`.

## 🔑 Access Credentials

| Service | URL | Login | Password |
| :--- | :--- | :--- | :--- |
| **Apache Airflow** | [http://localhost:8080](http://localhost:8080) | `admin` | `admin` |
| **Metabase** | [http://localhost:3000](http://localhost:3000) | *(Setup on first launch)* | - |
| **PostgreSQL** | `localhost:5432` | `dwh_user` | `dwh_pass` |

* **Database Name:** `dwh`

## 📊 Key Features Implemented
* ✅ **Containerization:** Complete infrastructure defined as code (`docker-compose.yml`).
* ✅ **Orchestration:** Airflow DAGs handle dependencies between loading and transformation tasks.
* ✅ **Data Quality:** Automated tests in dbt ensure `unique`, `not_null`, and business logic constraints (e.g., `total_spent` cannot be negative).
* ✅ **Idempotency:** The pipeline can be rerun multiple times without creating duplicate records.
* ✅ **BI Dashboard:** Visualization of "Top Customers" using Metabase.

---
*Created by Andriy Sharagin as a Data Engineering portfolio project.*