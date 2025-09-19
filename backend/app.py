from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'OK', 'message': 'Backend de prueba funcionando'})

@app.route('/')
def index():
    return "API Clinica Notarial PoC is running!"

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hola desde la pipeline de Jenkins!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

