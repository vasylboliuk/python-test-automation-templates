import dataclasses
import json as json_lib
import logging

import requests
from requests import Request

from core.utils.dto_converter import DtoConverter

LOGGER = logging.getLogger(__name__)


class BaseEndpoint:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method, path, data=None, json=None, headers=None, params=None, **kwargs):
        """
        ore method to Send Request
        :param method: HTTP method as string (GET, POST, PUT, DELETE)
        :param path: url path
        :param data: data to be sent
        :param json: json data to be sent
        :param headers: request headers
        :param params: query params if needed
        :param kwargs: other libs kwargs attributes
        :return: response
        """
        url = self.base_url + path

        expected_status_code: int = kwargs.get("status_code", None)
        if expected_status_code is not None:
            del kwargs["status_code"]
        # Build request
        req = requests.Request(method, url, data=data, json=json, headers=headers, params=params, **kwargs)
        prepared = req.prepare()
        self._log_request(req)
        # Send request
        response = self.session.send(prepared)
        self._log_response(response, )
        if expected_status_code is not None:
            assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    def _log_request(self, request: Request):
        prepared = request.prepare()
        request_body = self._build_request_as_pretty_json(prepared.body)
        log_request = f"Request:\n" \
                      f"Request method: {prepared.method}\n" \
                      f"Request URI:    {prepared.url}\n" \
                      f"Query params:   {request.params}\n" \
                      f"Headers:        {prepared.headers}\n" \
                      f"Body:\n" \
                      f"{request_body}\n"
        LOGGER.info(log_request)

    def _log_response(self, response):
        response_json = response.json()
        log_data_response = json_lib.dumps(response_json, indent=4)
        log_response = f"Response:\n" \
                       f"Status code:      {response.status_code}\n" \
                       f"Response Headers: {response.headers}\n" \
                       f"Response Cookies: {response.cookies.get_dict()}\n" \
                       f"Response Data:\n" \
                       f"{log_data_response}"
        LOGGER.info(log_response)

    def _build_request_as_pretty_json(self, request_data):
        try:
            result_response = request_data.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            result_response = request_data
        if isinstance(request_data, str):
            result_response = DtoConverter.string_to_pretty_json(request_data)
        if isinstance(request_data, dict):
            result_response = DtoConverter.dict_to_pretty_json(request_data)
        return result_response

    def get(self, path, headers=None, **kwargs):
        return self._request('GET', path, headers=headers, **kwargs)

    def post(self, path, data=None, json=None, headers=None, **kwargs):
        return self._request('POST', path, data=data, json=json, headers=headers, **kwargs)

    def put(self, path, data=None, json=None, headers=None, **kwargs):
        return self._request('PUT', path, data=data, json=json, headers=headers, **kwargs)

    def delete(self, path, headers=None, **kwargs):
        return self._request('DELETE', path, headers=headers, **kwargs)

    def dataclass_deserialize(self, data, cls):
        if isinstance(data, list):
            return [cls.from_dict(item) for item in data]
        else:
            return cls.from_dict(data)

    def dataclass_serialize(self, data):
        return json_lib.dumps(dataclasses.asdict(data))

    def pydentic_deserialize(self, data, model_class):
        if isinstance(data, list):
            return [model_class(**item) for item in data]
        else:
            return model_class(**data)

    def pydentic_serialize(self, obj):
        return json_lib.dumps(obj)
