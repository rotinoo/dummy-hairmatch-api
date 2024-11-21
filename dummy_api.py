from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Dummy Endpoint for Face Type Detection
@app.route('/api/detect/face', methods=['POST'])
def detect_face():
    time.sleep(3)  # Simulate processing delay
    return jsonify({
        "tipe_wajah": "oval"
    })

# Dummy Endpoint for Hair Type Detection
@app.route('/api/detect/hair', methods=['POST'])
def detect_hair():
    time.sleep(3)  # Simulate processing delay
    return jsonify({
        "tipe_rambut": "keriting"
    })

# Dummy Endpoint for Recommendations
@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json

    # Simulate processing delay
    time.sleep(3)

    # Check if required fields are present
    if "tipe_wajah" not in data or "tipe_rambut" not in data:
        return jsonify({"error": "Missing 'tipe_wajah' or 'tipe_rambut' in request"}), 400

    # Dummy recommendation response
    return jsonify({
        "gaya_rambut": [
            {"nama": "Afro", "gambar": "https://example.com/afro.jpg"},
            {"nama": "Pompadour", "gambar": "https://example.com/pompadour.jpg"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)