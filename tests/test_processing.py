import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data, state, expected_filtered_data",
    [
        (
            [{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        ([{"state": "CANCELED"}, {"state": "CANCELED"}], "EXECUTED", []),
        ([{"state": "DRAFT"}, {"state": "PENDING"}, {"state": "EXECUTED"}], "PENDING", [{"state": "PENDING"}]),
        ([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "EXECUTED"}], "DRAFT", []),
    ],
)
def test_filter_by_state(data, state, expected_filtered_data):
    assert filter_by_state(data, state) == expected_filtered_data


def test_filter_by_state_default_state():
    data = [{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "EXECUTED"}]
    expected_filtered_data = [{"state": "EXECUTED"}, {"state": "EXECUTED"}]
    assert filter_by_state(data) == expected_filtered_data


@pytest.mark.parametrize(
    "data, reverse, expected_sorted_data",
    [
        (
            [
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2024-01-01T00:00:00.000000"},
                {"date": "2023-12-30T12:34:56.789012"},
            ],
            True,
            [
                {"date": "2024-01-01T00:00:00.000000"},
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2023-12-30T12:34:56.789012"},
            ],
        ),
        (
            [
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2024-01-01T00:00:00.000000"},
                {"date": "2023-12-30T12:34:56.789012"},
            ],
            False,
            [
                {"date": "2023-12-30T12:34:56.789012"},
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2024-01-01T00:00:00.000000"},
            ],
        ),
        (
            [
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2023-12-30T12:34:56.789012"},
            ],
            True,
            [
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2023-12-31T23:59:59.999999"},
                {"date": "2023-12-30T12:34:56.789012"},
            ],
        ),
    ],
)
def test_sort_by_date(data, reverse, expected_sorted_data):
    assert sort_by_date(data, reverse) == expected_sorted_data
