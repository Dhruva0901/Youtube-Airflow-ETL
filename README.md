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

## Implementation
1) Extract
    - Used the YouTube Data API to fetch video metadata.
    - Retrieved Author Name, Comments, Posted Date, and Number of Likes.
    - Ensured API rate limits were handled efficiently.

2) Transform
    - Processed raw JSON data to filter out unnecessary fields.
    - Structured data into a tabular format for improved usability.
    - Implemented data validation to prevent inconsistencies.
  
3) Load
    - Stored the transformed data in an Amazon S3 bucket.
    - Ensured efficient storage with optimized data partitioning.

4) Orchestration & Deployment
    - Implemented Apache Airflow for ETL workflow automation.
    - Deployed the pipeline on an AWS EC2 instance for scalability.
    - Configured DAG scheduling, logging, and error handling for reliability.
  
## Outcome & Impact
- 100% Automation – Eliminated manual data extraction and processing by implementing a fully automated ETL pipeline.
- Enhanced Data Usability – Transformed raw JSON into structured, analysis-ready data, making it suitable for insights and reporting.
- Cloud Native Solution – Leveraged AWS EC2 for execution and Amazon S3 for scalable, cost-effective data storage.
- Real World Application – Provides a foundation for trend analysis, sentiment analysis, and recommendation systems by continuously collecting and storing YouTube metadata.

## Learning & Takeaways
Building this project enhanced my expertise in Data Engineering, ETL workflows, API data extraction, and workflow automation using Apache Airflow. I gained hands-on experience with cloud deployment on AWS, error handling, and optimizing data storage for scalability and efficiency. Additionally, working with DAG scheduling and orchestration helped me understand real-world data pipeline challenges and solutions to ensure continuous, reliable data updates.

        




