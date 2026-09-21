from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date

data: List[Dict[str, Any]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Для def filter_by_state
# Тест 1: Фильтрация по умолчанию (EXECUTED)
executed_only = filter_by_state(data)
print(f"\n Фильтр по умолчанию ('EXECUTED'): найдено {len(executed_only)} записей")
for item in executed_only:
    print(f"   - ID: {item['id']}, State: {item['state']}")

# Тест 2: Фильтрация по конкретному состоянию (CANCELED)
canceled_only = filter_by_state(data, "CANCELED")
print(f"\n Фильтр ('CANCELED'): найдено {len(canceled_only)} записей")
for item in canceled_only:
    print(f"   - ID: {item['id']}, State: {item['state']}")

# Для def sort_by_date
sorted_desc = sort_by_date(data)
print("\n Сортировка (убывание, reverse=True):")
for item in sorted_desc:
    print(f"   ID: {item['id']}, Дата: {item['date']}")

sorted_desc = sort_by_date(data, reverse=False)
print("\n Сортировка (возрастание, reverse=False):")
for item in sorted_desc:
    print(f"   ID: {item['id']}, Дата: {item['date']}")
