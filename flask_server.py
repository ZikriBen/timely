from flask import Flask, request, abort


app = Flask(__name__)
    
@app.route('/')
def hello_world():
    return 'Hello, Queue!'

@app.route('/server_status', methods=["GET"])
def get_server_status():
    return 'OK'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5580")
