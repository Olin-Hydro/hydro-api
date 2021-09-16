from datetime import datetime
from flask import abort


def str_to_datetime(utc_time_str: str):
    try: 
        return datetime.strptime(utc_time_str,"%Y-%m-%dT%H:%M:%S.%f")
    except:
        abort(404, "Error converting datetime, ensure format is %Y-%m-%dT%H:%M:%S.%f")