import json
from monitor.activity_monitor import ActivityMonitor
from monitor.focus_monitor import FocusMonitor
from flask import Flask, request, abort, jsonify
from flask_cors import CORS

class ActivityServer:

    def __init__(self):
        with open("config.json", 'r') as f:
            config_dict = json.load(f)

        self.app = Flask(__name__)
        CORS(self.app)
        self.acticity_monitor = ActivityMonitor(min_stop=config_dict['activity_monitor']['min_stop'], total=config_dict['activity_monitor']['total'])
        self.focus_monitor    = FocusMonitor(total=config_dict['activity_monitor']['total'])


        @self.app.route('/')
        def hello_world():
            return 'Hello, Queue!'

        @self.app.route('/server_status', methods=["GET"])
        def get_server_status():
            return self._corsify_actual_response(jsonify('OK'))

        @self.app.route('/monitor_on', methods=["GET"])
        def start_activity_monitor():
            if self.acticity_monitor.running():
                return jsonify('Monitor is already running!')

            self.acticity_monitor.start_monitor()
                
            return jsonify('Monitor started!')
        
        @self.app.route('/monitor_off', methods=["GET"])
        def stop_activity_monitor():
            if self.acticity_monitor.running():
                return jsonify(self.acticity_monitor.stop_monitor())
            else:
                return jsonify("Monitor isn't running!")

        @self.app.route('/focus_on', methods=["GET"])
        def start_focus_monitor():
            if self.focus_monitor.running():
                return jsonify('Monitor is already running!')
            
            self.focus_monitor.start_monitor()
            return jsonify('Monitor started!')

        @self.app.route('/focus_off', methods=["GET"])
        def stop_focus_monitor():
            if self.focus_monitor.running():
                return jsonify(self.focus_monitor.stop_monitor())
            else:
                return jsonify("Monitor isn't running!")

    @staticmethod
    def _corsify_actual_response(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    def run(self):
        self.app.run(host="0.0.0.0", port="7750", debug=True)
    

if __name__ == "__main__":
    ActivityServer().run()