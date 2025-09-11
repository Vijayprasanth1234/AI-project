from inventory import list_ec2_instances
from analyzer import analyze_instance
from generator_llm import generate_recommendation

def run_once():
    instances = list_ec2_instances()
    results = []
    for inst in instances:
        a = analyze_instance(inst)
        if a.get('suggestion'):
            rec = a['suggestion']
            rec['instance_id'] = a['instance_id']
            text = generate_recommendation(rec)
            results.append({'inst': a['instance_id'], 'analysis': a, 'llm': text})
    return results
