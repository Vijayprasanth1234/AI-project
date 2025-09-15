// Fetch AWS cost
document.getElementById('fetchCostBtn').addEventListener('click', async () => {
    const reportElem = document.getElementById('costReport');
    reportElem.textContent = 'Fetching...';
    try {
        const response = await fetch('/cost');
        const data = await response.json();
        reportElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        reportElem.textContent = 'Error fetching cost data';
        console.error(err);
    }
});

// Fetch CloudWatch metrics
document.getElementById('fetchMetricBtn').addEventListener('click', async () => {
    const namespace = document.getElementById('namespace').value;
    const metric = document.getElementById('metric').value;
    const reportElem = document.getElementById('metricReport');
    reportElem.textContent = 'Fetching...';

    try {
        const response = await fetch(`/cloudwatch/${namespace}/${metric}`);
        const data = await response.json();
        reportElem.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        reportElem.textContent = 'Error fetching metric data';
        console.error(err);
    }
});
