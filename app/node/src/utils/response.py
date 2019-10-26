def json_success(data):
    return {"success": True, "data": data, "error": None}


def json_error(code, message, info=None):
    return {
        "success": False,
        "data": None,
        "error": {"code": int(code), "message": message, "info": info},
    }
