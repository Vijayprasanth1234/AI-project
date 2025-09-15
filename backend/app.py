from flask import Flask, jsonify
import boto3
import datetime

app = Flask(__name__)

# Initialize AWS clients
ce = boto3.client('ce')  # Cost Explorer
cloudwatch = boto3.client('cloudwatch')

@app.route('/cost', methods=['GET'])
def get_cost_data():
    """
    Fetch cost and usage data from AWS Cost Explorer.
    """
    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=30)  # last 30 days

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start.strftime('%Y-%m-%d'), 'End': end.strftime('%Y-%m-%d')},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    results = []
    for item in response['ResultsByTime']:
        results.append({
            'Date': item['TimePeriod']['Start'],
            'Cost': item['Total']['UnblendedCost']['Amount']
        })

    return jsonify(results)

@app.route('/cloudwatch/<string:namespace>/<string:metric_name>', methods=['GET'])
def get_cloudwatch_metrics(namespace, metric_name):
    """
    Fetch CloudWatch metric data.
    Example namespace: AWS/EC2
    Example metric_name: CPUUtilization
    """
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[{'Name': 'InstanceId', 'Value': 'i-0123456789abcdef0'}],  # replace with real instance ID
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(hours=24),
        EndTime=datetime.datetime.utcnow(),
        Period=3600,
        Statistics=['Average']
    )

    data_points = [{'Timestamp': dp['Timestamp'].isoformat(), 'Average': dp['Average']} for dp in response['Datapoints']]
    return jsonify(data_points)

if __name__ == '__main__':
    app.run(debug=True)
