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
    assert context.text is not None
    context.data_text = context.text
    do_request(context, feature, post_type, context.headers, True)


@given(u'I send a {post_type} request to {feature} with data from {config_file_path}')
def step_impl(context, post_type, feature, config_file_path):
    assert context.text is None
    context.data_text = get_data_text(join(context.path_data_files, config_file_path))
    do_request(context, feature, post_type, context.headers, True)


@when(u'I send a {post_type} request to {feature} with data')
def step_impl(context, post_type, feature):
    assert context.text is not None
    context.data_text = context.text
    do_request(context, feature, post_type, context.headers, False)


@when(u'I send a {post_type} request to {feature} with data from {config_file_path}')
def step_impl(context, post_type, feature, config_file_path):
    assert context.text is None
    context.data_text = get_data_text(join(context.path_data_files, config_file_path))
    do_request(context, feature, post_type, context.headers, False)


@when(u'I send a {post_type} request to {feature}')
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
    context.data_text = get_data_text(join(context.path_data_files, config_file_path))
    must_contain = generate_data(context)
    assert must_contain is not None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    for tag in must_contain:
        assert tag in api_response
        assert api_response[tag] == must_contain[tag]


@then('I expect the single response contains')
def step_impl(context):
    assert context.text is not None
    must_contain = generate_data(context)
    assert must_contain is not None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    for tag in must_contain:
        assert tag in api_response
        assert api_response[tag] == must_contain[tag]


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
    assert isinstance(api_response, list)
    assert len(api_response) == int(n)


@step('delete urls marked to delete')
def step_impl(context):
    for url in context.to_delete:
        context.api.set_url(url)
        context.api.do_request('delete', headers=context.headers)
