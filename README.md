# AWS Cost Optimization Agent

A dashboard to fetch AWS costs and CloudWatch metrics.

## Features
- Get last 30 days of AWS cost from Cost Explorer
- Fetch CloudWatch metrics (CPU, memory, etc.)
- Web interface with Flask backend
- Dockerized for easy deployment

## How to Run
1. Configure AWS credentials locally (via `aws configure`).
2. Build and run Docker:
   ```bash
   docker-compose up --build
