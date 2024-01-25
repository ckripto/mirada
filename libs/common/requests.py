from typing import Optional

import allure
import requests


class Requests:
    @staticmethod
    @allure.step("Send POST request")
    def post(
        url,
        json_data,
        headers: Optional[dict] = None,
        verify: bool = False,
        allow_redirects: bool = False,
    ) -> requests.Response:
        response = requests.post(
            url, json=json_data, headers=headers, verify=verify, allow_redirects=allow_redirects
        )
        allure.attach(
            f"url: {url}\n"
            f"data: {json_data}\n"
            f"response code: {response.status_code}\n"
            f"response data: {response.text}",
            "POST request additional info",
            allure.attachment_type.TEXT,
        )
        return response

    @staticmethod
    @allure.step("Send GET request")
    def get(
            url, headers: Optional[dict] = None, verify: bool = False, allow_redirects: bool = False
    ) -> requests.Response:
        response = requests.get(
            url, headers=headers, verify=verify, allow_redirects=allow_redirects
        )
        allure.attach(
            f"url: {url}\n"
            f"response code: {response.status_code}\n"
            f"response data: {response.text}",
            "GET request additional info",
            allure.attachment_type.TEXT,
        )
        return response

    @staticmethod
    @allure.step("Send DELETE request")
    def delete(
            url, headers: Optional[dict] = None, verify: bool = False, allow_redirects: bool = False
    ) -> requests.Response:
        response = requests.delete(
            url, headers=headers, verify=verify, allow_redirects=allow_redirects
        )
        allure.attach(
            f"url: {url}\n"
            f"response code: {response.status_code}\n"
            f"response data: {response.text}",
            "DELETE request additional info",
            allure.attachment_type.TEXT,
        )
        return response
