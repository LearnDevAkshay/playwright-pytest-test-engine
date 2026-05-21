from playwright.sync_api import Playwright

print("NEW PLAYWRIGHT CONFTEST LOADED")
import os

import pytest


from pathlib import Path

from utils.read_test_data_file import TestDataReader


@pytest.fixture
def getdata(request):
    ROOT_DIR = Path(__file__).resolve().parent
    test_case_name = request.node.originalname
    data_folder_path = os.path.join(ROOT_DIR,"data/csv")
    test_data_list = TestDataReader.read_all_csv_by_test_case(data_folder_path,test_case_name)
    for index, data in enumerate(test_data_list, start=1):
        setattr(request.cls, f"td{index}", data)





@pytest.fixture(scope="function")
def page_instance(page):

    page.set_viewport_size({
        "width": 1920,
        "height": 1080
    })

    yield page

    page.close()



@pytest.fixture()
def api_request(playwright: Playwright):

    request_context = playwright.request.new_context(
        extra_http_headers={

        "Content-Type": "application/json",
        "Accept": "application/json"

        }
    )

    yield request_context

    request_context.dispose()


