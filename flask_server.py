from monitor.activity_monitor import ActivityMonitor 
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

class ActivityServer:

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.acticity_monitor = ActivityMonitor(min_stop=2, total=60)

        @self.app.route('/')
        def hello_world():
            return 'Hello, Queue!'

        @self.app.route('/server_status', methods=["GET"])
        def get_server_status():
            return self._corsify_actual_response(jsonify('OK'))

        @self.app.route('/monitor_on', methods=["GET"])
        def start_monitoring():
            if self.acticity_monitor.start_monitor() != 0:
                return jsonify('Monitor is already running!')
            return jsonify('Monitor started!')
        
        @self.app.route('/monitor_off', methods=["GET"])
        def stop_monitoring():
            self.acticity_monitor.stop_monitor()
            return jsonify(self.acticity_monitor.stops)

    @staticmethod
    def _corsify_actual_response(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    def run(self):
        self.app.run(host="0.0.0.0", port="7750", debug=True)
    

if __name__ == "__main__":
    ActivityServer().run()