from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    print("called generate")
    data = request.json
    modelname = data.get('modelname')
    viewerid = data.get('viewerid')
    
    result = {
        "reason": modelname,
        "result": random.randint(1, 100)
    }
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
