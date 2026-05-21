import allure

from api.booking_api import BookingAPI
from utils.json_reader import JsonReader
from utils.schema_validator import SchemaValidator


@allure.suite("Booking API")
class TestBookingAPI:

    @allure.title("Verify Get Booking Details")
    def test_get_booking_details(self, api_request):

        booking_api = BookingAPI(api_request)

        response = booking_api.get_booking(2)

        response_body = response.json()

        assert response.status == 200

        SchemaValidator.validate_schema(
            response_body,
            "data/json/booking_schema.json"
        )

    @allure.title("Verify Create Booking")
    def test_create_booking(
            self,
            api_request
    ):
        booking_api = BookingAPI(api_request)

        payload = JsonReader.read_json_file(
            "data/json/create_booking_payload.json"
        )

        response = booking_api.create_booking(payload)

        assert response.status == 200

        response_body = response.json()

        assert response_body["booking"]["firstname"] == "Jim"

        assert response_body["booking"]["lastname"] == "Brown"