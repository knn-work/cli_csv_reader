from typing import Any

from tabulate import tabulate


class Table:
    """
    Класс, представляющий таблицу с заголовками, строками и автоматически определяемыми типами.

    """

    def __init__(self):
        self.__head: list[str] | None = None
        self.__types: list[type | None] | None = None
        self.__head_set: set[str] | None = None
        self.__rows: list[list[Any]] = []

    @property
    def head(self) -> list[str] | None:
        """
        Возвращает заголовки таблицы.
        Returns:
            Список названий столбцов или None.
        """
        return self.__head

    @head.setter
    def head(self, head: list[str]) -> None:
        """
        Устанавливает заголовки таблицы и инициализирует структуру типов.
        Args:
            head: Список названий столбцов.
        """
        self.__head = head
        self.__types = [None] * len(head)
        self.__head_set = set(head)

    def get_column(self, position: int) -> list[Any]:
        """Возвращает столбец по позиции.

        Args:
            position: Индекс столбца.
        Returns:
            Список значений из указанного столбца.
        """
        return [row[position] for row in self.__rows]

    @property
    def rows(self) -> list[list[Any]]:
        """
        Возвращает все строки таблицы.
        Returns:
            Список строк.
        """
        return self.__rows

    @property
    def types(self) -> list[type | None] | None:
        """
        Возвращает список типов данных по столбцам.
        Returns:
            Список типов (float или str), либо None, если таблица пуста.
        """
        return self.__types

    def add_row(self, row: list[str]) -> None:
        """
        Добавляет строку в таблицу, автоматически определяя типы значений.
        Args:
            row: Список строковых значений, соответствующих столбцам.
        """
        new_row: list[Any] = []
        for i, element in enumerate(row):
            if self.__types[i] is None:
                try:
                    self.__types[i] = float
                    element = float(element)
                except ValueError:
                    self.__types[i] = str
            new_row.append(self.__types[i](element))
        self.__rows.append(new_row)



    def __str__(self) -> str:
        return tabulate([self.__head] + self.__rows) if self.__head else "Empty table"

    def __contains__(self, item: str) -> bool:
        """
        Проверяет, есть ли указанный заголовок в таблице.
        Args:
            item: Имя столбца.
        Returns:
            True, если столбец есть в заголовках, иначе False.
        """
        return item in self.__head_set if self.__head_set else False