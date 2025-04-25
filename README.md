# Quickkart-order-processing-Serverless
// Project: QuickKart Order Processing System (Enterprise-Grade)

// === FILE: frontend/src/App.js ===
<unchanged>...

// === FILE: README.md ===
# 🚀 QuickKart Serverless Order Processing System

A full-stack, enterprise-grade **serverless order processing system** that simulates real-time workflows used in production at companies like Amazon, Flipkart, and Walmart. Designed using AWS-managed services and DevOps best practices for high availability, scalability, and cost-efficiency.

---

## 🌐 Live Architecture Overview

```
User ➝ React App ➝ API Gateway ➝ Lambda (submitOrder) ➝ SQS
                                                ⬇
                                  Lambda (processOrder)
                                       ⬇        ⬇        ⬇
                                 DynamoDB     S3     SNS Alerts
```

---

## 🧰 Tech Stack

| Layer           | Technology Used                                                |
|----------------|----------------------------------------------------------------|
| Frontend       | React.js                                                      |
| API Layer      | AWS API Gateway                                               |
| Compute        | AWS Lambda (Node.js)                                          |
| Messaging      | AWS SQS (FIFO queue with DLQ support)                         |
| Storage        | Amazon DynamoDB (Order Data), Amazon S3 (File Storage)        |
| Notifications  | Amazon SNS (Success/Failure Alerts)                           |
| Infrastructure | Terraform (IaC), GitHub Actions (CI/CD pipeline)              |

---

## 🚀 Features

- 📦 Accepts real-time customer orders through a frontend form
- 🔒 Validates and processes orders using Lambda & SQS
- 🗃️ Stores order details in DynamoDB with timestamp
- 🧾 Stores optional files in S3 with encryption
- 📩 Sends order status alerts to teams using SNS
- 🛠️ Fully automated deployment via GitHub Actions + Terraform

---

## 🔧 Project Structure
```
quickkart-order-processing/
│
├── frontend/              # React app for placing orders
│
├── lambda/                # Serverless functions
│   ├── submitOrder/       # API Gateway Lambda
│   └── processOrder/      # SQS-triggered Lambda
│
├── infra/                 # Terraform for AWS infra
│   ├── dynamodb.tf
│   ├── sqs.tf
│   ├── sns.tf
│   └── s3.tf
│
├── .github/workflows/     # GitHub Actions CI/CD pipeline
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
- GitHub repo with Secrets set:
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

### 3️⃣ Deploy Lambda Functions
```bash
zip -j submitOrder.zip lambda/submitOrder/index.js
aws lambda update-function-code --function-name submitOrder --zip-file fileb://submitOrder.zip

zip -j processOrder.zip lambda/processOrder/index.js
aws lambda update-function-code --function-name processOrder --zip-file fileb://processOrder.zip
```

### 4️⃣ Run Frontend
```bash
cd frontend
npm install
npm start
```
👉 Update API URL in `App.js` with your API Gateway URL

---

## ✅ How to Know It's Working

- ✅ Submit order via form → API Gateway response is success
- ✅ Order appears in DynamoDB table
- ✅ File (if any) is stored in S3 bucket
- ✅ Email/SMS sent from SNS topic
- ✅ GitHub Actions runs `deploy.yml` successfully

---

## 📷 Screenshots
_(Add screenshots of form submission, DynamoDB, SQS, logs)_

---

## 👨‍💻 Author
**Joshua Veeraiah**  
DevOps & Cloud Enthusiast aspiring to work on scalable infrastructure with real-time automation. Connect with me on [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📄 License
This project is for educational and demo purposes. Customize it for production use!
