from json import dumps, JSONDecodeError
from simplejson.errors import JSONDecodeError
from requests import request


# Class used for generic API connections and requests
class GenericApi:
    def __init__(self):
        self.__url = ""
        self.__config = {}
        self.__request = None

    # Build the end_point (url) for request according to configuration file
    def build_end_point(self, tag, *ids):
        end_point = self.__config['URL']['base'] + self.__config['URL'][tag]
        index = 0
        for n_id in ids:
            end_point = end_point.replace('$ID(' + str(index) + ')', n_id)
            index += 1
        self.set_url(end_point)

    # Does the request and saves it as an attribute to recover data later
    def do_request(self, http_method, data=None, headers=None, params=None):
        self.__request = request(http_method, self.__url, data=data, headers=headers, params=params)

    # Recovers the response of the request as a text or string
    def get_full_response(self):
        try:
            full_response = dumps(self.__request.json(), indent=4, sort_keys=True)
        except JSONDecodeError:
            full_response = '{}'
        return full_response

    # Recovers the status code of the request
    def get_status(self):
        return self.__request.status_code

    # Manually sets the url that the API object will use
    def set_url(self, value):
        self.__url = value

    # Gets the url that the API object is currently using
    def get_url(self):
        return self.__url

    # Manually sets the config that the API object will use (should be a dict)
    def set_config(self, value):
        self.__config = value

    # Gets the configuration that the API object is currently using
    def get_config(self):
        return self.__config
