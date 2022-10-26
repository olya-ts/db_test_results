import requests

from framework.utils.logger import Logger
from framework.constants import status_codes


class GeneralAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, path: str):
        Logger.info("Sending GET request to the url " + self.base_url + path)
        response = requests.get(self.base_url + path)
        setattr(self, "response", response)
        return response

    def send_post_request(self, path: str, data: dict):
        Logger.info("Sending POST request to the url " + self.base_url + path)
        response = requests.post(self.base_url + path, data)
        setattr(self, "response", response)
        return response

    def send_put_request(self, path: str, data: dict):
        Logger.info("Sending PUT request to the url " + self.base_url + path)
        response = requests.put(self.base_url + path, data)
        setattr(self, "response", response)
        return response

    def send_patch_request(self, path: str, data: dict):
        Logger.info("Sending PATCH request to the url " + self.base_url + path)
        response = requests.patch(self.base_url + path, data)
        setattr(self, "response", response)
        return response

    def send_delete_request(self, path: str):
        Logger.info("Sending DELETE request to the url " + self.base_url + path)
        response = requests.delete(self.base_url + path)
        setattr(self, "response", response)
        return response

    def get_status_code(self):
        Logger.info("Getting status-code")
        status_code = getattr(self, "response").status_code
        return status_code

    def get_header_by_key(self, key: str):
        Logger.info("Getting header by the key " + key)
        header = getattr(self, "response").headers[key]
        return header

    def check_status_code(self, expected_status_code: int = status_codes.STATUS_200_OK):
        Logger.info("Checking if the status code equals " + str(expected_status_code))
        return self.get_status_code() == expected_status_code
