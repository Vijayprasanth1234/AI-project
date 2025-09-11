def analyze_instance(inst):
    # Example: basic idle check based on CPU options (mock — replace with CloudWatch metrics)
    instance_id = inst.get("InstanceId")
    instance_type = inst.get("InstanceType")
    state = inst.get("State", {}).get("Name")
    
    # Mock analysis
    if state == "stopped":
        return {"instance_id": instance_id, "suggestion": {"instance_id": instance_id, "from": instance_type, "to": None, "cpu_avg": 0.0, "estimated_monthly_savings_usd": 20}}
    
    if "t3.large" in instance_type:
        return {"instance_id": instance_id, "suggestion": {"instance_id": instance_id, "from": instance_type, "to": "t3.medium", "cpu_avg": 6.5, "estimated_monthly_savings_usd": 40}}
    
    return {"instance_id": instance_id, "suggestion": None}
