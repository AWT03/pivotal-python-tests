from json import loads
from os.path import join
from datetime import datetime
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path

CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


def format_string(value):
    value = value.replace('(prefix)', CONFIG.get('PREFIX'))
    value = value.replace('(current_date_time)', datetime.now().strftime("%d-%m-%YT%H:%M:%S"))
    return value
