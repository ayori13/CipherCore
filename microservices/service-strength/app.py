from flask import Flask, request, jsonify
import string

app = Flask(__name__)

def check_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 1:
        strength = "weak"
    elif score == 2:
        strength = "medium"
    else:
        strength = "strong"

    return strength, score / 4

@app.post("/check")
def check():
    data = request.json
    password = data.get("password", "")
    strength, score = check_strength(password)
    return jsonify({"strength": strength, "score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
