AI for Network Security – DDoS Detection Using Machine Learning
Overview

This project focuses on detecting DoS and DDoS attacks using machine learning and network traffic analysis.
The system processes raw PCAP network traces, extracts important traffic features, and trains a Decision Tree classifier to distinguish between normal and malicious traffic.

The project was developed as part of a cybersecurity practice course and demonstrates how machine learning can be applied to network security problems.

Project Objective

The main objective of this project is to:

Analyze network traffic data from PCAP files
Extract meaningful traffic features
Build a machine learning model for attack detection
Evaluate the model using standard performance metrics

The final model achieved an accuracy of approximately 99.68%.

Dataset

The dataset consists of 8 PCAP files containing both normal traffic and different types of DDoS attacks.

Attack Traffic
UDP Flood
DNS Flood
NTP Flood
LDAP Flood
SSDP Flood
SNMP Flood
UDP-Lag
Normal Traffic
benign.pcap

Dataset Source:
Network Security PCAP Dataset Repository

Technologies Used
Python 3
Scapy
Pandas
Scikit-learn
Matplotlib
Seaborn
Project Workflow
Phase 1 – Data Extraction and Labeling
Read PCAP files using Scapy
Extract packet-level features:
Protocol
Source Port
Destination Port
Packet Size
Label traffic:
0 = Normal
1 = Attack
Convert extracted data into CSV format
Phase 2 – Machine Learning
Split dataset into:
70% Training
30% Testing
Train a Decision Tree classifier
Generate predictions
Evaluate model performance
Model Evaluation Metrics

The model was evaluated using:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
Final Results
Accuracy: 99.68%
False Positives: 79
False Negatives: 37
Important Design Decisions

Source and destination IP addresses were intentionally excluded as features to avoid overfitting and ensure the model focused on traffic behavior instead of memorizing specific network identities.

Project Structure
project/
│
├── phase1_data_extraction.py
├── phase2_ml_training.py
├── network_dataset.csv
├── confusion_matrix.png
├── decision_tree.png
├── README.md
└── requirements.txt
How to Run the Project
1. Install Required Libraries
pip install -r requirements.txt
2. Run Data Extraction
python phase1_data_extraction.py
3. Run Machine Learning Model
python phase2_ml_training.py
Output

The project generates:

Processed CSV dataset
Trained Decision Tree model
Confusion Matrix
Performance metrics
Future Improvements

Possible future improvements include:

Using larger datasets
Adding time-based traffic features
Testing advanced ML models such as Random Forest or Neural Networks
Real-time traffic monitoring integration
Author

Tanim Ahmed
Wayne State University
CSC 5290 – Cyber Security Practice
