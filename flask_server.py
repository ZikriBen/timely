from monitor.activity_monitor import ActivityMonitor 
from flask import Flask, request, abort


class ActivityServer:

    def __init__(self):
        self.app = Flask(__name__)
        self.acticity_monitor = ActivityMonitor(min_stop=2, total=10)

        @self.app.route('/')
        def hello_world():
            return 'Hello, Queue!'

        @self.app.route('/server_status', methods=["GET"])
        def get_server_status():
            return 'OK'

        @self.app.route('/monitor_on', methods=["POST"])
        def start_monitoring():
            self.acticity_monitor.start_monitor()
            return 'Monitor started!'
        
        @self.app.route('/monitor_off', methods=["POST"])
        def stop_monitoring():
           self.acticity_monitor.stop_monitor()
           return str(self.acticity_monitor.stops)

    def run(self):
        self.app.run(host="0.0.0.0", port="7750", debug=True)
    

if __name__ == "__main__":
    ActivityServer().run()