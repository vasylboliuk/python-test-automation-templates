from enum import Enum


class HttpStatus(Enum):

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, code, summary):
        self.code = code
        self.summary = summary

    OK = 200, "OK"
    CREATED = 201, "Created"
    NO_CONTENT = 204, "No Content"

    BAD_REQUEST = 400, "Bad Request"
    UNAUTHORIZED = 401, "Unauthorized"
    FORBIDDEN = 403, "Forbidden"

    INTERNAL_SERVER_ERROR = 500, "Internal Server Error"
    NOT_IMPLEMENTED = 501, "Not Implemented"
    BAD_GATEWAY = 503, "Bad Gateway"
    SERVICE_UNAVAILABLE = 504, "Service Unavailable"


