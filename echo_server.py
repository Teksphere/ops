from flask import Flask
import argparse

app = Flask(__name__)

@app.route('/')
def echo():
    return app.config['MESSAGE']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8080, help='Port to run the server on')
    parser.add_argument('-c', '--content', type=str, default='Hello', help='Message to echo')
    args = parser.parse_args()

    app.config['MESSAGE'] = args.content
    app.run(host='0.0.0.0', port=args.port)
