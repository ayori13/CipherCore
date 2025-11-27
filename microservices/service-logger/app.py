from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.post("/log")
def log_data():
    data = request.json
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] LOG RECEIVED: {data}")
    return jsonify({"status": "logged", "received": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)