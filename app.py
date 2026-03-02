from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Your heat stress prediction logic here
    prediction = "Heat stress risk: Moderate"  # Placeholder response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)