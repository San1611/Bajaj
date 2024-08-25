from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded user info
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Determine the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        if lowercase_alphabets:
            highest_lowercase_alphabet = [max(lowercase_alphabets)]
        else:
            highest_lowercase_alphabet = []

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
