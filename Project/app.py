from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = max(alphabets, default='', key=lambda x: x.lower())

    response = {
        "is_success": True,
        "user_id": "Ananda_Vardhan_2003",  # Replace with your actual details
        "email": "anandvardhan179@gmail.com",  # Replace with your email
        "roll_number": "RA2111027020051",  # Replace with your roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)

