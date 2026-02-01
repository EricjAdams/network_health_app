from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

def check_network():
    try:
        response = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Online" if response.returncode == 0 else "Offline"
    except:
        return "Error"

def check_latency(host="8.8.8.8"):
    try:
        response = subprocess.run(["ping", "-c", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in response.stdout.splitlines():
            if "time=" in line:
                return line.split("time=")[1].split()[0] + " ms"
        return "N/A"
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

