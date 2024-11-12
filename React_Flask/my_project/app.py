from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/validate', methods=['POST'])
def validate_number():
    data = request.json
    input_value = data.get('number', '')
    
    try:
        # Try to convert to float to check if it's a number
        float(input_value)
        return jsonify({
            "isValid": True,
            "message": "That's a valid number!"
        })
    except ValueError:
        return jsonify({
            "isValid": False,
            "message": "That's not a valid number."
        })

if __name__ == '__main__':
    app.run(debug=True)