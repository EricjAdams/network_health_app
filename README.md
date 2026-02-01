# Network Health Analyzer

A Python/Flask web app that checks network connectivity and latency, displaying results on a live dashboard. This project demonstrates backend development, network monitoring basics, and cloud deployment.

---

## Live Demo
Try it live on Render: [https://network_health_app.onrender.com](https://network_health_app.onrender.com)

---

## Features
- Checks network connectivity (ping)
- Measures latency
- Displays results on a simple web dashboard
- Hosted securely on Render using Gunicorn
- Easily extendable with logging, alerts, or additional network checks

---

## Installation / Setup

Clone the repository and set up your environment:

```bash
# Clone repo
git clone https://github.com/EricjAdams/network_health_app.git
cd network_health_app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

