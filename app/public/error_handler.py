def new_error(error_name, error_message, model_fields):
    for field in model_fields:
        if field in error_message:
            return Exception('{e}: {f}'.format(e=error_name,f=field))

    