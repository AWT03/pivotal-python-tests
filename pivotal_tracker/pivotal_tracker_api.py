from core.request_api.generic_api import GenericApi
from core.features.steps import functions
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path
from os.path import join


class PivotalTrackerApi(GenericApi):
    def __init__(self):
        super().__init__()

    # Build the end_point (url) for request according to configuration file
    def build_end_point(self, tag, *ids):
        end_point_config = functions.get_config(join(pivotal_tracker_path, "end_point.json"))
        end_point = self._config['BASE_URL'] + end_point_config[tag]
        index = 0
        for n_id in ids:
            end_point = end_point.replace('$ID(' + str(index) + ')', n_id)
            index += 1
        self.set_url(end_point)
