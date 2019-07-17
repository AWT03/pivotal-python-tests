def get_object_attribute_value(context, type_attribute, type_object):
    response = context.save_response
    object_attribute_value = ''
    for res in response:
        if res['kind'] == type_object.lower():
            object_attribute_value = res[type_attribute.lower()]
            break
    return object_attribute_value
