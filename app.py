from flask import Flask, render_template_string
import requests
import time

app = Flask(__name__)

def check_network():
    try:
        response = requests.get("https://www.google.com", timeout=3)
        return "Online" if response.status_code == 200 else "Offline"
    except:
        return "Offline"

def check_latency():
    try:
        start = time.time()
        requests.get("https://www.google.com", timeout=3)
        end = time.time()
        latency_ms = round((end - start) * 1000, 2)
        return f"{latency_ms} ms"
    except:
        return "N/A"

@app.route("/")
def dashboard():
    network_status = check_network()
    latency = check_latency()
    html = f"""
    <h1>Network Health Analyzer</h1>
    <p>Network Status: <strong>{network_status}</strong></p>
    <p>Latency: <strong>{latency}</strong></p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

