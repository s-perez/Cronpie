import re

TIME_REGEX = '^(\*|(\d+(-\d+)?,)*\d+(-\d+)?)(\/\d+)?$'

def _validate_time_expr_format(time_expr):
    return True if re.fullmatch(TIME_REGEX, time_expr) else False


def is_cron_time_expression(instance, attribute, value):
    is_str = isinstance(value, str)
    if is_str:
        elements = value.split(' ')
        has_right_length = len(elements) == 5
        is_valid_time = all(_validate_time_expr_format(x) for x in elements)
        error = not all([is_str, has_right_length, is_valid_time])
    else:
        error = True
    if error:
        raise ValueError("{} is not a valid time expression".format(value))

def is_non_empty_list(instance, attribute, value):
    is_list = isinstance(value, list)
    if is_list:
        error = not len(value) > 0

    if error:
        raise ValueError("{} is not a valid command".format(value))
