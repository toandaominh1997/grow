from flask import Flask
from redis import Redis
from prometheus_client import Counter, generate_latest, Summary, Histogram

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
view_metric = Counter('view', 'Product view', ['product'])
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
h = Histogram('request_latency_seconds', 'Description of histogram')

@app.route('/')
def hello():
    h.observe(4.7)
    count = redis.incr('hits')
    return 'Hello World! I dfam tonne. I have been seen {} times.\n'.format(count)

@app.route('/view/<id>')
def view_product(id):
    view_metric.labels(product=id).inc()
    return "View %s" % id

@app.route('/metrics')
def metrics():
    return generate_latest()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
