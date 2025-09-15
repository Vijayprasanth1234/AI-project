from flask import Flask, jsonify, render_template
import boto3
import datetime

app = Flask(__name__)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AWS_Cost_Optimization')

# Home route to render the dashboard
@app.route('/')
def dashboard():
    return render_template('index.html')

# API to fetch summary metrics
@app.route('/api/summary')
def get_summary():
    # Fetch last 7 days total spend from DynamoDB (placeholder logic)
    total_spend = 12450  # Replace with actual query from DynamoDB
    estimated_savings = 1230  # Replace with calculated savings
    idle_resources = 5  # Replace with count of idle resources
    
    return jsonify({
        "total_spend": total_spend,
        "estimated_savings": estimated_savings,
        "idle_resources": idle_resources
    })

# API to fetch recommendations
@app.route('/api/recommendations')
def get_recommendations():
    # Placeholder: Fetch from DynamoDB or generate via AI
    recommendations = [
        "EC2 i-123456 underutilized: consider rightsizing.",
        "S3 bucket 'logs-bucket' not accessed for 90 days: move to Glacier.",
        "RDS db-prod low CPU: consider switching to smaller instance type."
    ]
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
