// Project: QuickKart Serverless Order Processing System

---

## 🧾 Project Overview

QuickKart is a **fully serverless order processing system** designed to simulate a real-world e-commerce backend. It demonstrates modern cloud-native architecture using AWS services, CI/CD pipelines, Infrastructure as Code (IaC), and a React frontend hosted on S3.

---

## 🌐 Live Frontend

**URL**: [QuickKart Order Form](http://quickkart-frontend-joshua.s3-website-us-east-1.amazonaws.com)

---

## 🧰 Tech Stack

- **Frontend**: React (hosted on S3 as static site)
- **Backend**: AWS Lambda (Python)
- **API Gateway**: Handles HTTP requests
- **SQS**: FIFO queue to manage decoupled event-driven communication
- **DynamoDB**: Stores order information
- **SNS**: Sends email notifications
- **S3**: Stores uploaded files (if needed)
- **Terraform**: Provisions infrastructure as code
- **CI/CD**: GitHub Actions

---

## 🔁 Architecture Flow

```
[React Form] ---> [API Gateway] ---> [submitOrder Lambda]
                                          |
                                          v
                                     [SQS Queue]
                                          |
                                          v
                                [processOrder Lambda]
                                 |         |         |
                                 v         v         v
                          [DynamoDB]   [S3]     [SNS Email]
```

---

## 🛠 How to Run Locally or Reproduce

### 1. Deploy Infra
```bash
cd infra
terraform init
terraform apply -auto-approve
```

### 2. Deploy Lambdas
```bash
zip submitOrder.zip submitOrder.py
aws lambda update-function-code --function-name submitOrder --zip-file fileb://submitOrder.zip

zip processOrder.zip processOrder.py
aws lambda update-function-code --function-name processOrder --zip-file fileb://processOrder.zip
```

### 3. Set Environment Variables
```bash
aws lambda update-function-configuration \
  --function-name submitOrder \
  --environment "Variables={SQS_URL=https://sqs.us-east-1.amazonaws.com/123456789012/order-queue.fifo}"

aws lambda update-function-configuration \
  --function-name processOrder \
  --environment "Variables={SNS_TOPIC=arn:aws:sns:us-east-1:123456789012:order-alerts}"
```

### 4. Run Frontend
```bash
cd frontend
npm install
npm start
```

---

## 📦 GitHub Actions CI/CD

- Automatically deploys on push to `main`
- Provisions Terraform infra
- Updates Lambda function code

---

## 📧 SNS Email Subscription (Optional)
```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:order-alerts \
  --protocol email \
  --notification-endpoint your-email@example.com
```

---

## 🧪 DevOps Skills Demonstrated

✅ Serverless Architecture Design  
✅ CI/CD with GitHub Actions  
✅ Infrastructure as Code (Terraform)  
✅ Monitoring via CloudWatch Logs  
✅ Secure IAM roles and permissions

---


---

## 🙌 Author
Built by **Joshua Veeraiah** — aspiring DevOps & Cloud Engineer passionate about AWS and real-world architecture building.
