from behave import given, then, when, step
from core.features.steps.functions import *
from core.request_api.generic_api import GenericApi


@given('I start a connection with the API')
def step_impl(context):
    api = GenericApi()
    context.api = api
    context.to_delete = []
    context.saved_ids = ['']
    context.path_data_files = ''
    context.headers = None


@given(u'I send a {post_type} request to {feature} with data')
def step_impl(context, post_type, feature):
    if context.text:
        context.data_text = context.text
        do_request(context, feature, post_type, context.headers, True)
    elif context.table:
        for row in context.table:
            current_time_random = datetime.now().strftime('_%d-%m-%Y_%H:%M:%S.%f')[:-3]
            context.current_time_random = current_time_random
            context.data_row = row
            context.data_text = None
            do_request(context, feature, post_type, context.headers, False)


@when(u'I send a "{post_type}" request to "{feature}" with data "{description}" "{complete}" "{position}"')
def step_impl(context, post_type, feature, description, complete, position):
    data_dict = {'description':description, 'complete':bool(complete), 'position':int(position)}
    data = dumps(data_dict)
    context.data = data
    context.data_text = None
    content_type = context.api.get_config()['Content-Type']
    context.headers.update({"Content-Type": content_type})
    do_request(context, feature, post_type, context.headers, True)


@given(u'I send a {post_type} request to {feature} with data from {config_file_path}')
def step_impl(context, post_type, feature, config_file_path):
    assert context.text is None
    context.data_text = get_data_text(join(context.path_data_files, *config_file_path.split("/")))
    do_request(context, feature, post_type, context.headers, True)


@when(u'I send a {post_type} request to {feature} with data')
def step_impl(context, post_type, feature):
    if context.text is not None:
        context.data_text = context.text
        do_request(context, feature, post_type, context.headers, False)
    elif context.table:
        for row in context.table:
            current_time_random = datetime.now().strftime('_%d-%m-%Y_%H:%M:%S.%f')[:-3]
            context.current_time_random = current_time_random
            context.data_row = row
            context.data_text = None
            do_request(context, feature, post_type, context.headers, False)


@when(u'I send a {post_type} request to {feature} with data from {config_file_path}')
def step_impl(context, post_type, feature, config_file_path):
    assert context.text is None
    context.data_text = dumps(get_data_text(join(context.path_data_files, *config_file_path.split("/"))))
    context.headers['Content-Type'] = 'application/json'
    do_request(context, feature, post_type, context.headers, False)


@step(u'I send a {post_type} request to {feature}')
def step_impl(context, post_type, feature):
    assert context.text is None
    context.data_text = {}
    do_request(context, feature, post_type, context.headers, False)


@when('I make sure last id is None')
def set_imp(context):
    context.saved_ids[-1] = ''


@then('I expect status code is {status_code}')
def step_impl(context, status_code):
    assert str(context.api.get_status()) == str(status_code)


@then('I expect the single response contains previously set values')
def step_impl(context):
    must_contain = generate_data(context)
    assert must_contain is not None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    for tag in must_contain:
        assert tag in api_response
        assert api_response[tag] == must_contain[tag]


@then('I expect the single response contains data from {config_file_path}')
def step_impl(context, config_file_path):
    assert context.text is None
    context.data_text = get_data_text(join(context.path_data_files, *config_file_path.split("/")))
    must_contain = generate_data(context)
    assert must_contain is not None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    for tag in must_contain:
        assert tag in api_response
        if not isinstance(must_contain[tag], list):
            assert api_response[tag] == must_contain[tag]


@then('I expect the single response contains')
def step_impl(context):
    assert context.text is not None
    context.data_text = context.text
    must_contain = generate_data(context)
    assert must_contain is not None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    for tag in must_contain:
        assert tag in api_response
        assert str(api_response[tag]).lower() == str(must_contain[tag]).lower()


@then('I expect the response {field} is not null')
def step_impl(context, field):
    api_response = loads(context.api.get_full_response())
    assert api_response[field] is not None


@then('I expect the response is a list')
def step_impl(context):
    api_response = loads(context.api.get_full_response())
    assert isinstance(api_response, list)


@then('I expect the response list contains {n} values')
def step_imp(context, n):
    api_response = loads(context.api.get_full_response())
    context.list_data = api_response
    assert isinstance(api_response, list)
    assert len(api_response) == int(n)

#@then('I expect the response list contains {n} values')
#def step_imp(context, n):
#    api_response = loads(context.api.get_full_response())
#    for info in api_response:
#        if info['name'].find('multiple_projects'):
#            #context.list_data.append(info)
#            print("True")
#    if not context.list_data:
#        context.list_data = api_response
#    assert isinstance(api_response, list)
#    assert len(api_response) == int(n)


@step('delete urls marked to delete')
def step_impl(context):
    for url in context.to_delete:
        context.api.set_url(url)
        context.api.do_request('delete', headers=context.headers)


@then(u'I expect the items\' ids obtained are equal to the items\' ids created before')
def step_impl(context):
    ids_list = context.ids_list
    list_data = context.list_data
    count = 0
    for data in list_data:
        item_id = data.get('id', None)
        if str(item_id) in ids_list:
            count = count + 1
    assert (len(ids_list) == count)


@then(u'I expect the items\' value obtained are equal to the items\' value created before')
def step_impl(context):
    data_created = context.save_response
    data_obtained = context.list_data
    equal = False
    count = 0
    if len(data_obtained) == len(data_created):
        for obj in data_created:
            for data in data_obtained:
                if obj.get('id', None) == data.get('id', None):
                    for key in obj:
                        if obj[key] != data[key]:
                            assert equal is True
                    count += 1
                    break
        if len(data_created) == count:
            equal = True
    else:
        equal = False
    assert equal is True


@then(u'I expect this error {error_key} is thrown')
def step_impl(context, error_key):
    api_response = loads(context.api.get_full_response())
    messages = context.api.get_message()
    error_validate = messages.get(error_key)
    if api_response is not None:
        for key in error_validate:
            assert error_validate[key] in api_response[key]


@when(u'I send a {type_method} request to {feature} with data in {json_file}')
def step_impl(context, type_method, feature, json_file):
    path_data_file = join(context.path_data_files, json_file)
    file = open(path_data_file, 'r')
    data = file.read()
    context.data = data
    context.data_text = None
    content_type = context.api.get_config()['Content-Type']
    context.headers.update({"Content-Type": content_type})
    do_request(context, feature, type_method, context.headers, True)


@then(u'I expect the general problem is {general_problem}')
def step_impl(context, general_problem):
    api_response = loads(context.api.get_full_response())
    if api_response is not None:
        assert api_response.get("general_problem", None) == general_problem


@then('I save the response id as URL reference')
def step_impl(context):
    context.saved_ids.append('')
