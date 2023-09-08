from flask_restx import Namespace, Resource
from datetime import datetime
from pytz import timezone

track_namespace = Namespace('tracks',description=" a namespace for getting information about different tracks in in HNG")
dt = datetime.now()
format = "%Y-%m-%d T%H:%M:%SZ"
now_utc = datetime.now(timezone('Africa/Lagos'))



@track_namespace.route('/get-track/<slack_name>/<track_type>')
class trackGet(Resource):
    """Get track by slack name and track type"""
    def get(self, slack_name, track_type):
        return {
        "slack_name": slack_name,
        "Current_day": dt.strftime('%A'),
        "utc_time": now_utc.strftime(format),
        "Track": track_type,
        "GitHub_File_URL": "https://github.com/danielTunwashe/flask_zuri_api_st1/blob/main/api/__init__.py",
        "GitHub_Repo_URL": "https://github.com/danielTunwashe/flask_zuri_api_st1.git",
        "Status Code": 200
        }