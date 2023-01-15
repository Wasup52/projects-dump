def get_error(http_code):
    if http_code == 400:
        return "Bad request"
    elif http_code == 401:
        return "Unauthorized"
    elif http_code == 403:
        return "Forbidden"
    elif http_code == 404:
        return "Not found"
    elif http_code == 405:
        return "Method not allowed"
    elif http_code == 409:
        return "Conflict"
    elif http_code == 410:
        return "Gone"
    elif http_code == 429:
        return "Too many requests"
    elif http_code == 500:
        return "Internal server error"
    elif http_code == 503:
        return "Service unavailable"
    else:
        return "Unknown error"