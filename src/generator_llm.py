import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recommendation(rec):
    prompt = f"""You are an AWS cost optimization expert.
Analyze this EC2 recommendation and explain in simple terms for a DevOps engineer.

Instance: {rec.get('instance_id')}
Current type: {rec.get('from')}
Suggested type: {rec.get('to')}
Average CPU usage: {rec.get('cpu_avg')}%
Estimated monthly savings: ${rec.get('estimated_monthly_savings_usd')}

Explain clearly why this change saves cost, without being too technical."""

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for AWS cost savings."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return {"text": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
