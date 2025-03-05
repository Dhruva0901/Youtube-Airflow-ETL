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
✅ Apache Airflow  
✅ AWS EC2  
✅ AWS S3  
✅ YouTube API  
✅ Python 
