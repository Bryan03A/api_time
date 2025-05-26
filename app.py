from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
import os
import pytz

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests

@app.route("/api/time", methods=["GET"])
def get_current_time():
    # Set the timezone to Quito, Ecuador
    tz = pytz.timezone('America/Guayaquil')
    now = datetime.now(tz)

    # Format the time as dd/mm/yyyy hh:mm:ss AM/PM
    formatted_time = now.strftime("%d/%m/%Y %I:%M:%S %p")

    return jsonify({
        "message": "Current time fetched successfully - PR Test",
        "formatted_time": formatted_time
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)
