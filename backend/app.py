import os
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AWS Cost Optimization Agent API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def import_run_once():
    from src.main import run_once
    return run_once

def import_generator():
    from src.generator_llm import generate_recommendation
    return generate_recommendation

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommendations")
def recommendations():
    try:
        run_once = import_run_once()
        out = run_once()
        return {"recommendations": out}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        text = req.message.strip().lower()
        if any(k in text for k in ["idle", "ec2", "instances", "rightsizing", "recommend"]):
            run_once = import_run_once()
            out = run_once()
            return {"type": "recommendations", "payload": out}
        else:
            generate = import_generator()
            sample = {
                "instance_id": "i-sample",
                "from": "t3.large",
                "to": "t3.medium",
                "cpu_avg": 6.2,
                "estimated_monthly_savings_usd": 42.5
            }
            llm_out = generate(sample)
            return {"type": "explain", "payload": llm_out}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
