# 📌 Reddit Data Pipeline Engineering with AWS

This project is an **end-to-end data engineering pipeline** that extracts Reddit data, processes it, and loads it into AWS services for storage and analysis. The pipeline is orchestrated using **Apache Airflow** and leverages AWS services like **S3, Glue, Athena, and Redshift**.

---

## 🛠 Tech Stack

| Component           | Technology |
|--------------------|------------|
| **Data Orchestration** | Apache Airflow |
| **Task Queue** | Celery |
| **Database** | PostgreSQL |
| **Cloud Storage** | AWS S3 |
| **ETL Processing** | AWS Glue |
| **Querying** | AWS Athena |
| **Data Warehouse** | AWS Redshift |

---

## 🔍 Architecture

1. **Data Extraction**  
   - Reddit API is used to extract **posts, comments, and metadata**.

2. **Data Processing**  
   - Data is transformed and preprocessed using **Python scripts**.

3. **Data Storage**  
   - The cleaned data is stored in **PostgreSQL** and **AWS S3**.

4. **Data Transformation**  
   - **AWS Glue** performs **ETL (Extract, Transform, Load) operations**.

5. **Data Querying & Analysis**  
   - **AWS Athena** queries structured data stored in **S3**.  
   - **AWS Redshift** acts as a **data warehouse** for analytics.

6. **Workflow Automation**  
   - **Apache Airflow** automates **pipeline execution and scheduling**.

---

## 📊 Usage

- The pipeline **fetches data** from Reddit, **processes it**, and **loads it** into AWS services.
- **AWS Glue** refines the data, and **Athena** enables **SQL-based querying**.
- The processed data is stored in **Redshift** for further analytics.

---

## 🎯 Key Learnings

✅ **End-to-End Data Engineering**  
   - Understanding how to build a **complete data pipeline** from extraction to storage and querying.  

✅ **Cloud-Based ETL Processing**  
   - Gained experience in **AWS Glue** and **Athena** for **serverless data processing**.  

✅ **Data Orchestration with Airflow**  
   - Learned how to **schedule, monitor, and automate** workflows using **Apache Airflow**.  

✅ **Optimized Query Performance**  
   - Leveraged **Athena** for **cost-effective querying** and **Redshift** for **high-performance analytics**.  

✅ **Scalable Architecture Design**  
   - Implemented a **modular, cloud-native pipeline** that can handle **large-scale data efficiently**.  

---

## 🎯 Results

✅ Successfully automated **Reddit data ingestion and transformation**.  
✅ Enabled **efficient querying** via **Athena** and **Redshift**.  
✅ Built a **scalable architecture** using **AWS cloud services**.

---
