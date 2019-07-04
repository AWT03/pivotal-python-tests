from core.features.steps.functions import *
from pivotal_tracker.pivotal_tracker_api import PivotalTrackerApi
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path


def get_message(message_tag):
    return get_config(join(pivotal_tracker_path, 'message.json'))[message_tag]


# Delete items of the object
# object_endpoint: object end point it should be added to the main url
def delete_items(object_endpoint):
    api = PivotalTrackerApi()
    pivotal_config = get_config(join(pivotal_tracker_path, "config.json"))
    api.set_config(pivotal_config)
    user_config = pivotal_config.get("USER").get('owner')
    headers = {pivotal_config.get("TOKEN_HEADER"): user_config.get("TOKEN")}
    basic = pivotal_config.get("BASE_URL")
    prefix = pivotal_config.get("PREFIX")
    url = basic + '/' + object_endpoint
    api.set_url(url)
    http_method = 'GET'
    api.do_request(http_method.lower(), headers=headers)
    data = loads(api.get_full_response())
    delete_items_from_list(api, headers, data, prefix, url)


# Delete items by id of the object list
# api: object to do the request methods
# headers: for using the token for the request
# data: where all object item list is saved
# compare_project_name: name of the object that should be compared
# url: this is BASE_URL plus endpoint
def delete_items_from_list(api, headers, data, compare_project_name, url):
    for value in data:
        object_name = value.get('name', None)
        if compare_project_name in object_name:
            object_id = value.get('id', None)
            url_prepare = '{0}/{1}'.format(url, object_id)
            api.set_url(url_prepare)
            api.do_request('delete', headers=headers)
