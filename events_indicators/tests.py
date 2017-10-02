from datetime import datetime
from .api_connections import RequestEventsRawData


def test_success_request():
    current_time = datetime.now().__str__()
    request_events_raw_data = RequestEventsRawData(current_time)
    response_events_raw_data = request_events_raw_data.response
    response_status_code = response_events_raw_data.status_code
    assert response_status_code == 200


def test_data_content():
    current_time = datetime.now().__str__()
    request_events_raw_data = RequestEventsRawData(current_time)
    events_raw_data = request_events_raw_data.data
    type_events_raw_data = type(events_raw_data)
    empty_list = []
    assert type_events_raw_data == type(empty_list)


def test_data_lenght():
    current_time = datetime.now().__str__()
    request_events_raw_data = RequestEventsRawData(current_time)
    events_raw_data = request_events_raw_data.data_length
    type_events_raw_data = type(events_raw_data)
    integer = 1
    assert type_events_raw_data == type(integer)
