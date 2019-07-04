from behave.__main__ import main as behave_main
from os.path import join
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path

behave_main(join(pivotal_tracker_path, 'features'))
