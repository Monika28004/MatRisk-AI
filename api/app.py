from flask import Flask, render_template, request
import os
import sys

# Add the project root to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.integration_engine.unified_risk_engine import UnifiedRiskEngine

app = Flask(__name__)

engine = UnifiedRiskEngine()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        utilization = float(request.form["utilization"])
        result = engine.run(utilization)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    print("Starting MatRisk AI Dashboard...")
    app.run(debug=True)