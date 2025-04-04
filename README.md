# 🚗 Real-Time Vehicle Sensor Data Pipeline

This project simulates real-time vehicle telemetry data and processes it using Apache Kafka, Spark Streaming, and Power BI for analytics and monitoring.
# 🚗 Real-Time Vehicle Sensor Data Pipeline

This project simulates real-time vehicle telemetry data and processes it using Apache Kafka, Spark Streaming, and Jupyter Notebook. It showcases a full data engineering pipeline that’s dashboard-ready for future integration with Power BI or Tableau.

---

## 📌 Overview

This project demonstrates a **real-time data pipeline** for connected vehicles, enabling continuous ingestion, transformation, and streaming analytics.

The use case is applicable to **automotive analytics**, **IoT monitoring**, and **smart fleet management** solutions.

---

## 🛠️ Technologies Used

- Python
- Apache Kafka
- Apache Spark Structured Streaming
- Jupyter Notebook
- Pandas, NumPy
- Power BI / Tableau (optional for dashboard)
- Docker (optional for local deployment)

---

## 📁 Folder Structure

📦 RealTime_Vehicle_Data_Pipeline
├── data_generator/
│   └── vehicle_data_simulator.py
├── kafka_producer/
│   └── send_to_kafka.py
├── spark_streaming/
│   └── spark_consumer.py
├── Vehicle_Data_Simulator_Notebook.ipynb
├── sample_output_log.txt
├── requirements.txt
└── README.md

---

## 📊 Use Case

This pipeline helps:
- Monitor connected vehicle fleets
- Analyze sensor data like speed, fuel level, engine temp
- Trigger alerts for abnormal patterns
- Enable real-time dashboards for operations teams

---

## 🚀 How It Works

### 1. Simulate Vehicle Data (Python/Notebook)

```bash
python data_generator/vehicle_data_simulator.py
