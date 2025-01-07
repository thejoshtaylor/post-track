from flask import Flask, request

app = Flask(__name__)

@app.route('/save/<uuid>', methods=['POST'])
def save_request(uuid):
    # Check if uuid is valid
    if len(uuid) != 36:
        return 'Invalid', 400
    if uuid.count('-') != 4:
        return 'Invalid', 400
    # Save the request
    with open(f'{uuid}.txt', 'w') as f:
        f.write(request.data.decode('utf-8'))
    return 'Request saved'

@app.route('/load/<uuid>', methods=['GET'])
def load_request(uuid):
    # Check if uuid is valid
    if len(uuid) != 36:
        return 'Invalid', 400
    if uuid.count('-') != 4:
        return 'Invalid', 400
    # Load the request
    try:
        with open(f'{uuid}.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return 'Not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)