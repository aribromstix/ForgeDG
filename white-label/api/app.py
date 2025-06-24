from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process():
    return jsonify({ "jobId": "abc123" }), 202

@app.route('/status', methods=['GET'])
def status():
    job_id = request.args.get('jobId')
    return jsonify({ "jobId": job_id, "status": "queued" }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
