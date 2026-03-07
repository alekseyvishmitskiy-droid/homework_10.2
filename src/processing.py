import ast

"""
В модуле processing напишите функцию filter_by_state,
которая принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
содержащий только те словари, у которых ключ
state соответствует указанному значению.
"""

"""
В том же модуле напишите функцию sort_by_date,
которая принимает список словарей и необязательный параметр,
задающий порядок сортировки (по умолчанию — убывание).
Функция должна возвращать новый список, отсортированный по дате (date).
"""


"Сортируем данные по state"


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по ключу 'date'"""
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)


def main(): # pragma: no cover
    user_input = input("Введите список транзакций:")

    try:
        data = ast.literal_eval(user_input)

        if not isinstance(data, list):
            print("Ошибка: Введенные данные должны быть списком.")
            return

        # Фильтрация по EXECUTED
        print("\n# Выход функции со статусом 'EXECUTED':")
        executed_res = filter_by_state(data)
        print(executed_res)

        # Фильтрация по CANCELED
        print("\n# Выход функции со статусом 'CANCELED':")
        canceled_res = filter_by_state(data, state='CANCELED')
        print(canceled_res)

        # Отдельная сортировка всего списка по дате
        print("\n# Весь список, отсортированный по дате (от новых к старым):")
        all_sorted = sort_by_date(data)
        print(all_sorted)

    except (ValueError, SyntaxError):
        print("Ошибка: Некорректный формат данных.")


if __name__ == "__main__": # pragma: no cover
    main()
