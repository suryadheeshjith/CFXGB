# -*- coding:utf-8 -*-

def load_json(path):
    import json
    lines = []
    with open(path) as f:
        for row in f.readlines():
            if row.strip().startswith("//"):
                continue
            lines.append(row)
    return json.loads("\n".join(lines))

def get_config_value(config, key, default_value, value_types, required=False, config_name=None):
    
    if config_name is not None:
        log_prefix = "[{}] ".format(config_name)
    else:
        log_prefix = ""
    if required and not key in config:
        raise ValueError("{}config={}, key={} is absent but it's required !!!".format(log_prefix, config, key))
    elif not key in config:
        return default_value
    value = config[key]
    # value type check
    if value is not None:
        value_type_match = True
        if value_types is None:
            value_types = []
        elif not isinstance(value_types, list):
            value_types = [value_types]
        for value_type in value_types:
            if not isinstance(value, value_type):
                value_type_match = False
                break
        if not value_type_match:
            raise ValueError("{}config={}, Value type not matched!!! key={}, value={}, value_types={}".format(
                log_prefix, config, key, value, value_types))
    return value
