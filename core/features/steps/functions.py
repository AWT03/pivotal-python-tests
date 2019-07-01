from json import loads, dumps
from os.path import join
from datetime import datetime
from project_path import PROJECT_PATH
from core.request_api.generic_api import GenericApi
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path


current_date_time = datetime.now().strftime('_%d-%m-%Y_%H:%M:%S')


# Gets the configuration from a path
# :returns: a dict with the configurations
def get_config(config_path):
    f = open(config_path)
    config = f.read()
    f.close()
    config = loads(config)
    return config


def get_data_text(config_file_path, data_tag):
    path_to_config = join(PROJECT_PATH, *config_file_path.split("/"))
    f = open(path_to_config)
    data_text = dumps(loads(f.read())[data_tag])
    f.close()
    return data_text


# From a context.data_text returns data as a dict
def generate_data(context):
    if context.data_text:
        data = context.data_text.replace('(prefix)', context.api.get_config().get("PREFIX"))
        data = data.replace('(current_date_time)', current_date_time)
        data = data.replace('(current_account_id)', context.api.get_config().get("ACCOUNT_ID"))
        data = loads(data)
    else:
        data = {}
    return data


# From the context save all urls in a dict to delete later
# Also builds the ids list that will be used to build end points
# If is_requirement add to list, else just replace the last value on list
def save_to_delete(context, is_requirement):
    obj_id = loads(context.api.get_full_response())["id"]
    if is_requirement:
        context.saved_ids.insert(len(context.saved_ids)-1, str(obj_id))
    else:
        context.saved_ids[-1] = str(obj_id)
    context.to_delete.append(context.api.get_url()+str(obj_id))


# Does the request
# context contains the api for the request and other data
# feature_key, according to configuration file
# http_method that will be executed ('get', 'post, 'put,', 'delete')
# headers that will be used in the request
# is_requirement, new id will be added to list or will replace las value
def do_request(context, feature_key, http_method, headers, is_requirement):
    context.api.build_end_point(feature_key, *context.saved_ids)
    data = generate_data(context)
    context.api.do_request(http_method.lower(), data=data, headers=headers)
    if http_method.lower() == 'post':
        save_to_delete(context, is_requirement)


# Delete items of the object
# object_endpoint: object end point it should be added to the main url
def delete_items(object_endpoint):
    api = GenericApi()
    pivotal_config = get_config(join(pivotal_tracker_path, "config.json"))
    api.set_config(pivotal_config)
    user_config = pivotal_config.get("USER").get('owner')
    headers = {pivotal_config.get("TOKEN_HEADER"): user_config.get("TOKEN")}
    basic = pivotal_config.get("URL").get("base")
    prefix = pivotal_config.get("PREFIX")
    url = basic + '/' + object_endpoint
    api.set_url(url)
    http_method = 'GET'
    api.do_request(http_method.lower(), headers=headers)
    data = loads(api.get_full_response())
    delete_items_from_list(api, headers, data, prefix)


# Delete items by id of the object list
# api: object to do the request methods
# headers: for using the token for the request
# data: where all object item list is saved
# compare_project_name: name of the object that should be compared
def delete_items_from_list(api, headers, data, compare_project_name):
    for value in data:
        object_name = value.get('name', None)
        if compare_project_name in object_name:
            object_id = value.get('id', None)
            url_prepare = '{0}/{1}'.format(api.get_url(), object_id)
            api.set_url(url_prepare)
            api.do_request('delete', headers=headers)
