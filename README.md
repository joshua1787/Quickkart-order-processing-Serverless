// Project: QuickKart Order Processing System (Enterprise-Grade)


# 🚀 QuickKart Serverless Order Processing System (Python + Boto3)

A full-stack, enterprise-grade **serverless order processing system** built using **Python and Boto3**, simulating real-world workflows used at companies like Amazon, Flipkart, and Walmart. Designed with AWS-managed services and DevOps best practices for high availability, scalability, and cost-efficiency.

---

## 🌐 Live Architecture Overview

```
User ➝ React App ➝ API Gateway ➝ Lambda (submitOrder.py) ➝ SQS
                                                  ⬇
                                    Lambda (processOrder.py)
                                         ⬇        ⬇        ⬇
                                   DynamoDB     S3     SNS Alerts
```

---

## 🧰 Tech Stack

| Layer           | Technology Used                                                |
|-----------------|-----------------------------------------------------------------|
| Frontend        | React.js                                                       |
| API Layer       | AWS API Gateway                                                |
| Compute         | AWS Lambda (Python 3.12 + Boto3)                               |
| Messaging       | AWS SQS (FIFO queue with DLQ support)                          |
| Storage         | Amazon DynamoDB (Order Data), Amazon S3 (File Storage)         |
| Notifications   | Amazon SNS (Success/Failure Alerts)                            |
| Infrastructure  | Terraform (IaC), GitHub Actions (CI/CD pipeline)               |

---

## 🚀 Features

- 📦 Accepts real-time customer orders via frontend form
- 🔒 Validates and processes orders using Python Lambdas
- 🗃️ Stores order data in DynamoDB with timestamps
- 🧾 Uploads optional files to S3 with encryption
- 📩 Sends notifications through SNS
- 🛠️ Fully automated deployments with GitHub Actions and Terraform

---

## 🔧 Project Structure

```
quickkart-order-processing/
│
├── frontend/               # React app to place orders
│
├── lambda/                 # Serverless functions
│   ├── submitOrder.py       # API Gateway Lambda (Python)
│   └── processOrder.py      # SQS-triggered Lambda (Python)
│
├── infra/                  # Terraform files
│   ├── dynamodb.tf
│   ├── sqs.tf
│   ├── sns.tf
│   └── s3.tf
│
├── .github/workflows/       # GitHub Actions CI/CD
│   └── deploy.yml
│
└── README.md
```

---

## ⚙️ Setup Guide

### Prerequisites
- AWS Account with programmatic access (IAM user)
- Node.js + npm
- Terraform CLI installed
- Python 3.12 installed
- GitHub repository with secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

### 1️⃣ Clone the Project
```bash
git clone https://github.com/your-username/quickkart-order-processing.git
cd quickkart-order-processing
```

### 2️⃣ Deploy Infrastructure
```bash
cd infra
terraform init
terraform apply -auto-approve
```

### 3️⃣ Deploy Lambda Functions (Python)
```bash
zip submitOrder.zip lambda/submitOrder.py
aws lambda update-function-code --function-name submitOrder --zip-file fileb://submitOrder.zip

zip processOrder.zip lambda/processOrder.py
aws lambda update-function-code --function-name processOrder --zip-file fileb://processOrder.zip
```

### 4️⃣ Run Frontend
```bash
cd frontend
npm install
npm start
```
👉 Update API URL in `App.js` with your API Gateway endpoint.

---

## ✅ How to Know It's Working

- ✅ Submit order via frontend form
- ✅ API Gateway responds successfully
- ✅ DynamoDB stores order data
- ✅ S3 stores uploaded files (optional)
- ✅ SNS sends email/SMS notification
- ✅ GitHub Actions pipeline completes successfully

---

## 📷 Screenshots (Optional)
_(Form submission, SQS messages, DynamoDB items, SNS email received)_

---

## 👨‍💻 Author
**Joshua Veeraiah**  
DevOps & Cloud Enthusiast aspiring to deliver real-time, scalable solutions using AWS and modern DevOps practices. Let's connect on [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📄 License
This project is for educational, practice, and demo purposes. Customize for production use.
