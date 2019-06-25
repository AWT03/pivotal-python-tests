from json import loads
from os.path import join
from abc import ABC, abstractmethod
from core.request_api.generic_api import GenericApi
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path


class TabControl(ABC):
    def __init__(self, view):
        self._view = view
        self._api = GenericApi()
        self._api.set_config(self._get_config())
        self._headers = {}
        user_config = self._get_config().get("USER")
        self._headers[user_config.get("HEADER")] = user_config.get("3190382")

    def _show_response(self):
        self._view.set_request_status(str(self._api.get_status()))
        self._view.post_message(self._api.get_full_response())

    @staticmethod
    def _get_config():
        f = open(join(pivotal_tracker_path, "config.json"))
        config = f.read()
        f.close()
        config = loads(config)
        return config

    @abstractmethod
    def _update_api(self):
        pass

    @abstractmethod
    def _get_data(self):
        pass

    @abstractmethod
    def _connect_tab(self):
        pass

    def _generic_get(self):
        self._update_api()
        self._api.do_request('get', headers=self._headers)
        self._show_response()

    def _generic_put(self):
        self._update_api()
        self._api.do_request('put', self._get_data(), self._headers)
        self._show_response()

    def _generic_post(self):
        self._update_api()
        self._api.do_request('post', self._get_data(), self._headers)
        self._show_response()

    def _generic_delete(self):
        self._update_api()
        self._api.do_request('delete', headers=self._headers)
        self._show_response()
