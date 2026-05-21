from api.base_api import BaseAPI

class BookingAPI(BaseAPI):

    def get_booking(self, booking_id):

        endpoint = f"/booking/{booking_id}"

        response = self.get(endpoint)

        return response

    def create_booking(self, payload):
        endpoint = "/booking"

        return self.post(
            endpoint=endpoint,
            payload=payload
        )