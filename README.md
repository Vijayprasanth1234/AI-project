# AWS Cost Optimization AI Agent 🚀

This repo contains a web-based chatbot powered by FastAPI + React.
It connects to AWS (via boto3), analyzes cost optimization opportunities (idle EC2, rightsizing, etc.),
and uses an LLM (OpenAI GPT) to generate natural-language recommendations.

## Setup
1. Copy `.env.example` → `.env` and update secrets.
2. Run `docker-compose up --build`.
3. Backend: http://localhost:8000/docs
4. Frontend: http://localhost:3000
