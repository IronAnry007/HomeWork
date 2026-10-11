import pytest

from src.processing import filter_by_state

# Тестирование фильтрации списка словарей по заданному статусу state.
def test_filter_by_state_valid(for_test_filter_by_state_valid):
    assert filter_by_state(for_test_filter_by_state_valid) == [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]


# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
def test_filter_by_state_without_state():
    assert filter_by_state([
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570}]) == []


# Параметризация тестов для различных возможных значений статуса state.
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{'date': '2019-07-03T18:35:29.512364', 'id': 414288290, 'state': 'EXECUTED'},
                {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]),
    ("CANCELED", [{'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
                {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'}]),
    ("UNKNOWN", [])])
def test_filter_by_state_mix(for_test_filter_by_state_mix, state, expected):
    assert filter_by_state(for_test_filter_by_state_mix, state) == expected
