import falcon


def validate_params(param_list, *params):
    params_needed = []
    given_params = list(params)
    for param in param_list:
        if param not in given_params:
            params_needed.append(param)

    if len(params_needed) > 0:
        raise falcon.HTTPBadRequest(f'Missing parameters: {params_needed}')
