from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests

@app.route("/api/time", methods=["GET"])
def get_current_time():
    now = datetime.utcnow()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    return jsonify({
        "message": "Current UTC time fetched successfully.",
        "formatted_time": formatted_time
    })

if __name__ == "__main__":
    app.run(debug=True)