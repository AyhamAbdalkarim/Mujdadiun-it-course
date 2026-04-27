def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502:
            return "Server error"
        case _:
            return "Other"


print(http_status(404))
