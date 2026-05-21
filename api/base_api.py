import allure

from utils.environment import ENVIRONMENT


class BaseAPI:

    def __init__(self, api_request):

        self.api_request = api_request

        self.base_url = ENVIRONMENT["booking_base_url"]

    @allure.step("Perform GET request")
    def get(
            self,
            endpoint,
            params=None,
            headers=None
    ):
        print(f"{self.base_url}{endpoint}")

        response = self.api_request.get(
            url=f"{self.base_url}{endpoint}",
            params=params,
            headers=headers
        )



        return response

    @allure.step("Perform POST request")
    def post(
            self,
            endpoint,
            payload=None,
            headers=None
    ):

        response = self.api_request.post(
            url=f"{self.base_url}{endpoint}",
            data=payload,
            headers=headers
        )



        return response

    @allure.step("Perform PUT request")
    def put(
            self,
            endpoint,
            payload=None,
            headers=None
    ):

        response = self.api_request.put(
            url=f"{self.base_url}{endpoint}",
            data=payload,
            headers=headers
        )


        return response

    @allure.step("Perform DELETE request")
    def delete(
            self,
            endpoint,
            headers=None
    ):

        response = self.api_request.delete(
            url=f"{self.base_url}{endpoint}",
            headers=headers
        )



        return response

