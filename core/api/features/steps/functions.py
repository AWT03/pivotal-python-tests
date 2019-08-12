from json import loads, dumps
from os.path import join
from datetime import datetime
from project_path import PROJECT_PATH


current_date_time = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
current_ISO8601_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


# Gets the configuration from a path
# :returns: a dict with the configurations
def get_config(config_path):
    f = open(config_path)
    config = f.read()
    f.close()
    config = loads(config)
    return config


def get_data_text(file_path):
    path_to_config = join(PROJECT_PATH, *file_path.split("/"))
    f = open(path_to_config)
    data_text = dumps(loads(f.read()))
    f.close()
    return data_text


# From a context.table returns data as a dict
def generate_dict_from_data_table(context):
    dict_data = {}
    if context.table:
        data_list = context.data_row
        row_header = data_list.headings
        for head in row_header:
            if head != 'error':
                dict_data.update({head: data_list[head]})
    return dict_data


# From a context.data_text returns data as a dict
def generate_data(context):
    if context.data_text:
        data = context.data_text.replace('(prefix)', context.api.get_config().get("PREFIX"))
        data = data.replace('(current_date_time)', current_date_time)
        data = data.replace('(current_date_time_ISO8601)', current_ISO8601_datetime)
        data = data.replace('(current_account_id)', context.api.get_config()
                            .get("ACCOUNTS").get("API").get("ID"))
        data = loads(data)
    elif context.table:
        dict_data = generate_dict_from_data_table(context)
        data = dumps(dict_data)
        prefix = context.api.get_config().get("PREFIX")
        data = data.replace('(prefix)', prefix)
        data = data.replace('(random)', context.current_time_random)
        data = loads(data)
    elif "data" in context:
        data = context.data
        data = data.replace('(prefix)', context.api.get_config().get("PREFIX"))
        data = data.replace('(current_date_time)', current_date_time)
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


# To save a list of ids created
def save_ids_data(context):
    obj_id = loads(context.api.get_full_response())["id"]
    context.ids_list.append(str(obj_id))


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
    response = loads(context.api.get_full_response())
    if response:
        save_ids_only_response_not_list(response, http_method, context, is_requirement)


# Function to save the ids generated during creation of the different object
# Taking account that response is not a list
def save_ids_only_response_not_list(response, http_method, context, is_requirement):
    if not isinstance(response, list):
        save_ids_response_is_not_error(response, http_method, context, is_requirement)


# Function to save the ids generated during creation of the different object
# Taking account that response is not an error type
def save_ids_response_is_not_error(response, http_method, context, is_requirement):
    if response.get('kind', None) != 'error':
        save_ids_according_type_of_request(response, http_method, context, is_requirement)


# Function to save the ids generated during creation of the different object
# Taking account that type of the http_method
def save_ids_according_type_of_request(response, http_method, context, is_requirement):
    if http_method.lower() == 'post':
        if context.table is None:
            save_to_delete(context, is_requirement)
        else:
            save_ids_data(context)
            context.save_response.append(response)
    elif http_method.lower() == 'get':
        context.save_response.append(response)


# Function to compare data between data list
def compare_data_list(data_created, data_obtained):
    data_equal = False
    count = 0
    for obj in data_created:
        for data in data_obtained:
            if obj.get('id', None) == data.get('id', None):
                for key in obj:
                    if obj[key] != data[key]:
                        assert data_equal is True
                count += 1
                break
    data_equal = verify_data_len(data_created, count)
    return data_equal


# Function to verify if lists of length is the same as count variable
def verify_data_len(data_created, count):
    data_equal = False
    if len(data_created) == count:
        data_equal = True
    return data_equal
