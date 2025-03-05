# YouTube API Airflow ETL Pipeline  

## Overview  
This project demonstrates an ETL (Extract, Transform, Load) pipeline using Apache Airflow, originally designed for the Twitter API but later adapted to the YouTube API due to Twitter API deprecation. The pipeline extracts video metadata from the YouTube API, processes it, and stores it in an Amazon S3 bucket. It is deployed on an AWS EC2 instance using Airflow for orchestration.  

## Features  
- Extracts YouTube video metadata (title, views, likes, etc.) using the YouTube API
- Transforms raw JSON data into a structured format
- Loads processed data into an Amazon S3 bucket for further analysis
- Orchestrated using Apache Airflow on an AWS EC2 instance
-  Automates ETL workflow with DAG scheduling and logging

## Technologies Used  
✅ Apache Airflow: Workflow orchestration
✅ YouTube API: Data extraction
✅ AWS EC2: Compute instance for Airflow deployment
✅ AWS S3: Data storage
✅ Python: Data processing and automation
✅ Shell scripting: For environment setup

## Flow Architecture
![Your paragraph text](https://github.com/user-attachments/assets/5b84b746-3feb-4754-94c8-6b42ec594043)


