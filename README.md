# YouTube API Airflow ETL Pipeline  

## Overview  
As a graduate student in Data Engineering, I undertook this sub-project to address a common challenge in the digital media landscape: the need for efficient, scalable data collection and processing from social media platforms. This project demonstrates an ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline extracts video metadata from the YouTube API, processes it, and stores it in an Amazon S3 bucket for analysis. It is deployed on an AWS EC2 instance using Airflow for orchestration.  

## Features  
- Extracts YouTube video metadata (Author Name, Comment, Posted On and Number of Likes) using the YouTube API
- Transforms and clean raw JSON data into a structured format for accuracy and usability
- Loads processed data into an Amazon S3 bucket for efficient storage and further analysis
- Orchestrated using Apache Airflow on an AWS EC2 instance
- Implements an automated and scalable ETL pipeline with DAG scheduling, logging, and fault tolerance

## Flow Architecture
![Your paragraph text](https://github.com/user-attachments/assets/5b84b746-3feb-4754-94c8-6b42ec594043)




