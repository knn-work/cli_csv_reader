from abc import ABC, abstractmethod

from base.table import Table


class Command(ABC):
    """
    Абстрактная команда, которая должна реализовать метод execute.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Уникальное имя команды (используется как ключ аргумента).
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self, table: Table, arg_value: str) -> Table:
        """
        Выполняет команду, модифицируя таблицу.

        Args:
            table: Таблица для обработки
            arg_value: Аргумент команды из CLI
        Returns:
            Новая таблица с результатом
        """
        raise NotImplementedError
