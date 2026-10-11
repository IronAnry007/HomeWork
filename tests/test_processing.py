import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование фильтрации списка словарей по заданному статусу state.
def test_filter_by_state_valid(for_test_filter_by_state_valid):
    assert filter_by_state(for_test_filter_by_state_valid) == [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
@pytest.fixture
def for_test_filter_by_state_without_state():
    return [
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570}]
def test_filter_by_state_without_state(for_test_filter_by_state_without_state):
    assert filter_by_state(for_test_filter_by_state_without_state) == []


# Параметризация тестов для различных возможных значений статуса state.
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{'date': '2019-07-03T18:35:29.512364', 'id': 414288290, 'state': 'EXECUTED'},
                {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
    ("CANCELED", [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
                {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'}]),
    ("UNKNOWN", [])])
def test_filter_by_state_mix(for_test_filter_by_state_mix, state, expected):
    assert filter_by_state(for_test_filter_by_state_mix, state) == expected


# Тестирование сортировки списка словарей по датам в порядке убывания.
def test_sort_by_date_valid_descending(for_test_filter_by_state_mix):
    assert sort_by_date(for_test_filter_by_state_mix) == [
        {'date': '2019-07-03T18:35:29.512364', 'id': 414288290, 'state': 'EXECUTED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]


# Тестирование сортировки списка словарей по датам в порядке возрастания.
def test_sort_by_date_ascending(for_test_filter_by_state_mix):
    assert sort_by_date(for_test_filter_by_state_mix, False) == [
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591},
        {'date': '2019-07-03T18:35:29.512364', 'id': 414288290, 'state': 'EXECUTED'}]


# Проверка корректности сортировки при одинаковых датах.
@pytest.mark.parametrize("transactions", [[
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 615064591, 'state': 'CANCELED'}
]])
def test_sort_by_date_same_date(transactions):
    assert sort_by_date(transactions) == [
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 615064591, 'state': 'CANCELED'}]


# Тесты на работу функции с некорректными или нестандартными форматами дат.
@pytest.fixture
def for_test_sort_by_date_not_data():
    return [
        {'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018--30T02:08:58.425572', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2019-07-03T18', 'id': 615064591, 'state': 'CANCELED'}]
def test_sort_by_date_not_data(for_test_sort_by_date_not_data):
    assert (sort_by_date(for_test_sort_by_date_not_data) ==
            [{'date': '2019-07-03T18', 'id': 615064591, 'state': 'CANCELED'},
             {'id': 939719570, 'state': 'EXECUTED'},
             {'date': '2018--30T02:08:58.425572', 'id': 594226727, 'state': 'CANCELED'}])
